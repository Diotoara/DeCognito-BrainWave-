// "use client"

// import { useState, useEffect, useCallback } from "react"
// import { MatrixBackground } from "@/components/matrix-background"

// interface Investigation {
//   id: string
//   targetUser: string
//   platforms: string[]
//   status: "pending" | "in-progress" | "completed" | "failed"
//   createdAt: string
//   completedAt?: string
//   results?: Record<string, unknown>
// }

// type StatusFilter = "all" | Investigation["status"]

// export default function ReportsPage() {
//   const [investigations, setInvestigations] = useState<Investigation[]>([])
//   const [filteredInvestigations, setFilteredInvestigations] = useState<Investigation[]>([])
//   const [searchTerm, setSearchTerm] = useState("")
//   const [statusFilter, setStatusFilter] = useState<StatusFilter>("all")
//   const [loading, setLoading] = useState(true)
//   const [error, setError] = useState<string | null>(null)

//   // Load investigations from localStorage
//   const loadInvestigations = useCallback(() => {
//     try {
//       const stored = localStorage.getItem("osint_investigations")
//       if (stored) {
//         const data = JSON.parse(stored) as Investigation[]
//         setInvestigations(data)
//       }
//     } catch (err) {
//       console.error("Failed to load investigations:", err)
//       setError("Failed to load investigations. Please refresh the page.")
//     } finally {
//       setLoading(false)
//     }
//   }, [])

//   // Filter investigations based on search and status
//   const filterInvestigations = useCallback(() => {
//     let filtered = [...investigations]

//     if (searchTerm) {
//       const term = searchTerm.toLowerCase()
//       filtered = filtered.filter(
//         (inv) =>
//           inv.targetUser.toLowerCase().includes(term) ||
//           inv.id.toLowerCase().includes(term)
// )
//     }

//     if (statusFilter !== "all") {
//       filtered = filtered.filter((inv) => inv.status === statusFilter)
//     }

//     setFilteredInvestigations(filtered)
//   }, [investigations, searchTerm, statusFilter])

//   // Delete an investigation
//   const deleteInvestigation = (id: string) => {
//     if (!confirm("Are you sure you want to delete this investigation?")) return
    
//     const updated = investigations.filter((inv) => inv.id !== id)
//     setInvestigations(updated)
//     localStorage.setItem("osint_investigations", JSON.stringify(updated))
//   }

//   // Export investigation data
//   const exportInvestigation = (investigation: Investigation, format: "json" | "csv") => {
//     try {
//       let content: string
//       let filename: string
//       let mimeType: string

//       if (format === "json") {
//         content = JSON.stringify(investigation, null, 2)
//         filename = `${investigation.id}_report.json`
//         mimeType = "application/json"
//       } else {
//         // CSV format
//         const headers = ["Field", "Value"]
//         const rows = [
//           ["Investigation ID", investigation.id],
//           ["Target User", investigation.targetUser],
//           ["Platforms", investigation.platforms.join(", ")],
//           ["Status", investigation.status],
//           ["Created At", new Date(investigation.createdAt).toLocaleString()],
//           ["Completed At", investigation.completedAt ? new Date(investigation.completedAt).toLocaleString() : "N/A"],
//         ]
//         content = [headers, ...rows].map(row => row.map(cell => `"${cell}"`).join(",")).join("\n")
//         filename = `${investigation.id}_report.csv`
//         mimeType = "text/csv"
//       }

//       // Download file
//       const blob = new Blob([content], { type: mimeType })
//       const url = URL.createObjectURL(blob)
//       const a = document.createElement("a")
//       a.href = url
//       a.download = filename
//       document.body.appendChild(a)
//       a.click()
//       setTimeout(() => {
//         document.body.removeChild(a)
//         URL.revokeObjectURL(url)
//       }, 100)
//     } catch (err) {
//       console.error("Export failed:", err)
//       alert("Export failed. Please try again.")
//     }
//   }

