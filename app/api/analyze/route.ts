// import { type NextRequest, NextResponse } from "next/server"

// export async function POST(request: NextRequest) {
//   try {
//     const body = await request.json()
//     const { username, platforms, aiModels, exportFormats } = body

//     // Generate a unique investigation ID
//     const investigationId = `inv_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`

//     // Call Python backend directly without database dependency
//     const pythonBackendUrl = process.env.PYTHON_BACKEND_URL || "http://localhost:8000"

//     console.log(`Calling Python backend at: ${pythonBackendUrl}/analyze`)

//     const response = await fetch(`${pythonBackendUrl}/analyze`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({
//         investigation_id: investigationId,
//         username,
//         platforms,
//         ai_models: aiModels,
//         export_formats: exportFormats,
//       }),
//     })

//     if (!response.ok) {
//       const errorText = await response.text()
//       console.error("Python backend error:", errorText)
//       throw new Error(`Python backend failed: ${response.status} - ${errorText}`)
//     }

//     const result = await response.json()

//     return NextResponse.json({
//       investigationId: investigationId,
//       status: "success",
//       message: "Analysis completed successfully",
//       results: result.results,
//       exportUrls: result.export_urls || [],
//     })
//   } catch (error) {
//     console.error("Analysis error:", error)
//     return NextResponse.json(
//       {
//         error: error instanceof Error ? error.message : "Analysis failed",
//         details: "Check if Python backend is running on port 8000",
//       },
//       { status: 500 },
//     )
//   }
// }


// new above good


// import { type NextRequest, NextResponse } from "next/server"
// import { PrismaClient } from "@prisma/client"

// const prisma = new PrismaClient()

// export async function POST(request: NextRequest) {
//   try {
//     const body = await request.json()
//     const { username, platforms, aiModels, exportFormats } = body

//     // Create investigation record
//     const investigation = await prisma.investigation.create({
//       data: {
//         userId: "anonymous", // For now, using anonymous user
//         targetUser: username,
//         platform: platforms.join(","),
//         status: "IN_PROGRESS",
//       },
//     })

//     // Call Python backend
//     const pythonBackendUrl = process.env.PYTHON_BACKEND_URL || "http://localhost:8000"

//     const response = await fetch(`${pythonBackendUrl}/analyze`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({
//         investigation_id: investigation.id,
//         username,
//         platforms,
//         ai_models: aiModels,
//         export_formats: exportFormats,
//       }),
//     })

//     if (!response.ok) {
//       throw new Error("Python backend analysis failed")
//     }

//     const result = await response.json()

//     // Update investigation status
//     await prisma.investigation.update({
//       where: { id: investigation.id },
//       data: {
//         status: "COMPLETED",
//         completedAt: new Date(),
//       },
//     })

//     return NextResponse.json({
//       investigationId: investigation.id,
//       status: "success",
//       message: "Analysis completed successfully",
//     })
//   } catch (error) {
//     console.error("Analysis error:", error)
//     return NextResponse.json({ error: "Analysis failed" }, { status: 500 })
//   }
// }


