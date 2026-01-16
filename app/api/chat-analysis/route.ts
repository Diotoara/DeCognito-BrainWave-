import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const { message, context } = await request.json()

    // Call Python backend for Gemini analysis
    const response = await fetch(`${process.env.PYTHON_BACKEND_URL}/chat-analysis`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
        context,
      }),
    })

    if (!response.ok) {
      throw new Error(`Backend responded with status: ${response.status}`)
    }

    const data = await response.json()

    return NextResponse.json({
      response: data.response || "I'm having trouble processing your request right now.",
      model: data.model || "gemini-1.5-flash",
    })
  } catch (error) {
    console.error("Chat analysis error:", error)

    // Fallback response
    return NextResponse.json({
      response:
        "I'm currently experiencing technical difficulties. Please try again later or check if the Python backend is running.",
      error: true,
    })
  }
}