//   // View detailed results
//   const viewResults = useCallback((investigation: Investigation) => {
//     const resultsWindow = window.open("", "_blank", "width=800,height=600")
//     if (resultsWindow) {
//       resultsWindow.document.write(`
//         <!DOCTYPE html>
//         <html>
//           <head>
//             <title>Investigation Results - ${investigation.id}</title>
//             <style>
//               body { 
//                 font-family: Arial, sans-serif; 
//                 margin: 20px; 
//                 background: #1a1a1a; 
//                 color: #fff; 
//                 line-height: 1.6;
//               }
//               .header { 
//                 border-bottom: 2px solid #333; 
//                 padding-bottom: 20px; 
//                 margin-bottom: 20px; 
//               }
//               .section { 
//                 margin: 20px 0; 
//                 padding: 15px; 
//                 background: #2a2a2a; 
//                 border-radius: 8px; 
//               }
//               pre { 
//                 background: #1a1a1a; 
//                 padding: 10px; 
//                 border-radius: 5px; 
//                 overflow-x: auto;
//                 white-space: pre-wrap;
//                 word-wrap: break-word;
//               }
//               .badge { 
//                 display: inline-block;
//                 background: #0066cc; 
//                 color: white; 
//                 padding: 2px 8px; 
//                 border-radius: 12px; 
//                 font-size: 12px; 
//               }
//             </style>
//           </head>
//           <body>
//             <div class="header">
//               <h1>🔍 Investigation Results</h1>
//               <p><strong>ID:</strong> ${investigation.id}</p>
//               <p><strong>Target:</strong> ${investigation.targetUser}</p>
//               <p><strong>Status:</strong> <span class="badge">${investigation.status}</span></p>
//               <p><strong>Created:</strong> ${new Date(investigation.createdAt).toLocaleString()}</p>
//               ${investigation.completedAt ? `<p><strong>Completed:</strong> ${new Date(investigation.completedAt).toLocaleString()}</p>` : ''}
//             </div>
            
//             <div class="section">
//               <h2>📊 Summary</h2>
//               <p><strong>Platforms:</strong> ${investigation.platforms.join(", ")}</p>
//               <p><strong>Total Platforms:</strong> ${investigation.platforms.length}</p>
//             </div>
            
//             <div class="section">
//               <h2>📋 Results</h2>
//               <pre>${JSON.stringify(investigation.results || {}, null, 2)}</pre>
//             </div>
//           </body>
//         </html>
//       `)
//       resultsWindow.document.close()
//     }
//   }, [])

//   useEffect(() => {
//     loadInvestigations()
//   }, [loadInvestigations])

//   useEffect(() => {
//     filterInvestigations()
//   }, [filterInvestigations])

//   return (
//     <div className="min-h-screen bg-black text-white relative">
//       <MatrixBackground />

//       <div className="container mx-auto px-4 py-8 relative z-10">
//         <header className="mb-8">
//           <h1 className="text-3xl font-bold text-blue-400 mb-2">Investigation Reports</h1>
//           <div className="flex flex-col md:flex-row gap-4">
//             <input
//               type="text"
//               placeholder="Search by ID or username..."
//               className="flex-1 p-2 bg-gray-800 border border-gray-700 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
//               value={searchTerm}
//               onChange={(e) => setSearchTerm(e.target.value)}
//               aria-label="Search investigations"
//             />
//             <select
//               className="w-full md:w-48 p-2 bg-gray-800 border border-gray-700 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
//               value={statusFilter}
//               onChange={(e) => setStatusFilter(e.target.value as StatusFilter)}
//               aria-label="Filter by status"
//             >
//               <option value="all">All Statuses</option>
//               <option value="pending">Pending</option>
//               <option value="in-progress">In Progress</option>
//               <option value="completed">Completed</option>
//               <option value="failed">Failed</option>
//             </select>
//           </div>
//         </header>