// new 
import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  console.log("=== ANALYZE API CALLED ===")

  try {
    const body = await request.json()
    console.log("Request body:", body)

    // Extract data with proper defaults
    const {
      username,
      platforms,
      aiModels = ["sentiment", "ner"], // Default AI models
      exportFormats = ["csv", "json"], // Default export formats
      investigationId,
    } = body

    console.log("Parsed data:", { username, platforms, aiModels, exportFormats })

    // Generate investigation ID if not provided
    const finalInvestigationId = investigationId || `inv_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
    console.log("Investigation ID:", finalInvestigationId)

    // Python backend URL
    const pythonBackendUrl = process.env.PYTHON_BACKEND_URL || "http://localhost:8000"
    console.log("Backend URL:", pythonBackendUrl)

    // Test backend connection with multiple attempts
    console.log("Testing Python backend connection...")

    let healthResponse
    let connectionError = null

    // Try multiple connection attempts
    for (let attempt = 1; attempt <= 3; attempt++) {
      try {
        console.log(`Connection attempt ${attempt}/3...`)

        healthResponse = await fetch(`${pythonBackendUrl}/health`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
          signal: AbortSignal.timeout(5000),
        })

        if (healthResponse.ok) {
          const healthData = await healthResponse.json()
          console.log("Python backend health check passed:", healthData)
          connectionError = null
          break
        } else {
          throw new Error(`HTTP ${healthResponse.status}: ${healthResponse.statusText}`)
        }
      } catch (error) {
        connectionError = error
        console.log(`✗ Attempt ${attempt} failed:`, error instanceof Error ? error.message : String(error))

        if (attempt < 3) {
          console.log("Waiting 2 seconds before retry...")
          await new Promise((resolve) => setTimeout(resolve, 2000))
        }
      }
    }

    // If all connection attempts failed
    if (connectionError) {
      console.error("All connection attempts failed")

      return NextResponse.json(
        {
          error: "Python backend is not running or not accessible",
          details: {
            url: pythonBackendUrl,
            lastError: connectionError instanceof Error ? connectionError.message : String(connectionError),
            attempts: 3,
          },
          solutions: [
            "1. Make sure Python backend is running: cd backend && python main.py",
            "2. Check if port 8000 is available",
            "3. Verify firewall settings",
            "4. Try restarting the backend server",
          ],
          troubleshooting: {
            checkBackend: `Visit ${pythonBackendUrl}/health in your browser`,
            startCommand: "cd backend && python main.py",
            logLocation: "Check backend console for error messages",
          },
        },
        { status: 503 },
      )
    }

    // Call analysis endpoint
    console.log("Calling Python backend for analysis...")

    const analysisPayload = {
      investigation_id: finalInvestigationId,
      username,
      platforms,
      ai_models: aiModels,
      export_formats: exportFormats,
    }

    console.log("Analysis payload:", analysisPayload)

    const analysisResponse = await fetch(`${pythonBackendUrl}/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(analysisPayload),
      signal: AbortSignal.timeout(300000), // 5 minute timeout
    })

    console.log("Python backend response status:", analysisResponse.status)

    if (!analysisResponse.ok) {
      const errorText = await analysisResponse.text()
      console.error("Python backend error response:", errorText)

      let errorData
      try {
        errorData = JSON.parse(errorText)
      } catch {
        errorData = { message: errorText }
      }

      return NextResponse.json(
        {
          error: `Analysis failed (HTTP ${analysisResponse.status})`,
          details: errorData,
          investigationId: finalInvestigationId,
          timestamp: new Date().toISOString(),
        },
        { status: analysisResponse.status },
      )
    }

    const result = await analysisResponse.json()
    console.log("✓ Analysis completed successfully")

    return NextResponse.json({
      investigationId: finalInvestigationId,
      status: "success",
      message: "Analysis completed successfully",
      results: result.results || {},
      exportUrls: result.export_urls || [],
      timestamp: new Date().toISOString(),
    })
  } catch (error) {
    console.error("=== API ERROR ===")
    console.error("Error:", error)

    // Handle specific error types
    if (error instanceof TypeError && error.message.includes("fetch")) {
      return NextResponse.json(
        {
          error: "Network connection failed",
          details: "Cannot connect to Python backend",
          solutions: [
            "1. Start the backend: cd backend && python main.py",
            "2. Check if port 8000 is available",
            "3. Verify the backend is running at http://localhost:8000",
          ],
          originalError: error.message,
        },
        { status: 503 },
      )
    }

    if (error instanceof Error && error.name === "AbortError") {
      return NextResponse.json(
        {
          error: "Request timeout",
          details: "The request took too long to complete",
          solutions: [
            "1. Try again with fewer platforms",
            "2. Check backend performance",
            "3. Increase timeout if needed",
          ],
        },
        { status: 408 },
      )
    }

    return NextResponse.json(
      {
        error: "Internal server error",
        details: error instanceof Error ? error.message : "Unknown error",
        type: error?.constructor?.name || "Unknown",
        timestamp: new Date().toISOString(),
        solutions: [
          "1. Check the browser console for more details",
          "2. Verify the backend is running",
          "3. Try refreshing the page",
        ],
      },
      { status: 500 },
    )
  }
}