//         {error && (
//           <div className="bg-red-900/50 border border-red-700 text-red-200 p-4 rounded mb-6">
//             {error}
//           </div>
//         )}

//         {loading ? (
//           <div className="flex justify-center items-center h-64">
//             <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
//           </div>
//         ) : filteredInvestigations.length === 0 ? (
//           <div className="text-center py-12">
//             <h3 className="text-xl text-gray-400 mb-2">No investigations found</h3>
//             <p className="text-gray-500">
//               {searchTerm || statusFilter !== 'all' 
//                 ? "Try adjusting your search filters" 
//                 : "Create a new investigation to get started"}
//             </p>
//           </div>
//         ) : (
//           <div className="grid gap-4">
//             {filteredInvestigations.map((investigation) => (
//               <div 
//                 key={investigation.id} 
//                 className="bg-gray-900/70 border border-gray-800 rounded-lg p-4 hover:border-blue-500 transition-colors"
//               >
//                 <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
//                   <div>
//                     <h2 className="font-bold text-lg flex flex-wrap items-center gap-2">
//                       <span className="text-blue-400">#{investigation.id.slice(0, 8)}</span>
//                       <span>{investigation.targetUser}</span>
//                       <span className={`text-xs px-2 py-1 rounded-full ${
//                         investigation.status === 'completed' ? 'bg-green-900 text-green-300' :
//                         investigation.status === 'failed' ? 'bg-red-900 text-red-300' :
//                         'bg-yellow-900 text-yellow-300'
//                       }`}>
//                         {investigation.status.replace('-', ' ')}
//                       </span>
//                     </h2>
//                     <div className="flex flex-wrap gap-2 mt-2">
//                       {investigation.platforms.map(platform => (
//                         <span 
//                           key={platform} 
//                           className="text-xs bg-gray-800 px-2 py-1 rounded capitalize"
//                         >
//                           {platform}
//                         </span>
//                       ))}
//                     </div>
//                     <p className="text-sm text-gray-400 mt-2">
//                       Created: {new Date(investigation.createdAt).toLocaleString()}
//                     </p>
//                   </div>

//                   <div className="flex flex-wrap gap-2 justify-end">
//                     {investigation.status === 'completed' && (
//                       <>
//                         <button
//                           onClick={() => viewResults(investigation)}
//                           className="px-3 py-1 bg-blue-600 hover:bg-blue-700 rounded text-sm transition-colors"
//                           aria-label="View results"
//                         >
//                           View Results
//                         </button>
//                         <div className="relative group">
//                           <button 
//                             className="px-3 py-1 bg-gray-700 hover:bg-gray-600 rounded text-sm transition-colors"
//                             aria-label="Export options"
//                           >
//                             Export
//                           </button>
//                           <div className="absolute right-0 mt-1 hidden group-hover:block bg-gray-800 rounded shadow-lg z-10 w-40">
//                             <button 
//                               onClick={() => exportInvestigation(investigation, 'json')}
//                               className="block w-full text-left px-4 py-2 hover:bg-gray-700 text-sm"
//                             >
//                               Export as JSON
//                             </button>
//                             <button 
//                               onClick={() => exportInvestigation(investigation, 'csv')}
//                               className="block w-full text-left px-4 py-2 hover:bg-gray-700 text-sm"
//                             >
//                               Export as CSV
//                             </button>
//                           </div>
//                         </div>
//                       </>
//                     )}
//                     <button
//                       onClick={() => deleteInvestigation(investigation.id)}
//                       className="px-3 py-1 bg-red-600 hover:bg-red-700 rounded text-sm transition-colors"
//                       aria-label="Delete investigation"
//                     >
//                       Delete
//                     </button>
//                   </div>
//                 </div>
//               </div>
//             ))}
//           </div>
//         )}
//       </div>
//     </div>
//   )
// }


// !above best woeking 

"use client"

import { useState, useEffect } from "react"
import { MatrixBackground } from "@/components/matrix-background"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Search, Download, Eye, Trash2, Filter, User, Globe } from "lucide-react"

interface Investigation {
  id: string
  targetUser: string
  platforms: string[]
  status: string
  createdAt: string
  completedAt?: string
  results?: any
  aiAnalysis?: any
}

export default function ReportsPage() {
  const [investigations, setInvestigations] = useState<Investigation[]>([])
  const [filteredInvestigations, setFilteredInvestigations] = useState<Investigation[]>([])
  const [searchTerm, setSearchTerm] = useState("")
  const [statusFilter, setStatusFilter] = useState("all")
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadInvestigations()
  }, [])

  useEffect(() => {
    filterInvestigations()
  }, [investigations, searchTerm, statusFilter])

  const loadInvestigations = () => {
    try {
      const stored = localStorage.getItem("osint_investigations")
      if (stored) {
        const data = JSON.parse(stored)
        setInvestigations(data)
      }
    } catch (error) {
      console.error("Failed to load investigations:", error)
    } finally {
      setLoading(false)
    }
  }

  const filterInvestigations = () => {
    let filtered = investigations

    // Filter by search term
    if (searchTerm) {
      filtered = filtered.filter(
        (inv) =>
          inv.targetUser.toLowerCase().includes(searchTerm.toLowerCase()) ||
          inv.id.toLowerCase().includes(searchTerm.toLowerCase()),
      )
    }

    // Filter by status
    if (statusFilter !== "all") {
      filtered = filtered.filter((inv) => inv.status.toLowerCase() === statusFilter.toLowerCase())
    }

    setFilteredInvestigations(filtered)
  }

  const deleteInvestigation = (id: string) => {
    if (confirm("Are you sure you want to delete this investigation?")) {
      const updated = investigations.filter((inv) => inv.id !== id)
      setInvestigations(updated)
      localStorage.setItem("osint_investigations", JSON.stringify(updated))
    }
  }

  const exportInvestigation = (investigation: Investigation, format: string) => {
    try {
      let content = ""
      let filename = ""
      let mimeType = ""

      if (format === "json") {
        content = JSON.stringify(investigation, null, 2)
        filename = `${investigation.id}_report.json`
        mimeType = "application/json"
      } else if (format === "csv") {
        // Convert to CSV format
        const headers = ["Field", "Value"]
        const rows = [
          ["Investigation ID", investigation.id],
          ["Target User", investigation.targetUser],
          ["Platforms", investigation.platforms.join(", ")],
          ["Status", investigation.status],
          ["Created At", new Date(investigation.createdAt).toLocaleString()],
          ["Completed At", investigation.completedAt ? new Date(investigation.completedAt).toLocaleString() : "N/A"],
        ]

        // Add platform results
        if (investigation.results) {
          for (const [platform, data] of Object.entries(investigation.results)) {
            if (platform !== "ai_analysis" && typeof data === "object" && data !== null) {
              const platformData = data as any
              if (platformData.posts) {
                rows.push([`${platform} Posts`, platformData.posts.length.toString()])
              }
              if (platformData.comments) {
                rows.push([`${platform} Comments`, platformData.comments.length.toString()])
              }
              if (platformData.tweets) {
                rows.push([`${platform} Tweets`, platformData.tweets.length.toString()])
              }
              if (platformData.repositories) {
                rows.push([`${platform} Repositories`, platformData.repositories.length.toString()])
              }
              if (platformData.commits) {
                rows.push([`${platform} Commits`, platformData.commits.length.toString()])
              }
            }
          }
        }

        content = [headers, ...rows].map((row) => row.map((cell) => `"${cell}"`).join(",")).join("\n")
        filename = `${investigation.id}_report.csv`
        mimeType = "text/csv"
      }

      // Create and download file
      const blob = new Blob([content], { type: mimeType })
      const url = URL.createObjectURL(blob)
      const a = document.createElement("a")
      a.href = url
      a.download = filename
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)
    } catch (error) {
      console.error("Export failed:", error)
      alert("Export failed. Please try again.")
    }
  }

  const viewResults = (investigation: Investigation) => {
    // Create a detailed view of results
    const resultsWindow = window.open("", "_blank", "width=1200,height=800")
    if (resultsWindow) {
      const aiAnalysis = investigation.results?.ai_analysis || {}
      const platformResults = { ...investigation.results }
      delete platformResults.ai_analysis

      resultsWindow.document.write(`
        <html>
          <head>
            <title>Investigation Results - ${investigation.id}</title>
            <style>
              body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0; 
                padding: 20px; 
                background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%); 
                color: #fff; 
                line-height: 1.6;
              }
              .container { max-width: 1200px; margin: 0 auto; }
              .header { 
                border-bottom: 3px solid #0066cc; 
                padding-bottom: 20px; 
                margin-bottom: 30px; 
                text-align: center;
              }
              .header h1 { 
                color: #0066cc; 
                margin: 0; 
                font-size: 2.5em; 
                text-shadow: 0 0 10px rgba(0, 102, 204, 0.3);
              }
              .section { 
                margin: 30px 0; 
                padding: 20px; 
                background: rgba(255, 255, 255, 0.05); 
                border-radius: 12px; 
                border: 1px solid rgba(0, 102, 204, 0.2);
                backdrop-filter: blur(10px);
              }
              .section h2 { 
                color: #00ccff; 
                border-bottom: 2px solid rgba(0, 204, 255, 0.3); 
                padding-bottom: 10px;
                margin-top: 0;
              }
              .section h3 { 
                color: #66d9ff; 
                margin-top: 25px;
              }
              .platform { 
                margin: 15px 0; 
                padding: 15px; 
                background: rgba(0, 102, 204, 0.1); 
                border-radius: 8px; 
                border-left: 4px solid #0066cc;
              }
              .platform h4 { 
                color: #0066cc; 
                margin: 0 0 10px 0; 
                text-transform: uppercase; 
                font-size: 1.1em;
              }
              pre { 
                background: #1a1a1a; 
                padding: 15px; 
                border-radius: 8px; 
                overflow-x: auto; 
                border: 1px solid #333;
                font-size: 0.9em;
              }
              .badge { 
                background: linear-gradient(45deg, #0066cc, #00ccff); 
                color: white; 
                padding: 4px 12px; 
                border-radius: 20px; 
                font-size: 0.85em; 
                font-weight: bold;
                display: inline-block;
                margin: 2px;
              }
              .stats { 
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                gap: 15px; 
                margin: 20px 0;
              }
              .stat-card { 
                background: rgba(0, 102, 204, 0.1); 
                padding: 15px; 
                border-radius: 8px; 
                text-align: center;
                border: 1px solid rgba(0, 102, 204, 0.2);
              }
              .stat-number { 
                font-size: 2em; 
                font-weight: bold; 
                color: #00ccff; 
              }
              .stat-label { 
                color: #ccc; 
                font-size: 0.9em; 
              }
              .content-item {
                background: rgba(255, 255, 255, 0.03);
                padding: 10px;
                margin: 8px 0;
                border-radius: 6px;
                border-left: 3px solid #0066cc;
              }
              .ai-result {
                background: linear-gradient(135deg, rgba(0, 102, 204, 0.1), rgba(0, 204, 255, 0.1));
                padding: 20px;
                border-radius: 10px;
                margin: 15px 0;
                border: 1px solid rgba(0, 204, 255, 0.2);
              }
              .print-btn {
                position: fixed;
                top: 20px;
                right: 20px;
                background: #0066cc;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
              }
              .print-btn:hover {
                background: #0052a3;
              }
              @media print {
                body { background: white; color: black; }
                .section { background: white; border: 1px solid #ccc; }
                .print-btn { display: none; }
              }
            </style>
          </head>
          <body>
            <div class="container">
              <button class="print-btn" onclick="window.print()">🖨️ Print Report</button>
              
              <div class="header">
                <h1>🔍 OSINT Investigation Report</h1>
                <p><strong>Investigation ID:</strong> ${investigation.id}</p>
                <p><strong>Target User:</strong> ${investigation.targetUser}</p>
                <p><strong>Status:</strong> <span class="badge">${investigation.status}</span></p>
                <p><strong>Created:</strong> ${new Date(investigation.createdAt).toLocaleString()}</p>
                ${investigation.completedAt ? `<p><strong>Completed:</strong> ${new Date(investigation.completedAt).toLocaleString()}</p>` : ""}
              </div>
              
              <div class="section">
                <h2>📊 Executive Summary</h2>
                <div class="stats">
                  <div class="stat-card">
                    <div class="stat-number">${investigation.platforms.length}</div>
                    <div class="stat-label">Platforms Analyzed</div>
                  </div>
                  <div class="stat-card">
                    <div class="stat-number">${Object.keys(platformResults).length}</div>
                    <div class="stat-label">Data Sources</div>
                  </div>
                  <div class="stat-card">
                    <div class="stat-number">${Object.keys(aiAnalysis).length}</div>
                    <div class="stat-label">AI Models Used</div>
                  </div>
                </div>
                <p><strong>Platforms:</strong> ${investigation.platforms.map((p) => `<span class="badge">${p}</span>`).join(" ")}</p>
              </div>
              
              <div class="section">
                <h2>🎯 Platform Results</h2>
                ${Object.entries(platformResults)
                  .map(([platform, data]) => {
                    if (typeof data === "object" && data !== null) {
                      const platformData = data as any
                      let content = `<div class="platform"><h4>${platform.toUpperCase()}</h4>`

                      if (platformData.error) {
                        content += `<p style="color: #ff6b6b;">❌ Error: ${platformData.error}</p>`
                      } else {
                        if (platformData.user_info) {
                          content += `<p><strong>User Info:</strong> ${JSON.stringify(platformData.user_info, null, 2)}</p>`
                        }

                        const counts = []
                        if (platformData.posts) counts.push(`${platformData.posts.length} posts`)
                        if (platformData.comments) counts.push(`${platformData.comments.length} comments`)
                        if (platformData.tweets) counts.push(`${platformData.tweets.length} tweets`)
                        if (platformData.repositories) counts.push(`${platformData.repositories.length} repositories`)
                        if (platformData.commits) counts.push(`${platformData.commits.length} commits`)

                        if (counts.length > 0) {
                          content += `<p><strong>Content Found:</strong> ${counts.join(", ")}</p>`
                        }

                        // Show sample content
                        if (platformData.posts && platformData.posts.length > 0) {
                          content += `<h5>Sample Posts:</h5>`
                          platformData.posts.slice(0, 3).forEach((post: any) => {
                            const text = post.content || post.caption || post.title || post.body || post.selftext || ""
                            if (text) {
                              content += `<div class="content-item">${text.substring(0, 200)}${text.length > 200 ? "..." : ""}</div>`
                            }
                          })
                        }

                        if (platformData.tweets && platformData.tweets.length > 0) {
                          content += `<h5>Sample Tweets:</h5>`
                          platformData.tweets.slice(0, 3).forEach((tweet: any) => {
                            if (tweet.content) {
                              content += `<div class="content-item">${tweet.content.substring(0, 200)}${tweet.content.length > 200 ? "..." : ""}</div>`
                            }
                          })
                        }
                      }

                      content += `</div>`
                      return content
                    }
                    return ""
                  })
                  .join("")}
              </div>
              
              <div class="section">
                <h2>🧠 AI Analysis Results</h2>
                ${Object.entries(aiAnalysis)
                  .map(([model, results]) => {
                    if (typeof results === "object" && results !== null) {
                      const analysisResults = results as any
                      return `
                      <div class="ai-result">
                        <h3>${model.toUpperCase()} Analysis</h3>
                        ${
                          analysisResults.error
                            ? `<p style="color: #ff6b6b;">❌ Error: ${analysisResults.error}</p>`
                            : `<pre>${JSON.stringify(analysisResults, null, 2)}</pre>`
                        }
                      </div>
                    `
                    }
                    return ""
                  })
                  .join("")}
              </div>
              
              <div class="section">
                <h2>📋 Raw Data</h2>
                <details>
                  <summary style="cursor: pointer; color: #00ccff; font-weight: bold;">Click to view raw investigation data</summary>
                  <pre>${JSON.stringify(investigation, null, 2)}</pre>
                </details>
              </div>
              
              <div class="section" style="text-align: center; margin-top: 50px;">
                <p style="font-style: italic; color: #888;">
                  This report was generated by the AI-Based OSINT Platform for ethical research purposes.
                </p>
                <p style="font-size: 0.9em; color: #666;">
                  Generated on: ${new Date().toLocaleString()}
                </p>
              </div>
            </div>
          </body>
        </html>
      `)
      resultsWindow.document.close()
    }
  }

  const getStatusColor = (status: string) => {
    switch (status.toLowerCase()) {
      case "completed":
        return "bg-green-500"
      case "running":
        return "bg-blue-500"
      case "failed":
        return "bg-red-500"
      default:
        return "bg-gray-500"
    }
  }

  const getContentCount = (investigation: Investigation) => {
    if (!investigation.results) return 0

    let count = 0
    Object.entries(investigation.results).forEach(([platform, data]) => {
      if (platform !== "ai_analysis" && typeof data === "object" && data !== null) {
        const platformData = data as any
        if (platformData.posts) count += platformData.posts.length
        if (platformData.comments) count += platformData.comments.length
        if (platformData.tweets) count += platformData.tweets.length
        if (platformData.repositories) count += platformData.repositories.length
        if (platformData.commits) count += platformData.commits.length
      }
    })

    return count
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-black text-white relative flex items-center justify-center">
        <MatrixBackground />
        <div className="relative z-10 text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-500 mx-auto mb-4"></div>
          <p className="text-xl">Loading investigations...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-black text-white relative">
      <MatrixBackground />

      {/* Header */}
      <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
                📊 Investigation Reports
              </h1>
              <p className="text-gray-400 mt-2">View and manage your OSINT investigation results</p>
            </div>
            <Button onClick={loadInvestigations} className="bg-blue-600 hover:bg-blue-700">
              🔄 Refresh
            </Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="relative z-10 container mx-auto px-4 py-8">
        {/* Search and Filters */}
        <div className="mb-8 space-y-4">
          <div className="flex flex-col md:flex-row gap-4">
            <div className="flex-1 relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
              <Input
                placeholder="Search by username or investigation ID..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-10 bg-gray-900/50 border-gray-700 text-white"
              />
            </div>
            <div className="flex gap-2">
              <select
                value={statusFilter}
                onChange={(e) => setStatusFilter(e.target.value)}
                className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
              >
                <option value="all">All Status</option>
                <option value="completed">Completed</option>
                <option value="running">Running</option>
                <option value="failed">Failed</option>
              </select>
            </div>
          </div>
        </div>

        {/* Statistics */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-blue-500/20 rounded-lg">
                  <Globe className="h-6 w-6 text-blue-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">Total Investigations</p>
                  <p className="text-2xl font-bold text-white">{investigations.length}</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-green-500/20 rounded-lg">
                  <Eye className="h-6 w-6 text-green-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">Completed</p>
                  <p className="text-2xl font-bold text-white">
                    {investigations.filter((inv) => inv.status === "completed").length}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-yellow-500/20 rounded-lg">
                  <Filter className="h-6 w-6 text-yellow-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">Running</p>
                  <p className="text-2xl font-bold text-white">
                    {investigations.filter((inv) => inv.status === "running").length}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-red-500/20 rounded-lg">
                  <User className="h-6 w-6 text-red-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">Failed</p>
                  <p className="text-2xl font-bold text-white">
                    {investigations.filter((inv) => inv.status === "failed").length}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Investigations List */}
        {filteredInvestigations.length === 0 ? (
          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-12 text-center">
              <div className="text-6xl mb-4">🔍</div>
              <h3 className="text-xl font-semibold mb-2">No Investigations Found</h3>
              <p className="text-gray-400 mb-6">
                {investigations.length === 0
                  ? "You haven't run any investigations yet. Start by analyzing a target user."
                  : "No investigations match your current filters. Try adjusting your search criteria."}
              </p>
              <Button onClick={() => (window.location.href = "/analyze")} className="bg-blue-600 hover:bg-blue-700">
                🚀 Start New Investigation
              </Button>
            </CardContent>
          </Card>
        ) : (
          <div className="space-y-6">
            {filteredInvestigations.map((investigation) => (
              <Card
                key={investigation.id}
                className="bg-gray-900/50 border-gray-700 hover:border-blue-500/50 transition-colors"
              >
                <CardHeader>
                  <div className="flex items-start justify-between">
                    <div>
                      <CardTitle className="text-xl text-white flex items-center gap-2">
                        <User className="h-5 w-5 text-blue-400" />
                        {investigation.targetUser}
                      </CardTitle>
                      <CardDescription className="text-gray-400 mt-1">ID: {investigation.id}</CardDescription>
                    </div>
                    <Badge className={`${getStatusColor(investigation.status)} text-white`}>
                      {investigation.status}
                    </Badge>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                    <div>
                      <p className="text-sm text-gray-400">Platforms</p>
                      <div className="flex flex-wrap gap-1 mt-1">
                        {investigation.platforms.map((platform) => (
                          <Badge key={platform} variant="outline" className="text-xs">
                            {platform}
                          </Badge>
                        ))}
                      </div>
                    </div>
                    <div>
                      <p className="text-sm text-gray-400">Content Found</p>
                      <p className="text-lg font-semibold text-white">{getContentCount(investigation)}</p>
                    </div>
                    <div>
                      <p className="text-sm text-gray-400">Created</p>
                      <p className="text-sm text-white">{new Date(investigation.createdAt).toLocaleString()}</p>
                    </div>
                    <div>
                      <p className="text-sm text-gray-400">Completed</p>
                      <p className="text-sm text-white">
                        {investigation.completedAt ? new Date(investigation.completedAt).toLocaleString() : "N/A"}
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-wrap gap-2">
                    <Button
                      onClick={() => viewResults(investigation)}
                      size="sm"
                      className="bg-blue-600 hover:bg-blue-700"
                    >
                      <Eye className="h-4 w-4 mr-2" />
                      View Results
                    </Button>
                    <Button
                      onClick={() => exportInvestigation(investigation, "json")}
                      size="sm"
                      variant="outline"
                      className="border-gray-600 text-gray-300 hover:bg-gray-800"
                    >
                      <Download className="h-4 w-4 mr-2" />
                      Export JSON
                    </Button>
                    <Button
                      onClick={() => exportInvestigation(investigation, "csv")}
                      size="sm"
                      variant="outline"
                      className="border-gray-600 text-gray-300 hover:bg-gray-800"
                    >
                      <Download className="h-4 w-4 mr-2" />
                      Export CSV
                    </Button>
                    <Button
                      onClick={() => deleteInvestigation(investigation.id)}
                      size="sm"
                      variant="destructive"
                      className="bg-red-600 hover:bg-red-700"
                    >
                      <Trash2 className="h-4 w-4 mr-2" />
                      Delete
                    </Button>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}
