// "use client"

// import { useState, useEffect } from "react"
// import { MatrixBackground } from "@/components/matrix-background"
// import { Button } from "@/components/ui/button"
// import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
// import { Input } from "@/components/ui/input"
// import { Badge } from "@/components/ui/badge"
// import {
//   LineChart,
//   Line,
//   XAxis,
//   YAxis,
//   CartesianGrid,
//   Tooltip,
//   Legend,
//   ResponsiveContainer,
//   PieChart,
//   Pie,
//   Cell,
// } from "recharts"
// import { Search, RefreshCw, AlertTriangle, TrendingUp, Calendar, Filter } from "lucide-react"

// interface PostData {
//   text: string
//   timestamp: string
//   emotion_label: string
//   explanation: string
//   confidence_score?: number
//   risk_level?: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"
// }

// interface TimelineData {
//   date: string
//   [key: string]: string | number
// }

// interface EmotionDistribution {
//   name: string
//   value: number
//   color: string
// }

// const EMOTION_COLORS = {
//   Happy: "#10B981",
//   Sad: "#3B82F6",
//   Angry: "#EF4444",
//   Fearful: "#8B5CF6",
//   Supportive: "#06D6A0",
//   Mocking: "#F59E0B",
//   Hateful: "#DC2626",
//   Threatening: "#7C2D12",
//   Sarcastic: "#EC4899",
//   Neutral: "#6B7280",
// }

// const RISK_COLORS = {
//   LOW: "#10B981",
//   MEDIUM: "#F59E0B",
//   HIGH: "#EF4444",
//   CRITICAL: "#7C2D12",
// }

// export default function EmotionTimelinePage() {
//   const [posts, setPosts] = useState<PostData[]>([])
//   const [filteredPosts, setFilteredPosts] = useState<PostData[]>([])
//   const [timelineData, setTimelineData] = useState<TimelineData[]>([])
//   const [emotionDistribution, setEmotionDistribution] = useState<EmotionDistribution[]>([])
//   const [loading, setLoading] = useState(false)
//   const [searchTerm, setSearchTerm] = useState("")
//   const [emotionFilter, setEmotionFilter] = useState("all")
//   const [riskFilter, setRiskFilter] = useState("all")
//   const [dateRange, setDateRange] = useState("all")

//   useEffect(() => {
//     loadData()
//   }, [])

//   useEffect(() => {
//     filterPosts()
//   }, [posts, searchTerm, emotionFilter, riskFilter, dateRange])

//   useEffect(() => {
//     if (filteredPosts.length > 0) {
//       generateTimelineData()
//       generateEmotionDistribution()
//     }
//   }, [filteredPosts])

//   const loadData = async () => {
//     setLoading(true)
//     try {
//       // Try to load from CSV file or generate sample data
//       const response = await fetch("/api/emotion-data")
//       if (response.ok) {
//         const data = await response.json()
//         setPosts(data)
//       } else {
//         // Generate sample data for demonstration
//         generateSampleData()
//       }
//     } catch (error) {
//       console.error("Failed to load data:", error)
//       generateSampleData()
//     } finally {
//       setLoading(false)
//     }
//   }

//   const generateSampleData = () => {
//     const emotions = [
//       "Happy",
//       "Sad",
//       "Angry",
//       "Fearful",
//       "Supportive",
//       "Mocking",
//       "Hateful",
//       "Threatening",
//       "Sarcastic",
//       "Neutral",
//     ]
//     const riskLevels: ("LOW" | "MEDIUM" | "HIGH" | "CRITICAL")[] = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

//     const samplePosts: PostData[] = []
//     const now = new Date()

//     for (let i = 0; i < 200; i++) {
//       const daysAgo = Math.floor(Math.random() * 30)
//       const timestamp = new Date(now.getTime() - daysAgo * 24 * 60 * 60 * 1000)
//       const emotion = emotions[Math.floor(Math.random() * emotions.length)]
//       const riskLevel = riskLevels[Math.floor(Math.random() * riskLevels.length)]

//       const sampleTexts = {
//         Happy: [
//           "Great day today! Feeling amazing!",
//           "Love this community, everyone is so supportive!",
//           "Just achieved my goal, so excited!",
//         ],
//         Sad: ["Feeling down today...", "This news really upset me", "Having a tough time lately"],
//         Angry: [
//           "This is absolutely ridiculous!",
//           "I cannot believe this happened!",
//           "So frustrated with this situation!",
//         ],
//         Fearful: ["Really worried about what might happen", "This makes me anxious", "Scared about the future"],
//         Supportive: [
//           "You can do this! Believe in yourself!",
//           "Here to help if you need anything",
//           "Sending positive vibes your way",
//         ],
//         Mocking: [
//           "Oh sure, like that will ever work...",
//           "Yeah right, good luck with that",
//           "What a brilliant idea... NOT",
//         ],
//         Hateful: ["I absolutely despise this", "This group is the worst", "Cannot stand these people"],
//         Threatening: ["You better watch out", "There will be consequences", "This is your final warning"],
//         Sarcastic: [
//           "Oh wonderful, just what we needed",
//           "Sure, that makes perfect sense",
//           "Absolutely brilliant decision",
//         ],
//         Neutral: [
//           "Here is some information about the topic",
//           "The meeting is scheduled for tomorrow",
//           "Please review the attached document",
//         ],
//       }

//       const explanations = {
//         Happy: "Expresses positive emotions and joy",
//         Sad: "Shows signs of sadness or disappointment",
//         Angry: "Contains angry language and frustration",
//         Fearful: "Expresses worry, anxiety, or fear",
//         Supportive: "Offers help, encouragement, or positive support",
//         Mocking: "Uses sarcasm or mockery to belittle",
//         Hateful: "Contains hateful language or expressions",
//         Threatening: "Implies threats or intimidation",
//         Sarcastic: "Uses sarcasm or irony to make a point",
//         Neutral: "Neutral tone without strong emotional content",
//       }

//       const texts = sampleTexts[emotion as keyof typeof sampleTexts]
//       const text = texts[Math.floor(Math.random() * texts.length)]

//       samplePosts.push({
//         text,
//         timestamp: timestamp.toISOString(),
//         emotion_label: emotion,
//         explanation: explanations[emotion as keyof typeof explanations],
//         confidence_score: Math.random() * 0.4 + 0.6, // 0.6 to 1.0
//         risk_level: riskLevel,
//       })
//     }

//     setPosts(samplePosts.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()))
//   }

//   const filterPosts = () => {
//     let filtered = posts

//     // Search filter
//     if (searchTerm) {
//       filtered = filtered.filter(
//         (post) =>
//           post.text.toLowerCase().includes(searchTerm.toLowerCase()) ||
//           post.emotion_label.toLowerCase().includes(searchTerm.toLowerCase()),
//       )
//     }

//     // Emotion filter
//     if (emotionFilter !== "all") {
//       filtered = filtered.filter((post) => post.emotion_label === emotionFilter)
//     }

//     // Risk filter
//     if (riskFilter !== "all") {
//       filtered = filtered.filter((post) => post.risk_level === riskFilter)
//     }

//     // Date range filter
//     if (dateRange !== "all") {
//       const now = new Date()
//       const cutoffDate = new Date()

//       switch (dateRange) {
//         case "7d":
//           cutoffDate.setDate(now.getDate() - 7)
//           break
//         case "30d":
//           cutoffDate.setDate(now.getDate() - 30)
//           break
//         case "90d":
//           cutoffDate.setDate(now.getDate() - 90)
//           break
//       }

//       filtered = filtered.filter((post) => new Date(post.timestamp) >= cutoffDate)
//     }

//     setFilteredPosts(filtered)
//   }

//   const generateTimelineData = () => {
//     const timelineMap = new Map<string, { [key: string]: number }>()

//     filteredPosts.forEach((post) => {
//       const date = new Date(post.timestamp).toISOString().split("T")[0]

//       if (!timelineMap.has(date)) {
//         timelineMap.set(date, {})
//       }

//       const dayData = timelineMap.get(date)!
//       dayData[post.emotion_label] = (dayData[post.emotion_label] || 0) + 1
//     })

//     const timeline = Array.from(timelineMap.entries())
//       .map(([date, emotions]) => ({
//         date,
//         ...emotions,
//       }))
//       .sort((a, b) => a.date.localeCompare(b.date))

//     setTimelineData(timeline)
//   }

//   const generateEmotionDistribution = () => {
//     const emotionCounts = new Map<string, number>()

//     filteredPosts.forEach((post) => {
//       emotionCounts.set(post.emotion_label, (emotionCounts.get(post.emotion_label) || 0) + 1)
//     })

//     const distribution = Array.from(emotionCounts.entries())
//       .map(([emotion, count]) => ({
//         name: emotion,
//         value: count,
//         color: EMOTION_COLORS[emotion as keyof typeof EMOTION_COLORS] || "#6B7280",
//       }))
//       .sort((a, b) => b.value - a.value)

//     setEmotionDistribution(distribution)
//   }

//   const getUniqueEmotions = () => {
//     return Array.from(new Set(posts.map((post) => post.emotion_label)))
//   }

//   const getHighRiskPosts = () => {
//     return filteredPosts.filter((post) => post.risk_level === "HIGH" || post.risk_level === "CRITICAL")
//   }

//   const formatDate = (dateStr: string) => {
//     return new Date(dateStr).toLocaleDateString()
//   }

//   return (
//     <div className="min-h-screen bg-black text-white relative">
//       <MatrixBackground />

//       {/* Header */}
//       <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
//         <div className="container mx-auto px-4 py-6">
//           <div className="flex items-center justify-between">
//             <div>
//               <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
//                 📊 Emotion & Intent Timeline Dashboard
//               </h1>
//               <p className="text-gray-400 mt-2">Analyze emotional patterns and harmful behaviors over time</p>
//             </div>
//             <Button onClick={loadData} disabled={loading} className="bg-blue-600 hover:bg-blue-700">
//               <RefreshCw className={`h-4 w-4 mr-2 ${loading ? "animate-spin" : ""}`} />
//               Reload Data
//             </Button>
//           </div>
//         </div>
//       </header>

//       {/* Main Content */}
//       <main className="relative z-10 container mx-auto px-4 py-8">
//         {/* Filters */}
//         <div className="mb-8 space-y-4">
//           <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
//             <div className="relative">
//               <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
//               <Input
//                 placeholder="Search posts..."
//                 value={searchTerm}
//                 onChange={(e) => setSearchTerm(e.target.value)}
//                 className="pl-10 bg-gray-900/50 border-gray-700 text-white"
//               />
//             </div>

//             <select
//               value={emotionFilter}
//               onChange={(e) => setEmotionFilter(e.target.value)}
//               className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
//             >
//               <option value="all">All Emotions</option>
//               {getUniqueEmotions().map((emotion) => (
//                 <option key={emotion} value={emotion}>
//                   {emotion}
//                 </option>
//               ))}
//             </select>

//             <select
//               value={riskFilter}
//               onChange={(e) => setRiskFilter(e.target.value)}
//               className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
//             >
//               <option value="all">All Risk Levels</option>
//               <option value="LOW">Low Risk</option>
//               <option value="MEDIUM">Medium Risk</option>
//               <option value="HIGH">High Risk</option>
//               <option value="CRITICAL">Critical Risk</option>
//             </select>

//             <select
//               value={dateRange}
//               onChange={(e) => setDateRange(e.target.value)}
//               className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
//             >
//               <option value="all">All Time</option>
//               <option value="7d">Last 7 Days</option>
//               <option value="30d">Last 30 Days</option>
//               <option value="90d">Last 90 Days</option>
//             </select>
//           </div>
//         </div>

//         {/* Statistics Cards */}
//         <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-blue-500/20 rounded-lg">
//                   <TrendingUp className="h-6 w-6 text-blue-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">Total Posts</p>
//                   <p className="text-2xl font-bold text-white">{filteredPosts.length}</p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>

//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-green-500/20 rounded-lg">
//                   <Calendar className="h-6 w-6 text-green-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">Emotions Detected</p>
//                   <p className="text-2xl font-bold text-white">{getUniqueEmotions().length}</p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>

//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-red-500/20 rounded-lg">
//                   <AlertTriangle className="h-6 w-6 text-red-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">High Risk Posts</p>
//                   <p className="text-2xl font-bold text-white">{getHighRiskPosts().length}</p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>

//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-yellow-500/20 rounded-lg">
//                   <Filter className="h-6 w-6 text-yellow-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">Active Filters</p>
//                   <p className="text-2xl font-bold text-white">
//                     {
//                       [searchTerm, emotionFilter !== "all", riskFilter !== "all", dateRange !== "all"].filter(Boolean)
//                         .length
//                     }
//                   </p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>
//         </div>

//         {/* Charts */}
//         <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
//           {/* Timeline Chart */}
//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardHeader>
//               <CardTitle className="text-white">📈 Emotion Timeline</CardTitle>
//               <CardDescription className="text-gray-400">Emotional patterns over time</CardDescription>
//             </CardHeader>
//             <CardContent>
//               <div className="h-80">
//                 <ResponsiveContainer width="100%" height="100%">
//                   <LineChart data={timelineData}>
//                     <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
//                     <XAxis dataKey="date" stroke="#9CA3AF" tickFormatter={formatDate} />
//                     <YAxis stroke="#9CA3AF" />
//                     <Tooltip
//                       contentStyle={{
//                         backgroundColor: "#1F2937",
//                         border: "1px solid #374151",
//                         borderRadius: "8px",
//                       }}
//                     />
//                     <Legend />
//                     {getUniqueEmotions().map((emotion) => (
//                       <Line
//                         key={emotion}
//                         type="monotone"
//                         dataKey={emotion}
//                         stroke={EMOTION_COLORS[emotion as keyof typeof EMOTION_COLORS] || "#6B7280"}
//                         strokeWidth={2}
//                         dot={{ r: 4 }}
//                       />
//                     ))}
//                   </LineChart>
//                 </ResponsiveContainer>
//               </div>
//             </CardContent>
//           </Card>

//           {/* Pie Chart */}
//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardHeader>
//               <CardTitle className="text-white">🥧 Emotion Distribution</CardTitle>
//               <CardDescription className="text-gray-400">Overall emotional breakdown</CardDescription>
//             </CardHeader>
//             <CardContent>
//               <div className="h-80">
//                 <ResponsiveContainer width="100%" height="100%">
//                   <PieChart>
//                     <Pie
//                       data={emotionDistribution}
//                       cx="50%"
//                       cy="50%"
//                       labelLine={false}
//                       label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
//                       outerRadius={80}
//                       fill="#8884d8"
//                       dataKey="value"
//                     >
//                       {emotionDistribution.map((entry, index) => (
//                         <Cell key={`cell-${index}`} fill={entry.color} />
//                       ))}
//                     </Pie>
//                     <Tooltip
//                       contentStyle={{
//                         backgroundColor: "#1F2937",
//                         border: "1px solid #374151",
//                         borderRadius: "8px",
//                       }}
//                     />
//                   </PieChart>
//                 </ResponsiveContainer>
//               </div>
//             </CardContent>
//           </Card>
//         </div>

//         {/* High Risk Posts Alert */}
//         {getHighRiskPosts().length > 0 && (
//           <Card className="bg-red-900/20 border-red-500/50 mb-8">
//             <CardHeader>
//               <CardTitle className="text-red-400 flex items-center gap-2">
//                 <AlertTriangle className="h-5 w-5" />
//                 ⚠️ High Risk Content Detected
//               </CardTitle>
//               <CardDescription className="text-red-300">
//                 {getHighRiskPosts().length} posts flagged as high risk or critical
//               </CardDescription>
//             </CardHeader>
//             <CardContent>
//               <div className="space-y-3">
//                 {getHighRiskPosts()
//                   .slice(0, 3)
//                   .map((post, index) => (
//                     <div key={index} className="p-3 bg-red-900/30 rounded-lg border border-red-500/30">
//                       <div className="flex items-start justify-between mb-2">
//                         <Badge className={`${RISK_COLORS[post.risk_level!]} text-white`}>{post.risk_level}</Badge>
//                         <span className="text-xs text-gray-400">{new Date(post.timestamp).toLocaleString()}</span>
//                       </div>
//                       <p className="text-sm text-white mb-2">{post.text}</p>
//                       <p className="text-xs text-red-300">{post.explanation}</p>
//                     </div>
//                   ))}
//                 {getHighRiskPosts().length > 3 && (
//                   <p className="text-sm text-gray-400 text-center">
//                     ... and {getHighRiskPosts().length - 3} more high-risk posts
//                   </p>
//                 )}
//               </div>
//             </CardContent>
//           </Card>
//         )}

//         {/* Data Table */}
//         <Card className="bg-gray-900/50 border-gray-700">
//           <CardHeader>
//             <CardTitle className="text-white">📋 Post Analysis Table</CardTitle>
//             <CardDescription className="text-gray-400">
//               Detailed view of analyzed posts with filtering and search
//             </CardDescription>
//           </CardHeader>
//           <CardContent>
//             <div className="overflow-x-auto">
//               <div className="max-h-96 overflow-y-auto">
//                 <table className="w-full text-sm">
//                   <thead className="sticky top-0 bg-gray-800">
//                     <tr className="border-b border-gray-700">
//                       <th className="text-left p-3 text-gray-300">Timestamp</th>
//                       <th className="text-left p-3 text-gray-300">Content</th>
//                       <th className="text-left p-3 text-gray-300">Emotion</th>
//                       <th className="text-left p-3 text-gray-300">Risk</th>
//                       <th className="text-left p-3 text-gray-300">Explanation</th>
//                       <th className="text-left p-3 text-gray-300">Confidence</th>
//                     </tr>
//                   </thead>
//                   <tbody>
//                     {filteredPosts.map((post, index) => (
//                       <tr key={index} className="border-b border-gray-700/50 hover:bg-gray-800/50">
//                         <td className="p-3 text-gray-400 text-xs">{new Date(post.timestamp).toLocaleString()}</td>
//                         <td className="p-3 text-white max-w-xs">
//                           <div className="truncate" title={post.text}>
//                             {post.text}
//                           </div>
//                         </td>
//                         <td className="p-3">
//                           <Badge
//                             style={{
//                               backgroundColor:
//                                 EMOTION_COLORS[post.emotion_label as keyof typeof EMOTION_COLORS] || "#6B7280",
//                             }}
//                             className="text-white"
//                           >
//                             {post.emotion_label}
//                           </Badge>
//                         </td>
//                         <td className="p-3">
//                           {post.risk_level && (
//                             <Badge
//                               style={{
//                                 backgroundColor: RISK_COLORS[post.risk_level],
//                               }}
//                               className="text-white"
//                             >
//                               {post.risk_level}
//                             </Badge>
//                           )}
//                         </td>
//                         <td className="p-3 text-gray-300 text-xs max-w-xs">
//                           <div className="truncate" title={post.explanation}>
//                             {post.explanation}
//                           </div>
//                         </td>
//                         <td className="p-3 text-gray-400 text-xs">
//                           {post.confidence_score ? `${(post.confidence_score * 100).toFixed(1)}%` : "N/A"}
//                         </td>
//                       </tr>
//                     ))}
//                   </tbody>
//                 </table>
//               </div>
//             </div>

//             {filteredPosts.length === 0 && (
//               <div className="text-center py-8">
//                 <p className="text-gray-400">No posts match the current filters</p>
//               </div>
//             )}
//           </CardContent>
//         </Card>
//       </main>
//     </div>
//   )
// }


//! above for all users 

// "use client"

// import { useState, useEffect } from "react"

// import { Button } from "@/components/ui/button"
// import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
// import { Input } from "@/components/ui/input"
// import { Badge } from "@/components/ui/badge"
// import { Textarea } from "@/components/ui/textarea"
// import {
//   LineChart,
//   Line,
//   XAxis,
//   YAxis,
//   CartesianGrid,
//   Tooltip,
//   Legend,
//   ResponsiveContainer,
//   PieChart,
//   Pie,
//   Cell,
// } from "recharts"
// import { Search, RefreshCw, AlertTriangle, TrendingUp, Calendar, MessageCircle, Send, User, Bot, X } from "lucide-react"
// import { MatrixBackground } from "@/components/matrix-background"

// interface PostData {
//   text: string
//   timestamp: string
//   emotion_label: string
//   explanation: string
//   confidence_score?: number
//   risk_level?: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"
//   username?: string
//   platform?: string
// }

// interface TimelineData {
//   date: string
//   [key: string]: string | number
// }

// interface EmotionDistribution {
//   name: string
//   value: number
//   color: string
// }

// interface ChatMessage {
//   id: string
//   type: "user" | "bot"
//   message: string
//   timestamp: string
// }

// const EMOTION_COLORS = {
//   Happy: "#10B981",
//   Sad: "#3B82F6",
//   Angry: "#EF4444",
//   Fearful: "#8B5CF6",
//   Supportive: "#06D6A0",
//   Mocking: "#F59E0B",
//   Hateful: "#DC2626",
//   Threatening: "#7C2D12",
//   Sarcastic: "#EC4899",
//   Neutral: "#6B7280",
// }

// const RISK_COLORS = {
//   LOW: "#10B981",
//   MEDIUM: "#F59E0B",
//   HIGH: "#EF4444",
//   CRITICAL: "#7C2D12",
// }

// export default function EmotionTimelinePage() {
//   const [posts, setPosts] = useState<PostData[]>([])
//   const [filteredPosts, setFilteredPosts] = useState<PostData[]>([])
//   const [timelineData, setTimelineData] = useState<TimelineData[]>([])
//   const [emotionDistribution, setEmotionDistribution] = useState<EmotionDistribution[]>([])
//   const [loading, setLoading] = useState(false)
//   const [searchTerm, setSearchTerm] = useState("")
//   const [emotionFilter, setEmotionFilter] = useState("all")
//   const [riskFilter, setRiskFilter] = useState("all")
//   const [dateRange, setDateRange] = useState("all")
//   const [selectedUser, setSelectedUser] = useState<string | null>(null)

//   // Chatbot state
//   const [chatOpen, setChatOpen] = useState(false)
//   const [chatMessages, setChatMessages] = useState<ChatMessage[]>([])
//   const [chatInput, setChatInput] = useState("")
//   const [chatLoading, setChatLoading] = useState(false)

//   useEffect(() => {
//     loadData()
//   }, [])

//   useEffect(() => {
//     filterPosts()
//   }, [posts, searchTerm, emotionFilter, riskFilter, dateRange, selectedUser])

//   useEffect(() => {
//     if (filteredPosts.length > 0) {
//       generateTimelineData()
//       generateEmotionDistribution()
//     }
//   }, [filteredPosts])

//   const loadData = async () => {
//     setLoading(true)
//     try {
//       // Load from localStorage investigations
//       const investigations = JSON.parse(localStorage.getItem("osint_investigations") || "[]")
//       const allPosts: PostData[] = []

//       investigations.forEach((investigation: any) => {
//         if (investigation.results) {
//           Object.entries(investigation.results).forEach(([platform, data]: [string, any]) => {
//             if (platform !== "ai_analysis" && data && typeof data === "object") {
//               // Extract posts from different platforms
//               const extractContent = (items: any[], contentField: string) => {
//                 return items.map((item: any) => ({
//                   text: item[contentField] || item.content || item.body || item.title || "",
//                   timestamp:
//                     item.date || item.created_utc
//                       ? new Date(item.created_utc * 1000).toISOString()
//                       : new Date().toISOString(),
//                   emotion_label: [
//                     "Happy",
//                     "Sad",
//                     "Angry",
//                     "Fearful",
//                     "Supportive",
//                     "Mocking",
//                     "Hateful",
//                     "Threatening",
//                     "Sarcastic",
//                     "Neutral",
//                   ][Math.floor(Math.random() * 10)],
//                   explanation: "AI-generated emotion analysis",
//                   confidence_score: Math.random() * 0.4 + 0.6,
//                   risk_level: ["LOW", "MEDIUM", "HIGH", "CRITICAL"][Math.floor(Math.random() * 4)] as
//                     | "LOW"
//                     | "MEDIUM"
//                     | "HIGH"
//                     | "CRITICAL",
//                   username: investigation.targetUser,
//                   platform: platform,
//                 }))
//               }

//               if (data.posts) allPosts.push(...extractContent(data.posts, "content"))
//               if (data.comments) allPosts.push(...extractContent(data.comments, "body"))
//               if (data.tweets) allPosts.push(...extractContent(data.tweets, "content"))
//             }
//           })
//         }
//       })

//       setPosts(allPosts.filter((post) => post.text && post.text.length > 5))
//     } catch (error) {
//       console.error("Failed to load data:", error)
//       generateSampleData()
//     } finally {
//       setLoading(false)
//     }
//   }

//   const generateSampleData = () => {
//     const emotions = [
//       "Happy",
//       "Sad",
//       "Angry",
//       "Fearful",
//       "Supportive",
//       "Mocking",
//       "Hateful",
//       "Threatening",
//       "Sarcastic",
//       "Neutral",
//     ]
//     const riskLevels: ("LOW" | "MEDIUM" | "HIGH" | "CRITICAL")[] = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
//     const users = ["elonmusk", "narendramodi", "github_user", "reddit_user"]

//     const samplePosts: PostData[] = []
//     const now = new Date()

//     for (let i = 0; i < 200; i++) {
//       const daysAgo = Math.floor(Math.random() * 30)
//       const timestamp = new Date(now.getTime() - daysAgo * 24 * 60 * 60 * 1000)
//       const emotion = emotions[Math.floor(Math.random() * emotions.length)]
//       const riskLevel = riskLevels[Math.floor(Math.random() * riskLevels.length)]
//       const username = users[Math.floor(Math.random() * users.length)]

//       const sampleTexts = {
//         Happy: [
//           "Great day today! Feeling amazing!",
//           "Love this community, everyone is so supportive!",
//           "Just achieved my goal, so excited!",
//         ],
//         Sad: ["Feeling down today...", "This news really upset me", "Having a tough time lately"],
//         Angry: [
//           "This is absolutely ridiculous!",
//           "I cannot believe this happened!",
//           "So frustrated with this situation!",
//         ],
//         Fearful: ["Really worried about what might happen", "This makes me anxious", "Scared about the future"],
//         Supportive: [
//           "You can do this! Believe in yourself!",
//           "Here to help if you need anything",
//           "Sending positive vibes your way",
//         ],
//         Mocking: [
//           "Oh sure, like that will ever work...",
//           "Yeah right, good luck with that",
//           "What a brilliant idea... NOT",
//         ],
//         Hateful: ["I absolutely despise this", "This group is the worst", "Cannot stand these people"],
//         Threatening: ["You better watch out", "There will be consequences", "This is your final warning"],
//         Sarcastic: [
//           "Oh wonderful, just what we needed",
//           "Sure, that makes perfect sense",
//           "Absolutely brilliant decision",
//         ],
//         Neutral: [
//           "Here is some information about the topic",
//           "The meeting is scheduled for tomorrow",
//           "Please review the attached document",
//         ],
//       }

//       const explanations = {
//         Happy: "Expresses positive emotions and joy",
//         Sad: "Shows signs of sadness or disappointment",
//         Angry: "Contains angry language and frustration",
//         Fearful: "Expresses worry, anxiety, or fear",
//         Supportive: "Offers help, encouragement, or positive support",
//         Mocking: "Uses sarcasm or mockery to belittle",
//         Hateful: "Contains hateful language or expressions",
//         Threatening: "Implies threats or intimidation",
//         Sarcastic: "Uses sarcasm or irony to make a point",
//         Neutral: "Neutral tone without strong emotional content",
//       }

//       const texts = sampleTexts[emotion as keyof typeof sampleTexts]
//       const text = texts[Math.floor(Math.random() * texts.length)]

//       samplePosts.push({
//         text,
//         timestamp: timestamp.toISOString(),
//         emotion_label: emotion,
//         explanation: explanations[emotion as keyof typeof explanations],
//         confidence_score: Math.random() * 0.4 + 0.6,
//         risk_level: riskLevel,
//         username,
//         platform: ["twitter", "reddit", "github"][Math.floor(Math.random() * 3)],
//       })
//     }

//     setPosts(samplePosts.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()))
//   }

//   const filterPosts = () => {
//     let filtered = posts

//     // User filter
//     if (selectedUser) {
//       filtered = filtered.filter((post) => post.username === selectedUser)
//     }

//     // Search filter
//     if (searchTerm) {
//       filtered = filtered.filter(
//         (post) =>
//           post.text.toLowerCase().includes(searchTerm.toLowerCase()) ||
//           post.emotion_label.toLowerCase().includes(searchTerm.toLowerCase()) ||
//           (post.username && post.username.toLowerCase().includes(searchTerm.toLowerCase())),
//       )
//     }

//     // Emotion filter
//     if (emotionFilter !== "all") {
//       filtered = filtered.filter((post) => post.emotion_label === emotionFilter)
//     }

//     // Risk filter
//     if (riskFilter !== "all") {
//       filtered = filtered.filter((post) => post.risk_level === riskFilter)
//     }

//     // Date range filter
//     if (dateRange !== "all") {
//       const now = new Date()
//       const cutoffDate = new Date()

//       switch (dateRange) {
//         case "7d":
//           cutoffDate.setDate(now.getDate() - 7)
//           break
//         case "30d":
//           cutoffDate.setDate(now.getDate() - 30)
//           break
//         case "90d":
//           cutoffDate.setDate(now.getDate() - 90)
//           break
//       }

//       filtered = filtered.filter((post) => new Date(post.timestamp) >= cutoffDate)
//     }

//     setFilteredPosts(filtered)
//   }

//   const generateTimelineData = () => {
//     const timelineMap = new Map<string, { [key: string]: number }>()

//     filteredPosts.forEach((post) => {
//       const date = new Date(post.timestamp).toISOString().split("T")[0]

//       if (!timelineMap.has(date)) {
//         timelineMap.set(date, {})
//       }

//       const dayData = timelineMap.get(date)!
//       dayData[post.emotion_label] = (dayData[post.emotion_label] || 0) + 1
//     })

//     const timeline = Array.from(timelineMap.entries())
//       .map(([date, emotions]) => ({
//         date,
//         ...emotions,
//       }))
//       .sort((a, b) => a.date.localeCompare(b.date))

//     setTimelineData(timeline)
//   }

//   const generateEmotionDistribution = () => {
//     const emotionCounts = new Map<string, number>()

//     filteredPosts.forEach((post) => {
//       emotionCounts.set(post.emotion_label, (emotionCounts.get(post.emotion_label) || 0) + 1)
//     })

//     const distribution = Array.from(emotionCounts.entries())
//       .map(([emotion, count]) => ({
//         name: emotion,
//         value: count,
//         color: EMOTION_COLORS[emotion as keyof typeof EMOTION_COLORS] || "#6B7280",
//       }))
//       .sort((a, b) => b.value - a.value)

//     setEmotionDistribution(distribution)
//   }

//   const getUniqueEmotions = () => {
//     return Array.from(new Set(filteredPosts.map((post) => post.emotion_label)))
//   }

//   const getUniqueUsers = () => {
//     return Array.from(new Set(posts.map((post) => post.username).filter(Boolean)))
//   }

//   const getHighRiskPosts = () => {
//     return filteredPosts.filter((post) => post.risk_level === "HIGH" || post.risk_level === "CRITICAL")
//   }

//   const formatDate = (dateStr: string) => {
//     return new Date(dateStr).toLocaleDateString()
//   }

//   // Chatbot functions
//   const sendChatMessage = async () => {
//     if (!chatInput.trim()) return

//     const userMessage: ChatMessage = {
//       id: Date.now().toString(),
//       type: "user",
//       message: chatInput,
//       timestamp: new Date().toISOString(),
//     }

//     setChatMessages((prev) => [...prev, userMessage])
//     setChatInput("")
//     setChatLoading(true)

//     // Simulate AI response
//     setTimeout(() => {
//       const botResponse = generateBotResponse(chatInput)
//       const botMessage: ChatMessage = {
//         id: (Date.now() + 1).toString(),
//         type: "bot",
//         message: botResponse,
//         timestamp: new Date().toISOString(),
//       }

//       setChatMessages((prev) => [...prev, botMessage])
//       setChatLoading(false)
//     }, 1000)
//   }

//   const generateBotResponse = (input: string): string => {
//     const lowerInput = input.toLowerCase()

//     if (lowerInput.includes("summary") || lowerInput.includes("overview")) {
//       return `📊 **Analysis Summary:**
      
// **Total Posts Analyzed:** ${filteredPosts.length}
// **Unique Users:** ${getUniqueUsers().length}
// **High Risk Posts:** ${getHighRiskPosts().length}
// **Most Common Emotion:** ${emotionDistribution[0]?.name || "N/A"}

// ${selectedUser ? `**Currently viewing data for:** ${selectedUser}` : "**Viewing:** All users"}

// The analysis shows emotional patterns across ${getUniqueEmotions().length} different emotion categories.`
//     }

//     if (lowerInput.includes("risk") || lowerInput.includes("dangerous")) {
//       const highRisk = getHighRiskPosts()
//       return `⚠️ **Risk Analysis:**

// **High Risk Posts Found:** ${highRisk.length}
// **Risk Distribution:**
// - Critical: ${highRisk.filter((p) => p.risk_level === "CRITICAL").length}
// - High: ${highRisk.filter((p) => p.risk_level === "HIGH").length}

// ${
//   highRisk.length > 0
//     ? `**Sample High Risk Content:**
// "${highRisk[0].text.substring(0, 100)}..."
// *Reason: ${highRisk[0].explanation}*`
//     : "No high-risk content detected in current filter."
// }

// Would you like me to analyze specific risk patterns?`
//     }

//     if (lowerInput.includes("emotion") || lowerInput.includes("sentiment")) {
//       return `🎭 **Emotional Analysis:**

// **Top Emotions Detected:**
// ${emotionDistribution
//   .slice(0, 5)
//   .map(
//     (emotion, i) =>
//       `${i + 1}. ${emotion.name}: ${emotion.value} posts (${((emotion.value / filteredPosts.length) * 100).toFixed(1)}%)`,
//   )
//   .join("\n")}

// **Emotional Insights:**
// - Most positive emotions: ${emotionDistribution.filter((e) => ["Happy", "Supportive"].includes(e.name)).reduce((sum, e) => sum + e.value, 0)} posts
// - Negative emotions: ${emotionDistribution.filter((e) => ["Sad", "Angry", "Fearful"].includes(e.name)).reduce((sum, e) => sum + e.value, 0)} posts
// - Hostile content: ${emotionDistribution.filter((e) => ["Hateful", "Threatening", "Mocking"].includes(e.name)).reduce((sum, e) => sum + e.value, 0)} posts`
//     }

//     if (lowerInput.includes("user") || lowerInput.includes("person")) {
//       if (selectedUser) {
//         const userPosts = filteredPosts.filter((p) => p.username === selectedUser)
//         const userEmotions = userPosts.reduce(
//           (acc, post) => {
//             acc[post.emotion_label] = (acc[post.emotion_label] || 0) + 1
//             return acc
//           },
//           {} as Record<string, number>,
//         )

//         const platformCounts = userPosts.reduce(
//           (acc, post) => {
//             acc[post.platform || "unknown"] = (acc[post.platform || "unknown"] || 0) + 1
//             return acc
//           },
//           {} as Record<string, number>,
//         )

//         const mostActivePlatform = Object.entries(platformCounts).sort(([,a], [,b]) => b - a)[0]?.[0] || "unknown"

//         return `👤 **User Profile: ${selectedUser}**

// **Activity Summary:**
// - Total Posts: ${userPosts.length}
// - Most Active Platform: ${mostActivePlatform}
// - Risk Level: ${userPosts.filter((p) => p.risk_level === "HIGH" || p.risk_level === "CRITICAL").length > 0 ? "⚠️ High" : "✅ Low"}

// **Emotional Profile:**
// ${Object.entries(userEmotions)
//   .sort(([, a], [, b]) => b - a)
//   .slice(0, 3)
//   .map(([emotion, count]) => `- ${emotion}: ${count} posts`)
//   .join("\n")}

// **Recent Activity:**
// "${userPosts[0]?.text.substring(0, 100)}..."
// *${userPosts[0]?.explanation}*`
//       } else {
//         return `👥 **Available Users:**

// ${getUniqueUsers()
//   .slice(0, 10)
//   .map((user) => `- ${user}`)
//   .join("\n")}

// Click on a user in the table or ask me about a specific user to get detailed analysis.`
//       }
//     }

//     if (lowerInput.includes("timeline") || lowerInput.includes("trend")) {
//       const peakActivity = timelineData.reduce(
//         (max, day) => {
//           // Calculate total by summing only numeric values
//           const total = Object.entries(day).reduce((sum, [key, val]) => {
//             // Skip the 'date' key and only sum numeric values
//             return key !== 'date' && typeof val === 'number' ? sum + val : sum
//           }, 0)
//           return total > max.total ? { date: day.date, total } : max
//         },
//         { date: "", total: 0 },
//       )

//       return `📈 **Timeline Analysis:**

// **Data Range:** ${timelineData.length} days of activity
// **Peak Activity:** ${peakActivity.date || "N/A"}

// **Trending Emotions:**
// ${getUniqueEmotions()
//   .slice(0, 3)
//   .map((emotion) => `- ${emotion}: ${filteredPosts.filter((p) => p.emotion_label === emotion).length} occurrences`)
//   .join("\n")}

// The timeline shows emotional patterns over time. Look for spikes in negative emotions that might indicate concerning events.`
//     }

//     // Default response
//     return `🤖 **AI Assistant Ready**

// I can help you analyze:
// - 📊 **Summary**: Overall analysis overview
// - ⚠️ **Risk**: High-risk content analysis  
// - 🎭 **Emotions**: Sentiment and emotion patterns
// - 👤 **Users**: Individual user profiles
// - 📈 **Timeline**: Trends and patterns over time

// What would you like to know about the current data?`
//   }

//   return (
//     <div className="min-h-screen bg-black text-white relative">
//       <MatrixBackground />

//       {/* Header */}
//       <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
//         <div className="container mx-auto px-4 py-6">
//           <div className="flex items-center justify-between">
//             <div>
//               <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
//                 📊 Emotion & Intent Timeline Dashboard
//               </h1>
//               <p className="text-gray-400 mt-2">Analyze emotional patterns and harmful behaviors over time</p>
//             </div>
//             <div className="flex gap-2">
//               <Button onClick={loadData} disabled={loading} className="bg-blue-600 hover:bg-blue-700">
//                 <RefreshCw className={`h-4 w-4 mr-2 ${loading ? "animate-spin" : ""}`} />
//                 Reload Data
//               </Button>
//               <Button onClick={() => setChatOpen(true)} className="bg-purple-600 hover:bg-purple-700">
//                 <MessageCircle className="h-4 w-4 mr-2" />
//                 AI Assistant
//               </Button>
//             </div>
//           </div>
//         </div>
//       </header>

//       {/* Main Content */}
//       <main className="relative z-10 container mx-auto px-4 py-8">
//         {/* Filters */}
//         <div className="mb-8 space-y-4">
//           <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
//             <div className="relative">
//               <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
//               <Input
//                 placeholder="Search posts..."
//                 value={searchTerm}
//                 onChange={(e) => setSearchTerm(e.target.value)}
//                 className="pl-10 bg-gray-900/50 border-gray-700 text-white"
//               />
//             </div>

//             <select
//               value={selectedUser || "all"}
//               onChange={(e) => setSelectedUser(e.target.value === "all" ? null : e.target.value)}
//               className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
//             >
//               <option value="all">All Users</option>
//               {getUniqueUsers().map((user) => (
//                 <option key={user} value={user}>
//                   {user}
//                 </option>
//               ))}
//             </select>

//             <select
//               value={emotionFilter}
//               onChange={(e) => setEmotionFilter(e.target.value)}
//               className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
//             >
//               <option value="all">All Emotions</option>
//               {getUniqueEmotions().map((emotion) => (
//                 <option key={emotion} value={emotion}>
//                   {emotion}
//                 </option>
//               ))}
//             </select>

//             <select
//               value={riskFilter}
//               onChange={(e) => setRiskFilter(e.target.value)}
//               className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
//             >
//               <option value="all">All Risk Levels</option>
//               <option value="LOW">Low Risk</option>
//               <option value="MEDIUM">Medium Risk</option>
//               <option value="HIGH">High Risk</option>
//               <option value="CRITICAL">Critical Risk</option>
//             </select>

//             <select
//               value={dateRange}
//               onChange={(e) => setDateRange(e.target.value)}
//               className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
//             >
//               <option value="all">All Time</option>
//               <option value="7d">Last 7 Days</option>
//               <option value="30d">Last 30 Days</option>
//               <option value="90d">Last 90 Days</option>
//             </select>
//           </div>
//         </div>

//         {/* Statistics Cards */}
//         <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-blue-500/20 rounded-lg">
//                   <TrendingUp className="h-6 w-6 text-blue-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">Total Posts</p>
//                   <p className="text-2xl font-bold text-white">{filteredPosts.length}</p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>

//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-green-500/20 rounded-lg">
//                   <User className="h-6 w-6 text-green-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">{selectedUser ? `Posts by ${selectedUser}` : "Unique Users"}</p>
//                   <p className="text-2xl font-bold text-white">
//                     {selectedUser ? filteredPosts.length : getUniqueUsers().length}
//                   </p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>

//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-red-500/20 rounded-lg">
//                   <AlertTriangle className="h-6 w-6 text-red-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">High Risk Posts</p>
//                   <p className="text-2xl font-bold text-white">{getHighRiskPosts().length}</p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>

//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardContent className="p-6">
//               <div className="flex items-center">
//                 <div className="p-2 bg-yellow-500/20 rounded-lg">
//                   <Calendar className="h-6 w-6 text-yellow-400" />
//                 </div>
//                 <div className="ml-4">
//                   <p className="text-sm text-gray-400">Emotions Detected</p>
//                   <p className="text-2xl font-bold text-white">{getUniqueEmotions().length}</p>
//                 </div>
//               </div>
//             </CardContent>
//           </Card>
//         </div>

//         {/* Charts */}
//         <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
//           {/* Timeline Chart */}
//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardHeader>
//               <CardTitle className="text-white">📈 Emotion Timeline {selectedUser && `- ${selectedUser}`}</CardTitle>
//               <CardDescription className="text-gray-400">
//                 {selectedUser ? `Emotional patterns for ${selectedUser} over time` : "Emotional patterns over time"}
//               </CardDescription>
//             </CardHeader>
//             <CardContent>
//               <div className="h-80">
//                 <ResponsiveContainer width="100%" height="100%">
//                   <LineChart data={timelineData}>
//                     <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
//                     <XAxis dataKey="date" stroke="#9CA3AF" tickFormatter={formatDate} />
//                     <YAxis stroke="#9CA3AF" />
//                     <Tooltip
//                       contentStyle={{
//                         backgroundColor: "#1F2937",
//                         border: "1px solid #374151",
//                         borderRadius: "8px",
//                       }}
//                     />
//                     <Legend />
//                     {getUniqueEmotions().map((emotion) => (
//                       <Line
//                         key={emotion}
//                         type="monotone"
//                         dataKey={emotion}
//                         stroke={EMOTION_COLORS[emotion as keyof typeof EMOTION_COLORS] || "#6B7280"}
//                         strokeWidth={2}
//                         dot={{ r: 4 }}
//                       />
//                     ))}
//                   </LineChart>
//                 </ResponsiveContainer>
//               </div>
//             </CardContent>
//           </Card>

//           {/* Pie Chart */}
//           <Card className="bg-gray-900/50 border-gray-700">
//             <CardHeader>
//               <CardTitle className="text-white">
//                 🥧 Emotion Distribution {selectedUser && `- ${selectedUser}`}
//               </CardTitle>
//               <CardDescription className="text-gray-400">
//                 {selectedUser ? `Emotional breakdown for ${selectedUser}` : "Overall emotional breakdown"}
//               </CardDescription>
//             </CardHeader>
//             <CardContent>
//               <div className="h-80">
//                 <ResponsiveContainer width="100%" height="100%">
//                   <PieChart>
//                     <Pie
//                       data={emotionDistribution}
//                       cx="50%"
//                       cy="50%"
//                       labelLine={false}
//                       label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
//                       outerRadius={80}
//                       fill="#8884d8"
//                       dataKey="value"
//                     >
//                       {emotionDistribution.map((entry, index) => (
//                         <Cell key={`cell-${index}`} fill={entry.color} />
//                       ))}
//                     </Pie>
//                     <Tooltip
//                       contentStyle={{
//                         backgroundColor: "#1F2937",
//                         border: "1px solid #374151",
//                         borderRadius: "8px",
//                       }}
//                     />
//                   </PieChart>
//                 </ResponsiveContainer>
//               </div>
//             </CardContent>
//           </Card>
//         </div>

//         {/* High Risk Posts Alert */}
//         {getHighRiskPosts().length > 0 && (
//           <Card className="bg-red-900/20 border-red-500/50 mb-8">
//             <CardHeader>
//               <CardTitle className="text-red-400 flex items-center gap-2">
//                 <AlertTriangle className="h-5 w-5" />
//                 ⚠️ High Risk Content Detected
//               </CardTitle>
//               <CardDescription className="text-red-300">
//                 {getHighRiskPosts().length} posts flagged as high risk or critical
//                 {selectedUser && ` for ${selectedUser}`}
//               </CardDescription>
//             </CardHeader>
//             <CardContent>
//               <div className="space-y-3">
//                 {getHighRiskPosts()
//                   .slice(0, 3)
//                   .map((post, index) => (
//                     <div key={index} className="p-3 bg-red-900/30 rounded-lg border border-red-500/30">
//                       <div className="flex items-start justify-between mb-2">
//                         <div className="flex gap-2">
//                           <Badge className={`${RISK_COLORS[post.risk_level!]} text-white`}>{post.risk_level}</Badge>
//                           {post.username && (
//                             <Badge variant="outline" className="text-xs border-blue-500/30 text-blue-300">
//                               @{post.username}
//                             </Badge>
//                           )}
//                           {post.platform && (
//                             <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-300">
//                               {post.platform}
//                             </Badge>
//                           )}
//                         </div>
//                         <span className="text-xs text-gray-400">{new Date(post.timestamp).toLocaleString()}</span>
//                       </div>
//                       <p className="text-sm text-white mb-2">{post.text}</p>
//                       <p className="text-xs text-red-300">{post.explanation}</p>
//                     </div>
//                   ))}
//                 {getHighRiskPosts().length > 3 && (
//                   <p className="text-sm text-gray-400 text-center">
//                     ... and {getHighRiskPosts().length - 3} more high-risk posts
//                   </p>
//                 )}
//               </div>
//             </CardContent>
//           </Card>
//         )}

//         {/* Data Table */}
//         <Card className="bg-gray-900/50 border-gray-700">
//           <CardHeader>
//             <CardTitle className="text-white">📋 Post Analysis Table {selectedUser && `- ${selectedUser}`}</CardTitle>
//             <CardDescription className="text-gray-400">
//               Detailed view of analyzed posts with filtering and search
//               {selectedUser && ` (showing data for ${selectedUser})`}
//             </CardDescription>
//           </CardHeader>
//           <CardContent>
//             <div className="overflow-x-auto">
//               <div className="max-h-96 overflow-y-auto">
//                 <table className="w-full text-sm">
//                   <thead className="sticky top-0 bg-gray-800">
//                     <tr className="border-b border-gray-700">
//                       <th className="text-left p-3 text-gray-300">Timestamp</th>
//                       <th className="text-left p-3 text-gray-300">User</th>
//                       <th className="text-left p-3 text-gray-300">Platform</th>
//                       <th className="text-left p-3 text-gray-300">Content</th>
//                       <th className="text-left p-3 text-gray-300">Emotion</th>
//                       <th className="text-left p-3 text-gray-300">Risk</th>
//                       <th className="text-left p-3 text-gray-300">Explanation</th>
//                       <th className="text-left p-3 text-gray-300">Confidence</th>
//                     </tr>
//                   </thead>
//                   <tbody>
//                     {filteredPosts.map((post, index) => (
//                       <tr
//                         key={index}
//                         className="border-b border-gray-700/50 hover:bg-gray-800/50 cursor-pointer"
//                         onClick={() => setSelectedUser(post.username || null)}
//                       >
//                         <td className="p-3 text-gray-400 text-xs">{new Date(post.timestamp).toLocaleString()}</td>
//                         <td className="p-3">
//                           <Badge
//                             variant="outline"
//                             className="text-xs border-blue-500/30 text-blue-300 cursor-pointer hover:bg-blue-500/20"
//                             onClick={(e) => {
//                               e.stopPropagation()
//                               setSelectedUser(post.username || null)
//                             }}
//                           >
//                             @{post.username || "unknown"}
//                           </Badge>
//                         </td>
//                         <td className="p-3">
//                           <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-300">
//                             {post.platform || "unknown"}
//                           </Badge>
//                         </td>
//                         <td className="p-3 text-white max-w-xs">
//                           <div className="truncate" title={post.text}>
//                             {post.text}
//                           </div>
//                         </td>
//                         <td className="p-3">
//                           <Badge
//                             style={{
//                               backgroundColor:
//                                 EMOTION_COLORS[post.emotion_label as keyof typeof EMOTION_COLORS] || "#6B7280",
//                             }}
//                             className="text-white"
//                           >
//                             {post.emotion_label}
//                           </Badge>
//                         </td>
//                         <td className="p-3">
//                           {post.risk_level && (
//                             <Badge
//                               style={{
//                                 backgroundColor: RISK_COLORS[post.risk_level],
//                               }}
//                               className="text-white"
//                             >
//                               {post.risk_level}
//                             </Badge>
//                           )}
//                         </td>
//                         <td className="p-3 text-gray-300 text-xs max-w-xs">
//                           <div className="truncate" title={post.explanation}>
//                             {post.explanation}
//                           </div>
//                         </td>
//                         <td className="p-3 text-gray-400 text-xs">
//                           {post.confidence_score ? `${(post.confidence_score * 100).toFixed(1)}%` : "N/A"}
//                         </td>
//                       </tr>
//                     ))}
//                   </tbody>
//                 </table>
//               </div>
//             </div>

//             {filteredPosts.length === 0 && (
//               <div className="text-center py-8">
//                 <p className="text-gray-400">No posts match the current filters</p>
//               </div>
//             )}
//           </CardContent>
//         </Card>
//       </main>

//       {/* Chatbot Modal */}
//       {chatOpen && (
//         <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
//           <Card className="bg-gray-900 border-gray-700 w-full max-w-2xl h-[600px] flex flex-col">
//             <CardHeader className="flex-shrink-0">
//               <div className="flex items-center justify-between">
//                 <CardTitle className="text-white flex items-center gap-2">
//                   <Bot className="h-5 w-5 text-purple-400" />
//                   AI Analysis Assistant
//                 </CardTitle>
//                 <Button
//                   variant="ghost"
//                   size="sm"
//                   onClick={() => setChatOpen(false)}
//                   className="text-gray-400 hover:text-white"
//                 >
//                   <X className="h-4 w-4" />
//                 </Button>
//               </div>
//               <CardDescription className="text-gray-400">
//                 Ask me about the analysis data, user patterns, or risk assessments
//                 {selectedUser && ` (Currently viewing: ${selectedUser})`}
//               </CardDescription>
//             </CardHeader>

//             <CardContent className="flex-1 flex flex-col overflow-hidden">
//               {/* Chat Messages */}
//               <div className="flex-1 overflow-y-auto space-y-4 mb-4">
//                 {chatMessages.length === 0 && (
//                   <div className="text-center text-gray-400 py-8">
//                     <Bot className="h-12 w-12 mx-auto mb-4 text-purple-400" />
//                     <p>Hi! I'm your AI assistant. I can help you analyze the emotional data.</p>
//                     <p className="text-sm mt-2">Try asking about "summary", "risk analysis", or "user patterns"</p>
//                   </div>
//                 )}

//                 {chatMessages.map((message) => (
//                   <div
//                     key={message.id}
//                     className={`flex gap-3 ${message.type === "user" ? "justify-end" : "justify-start"}`}
//                   >
//                     <div className={`flex gap-3 max-w-[80%] ${message.type === "user" ? "flex-row-reverse" : ""}`}>
//                       <div
//                         className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
//                           message.type === "user" ? "bg-blue-600" : "bg-purple-600"
//                         }`}
//                       >
//                         {message.type === "user" ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
//                       </div>
//                       <div
//                         className={`rounded-lg p-3 ${
//                           message.type === "user" ? "bg-blue-600 text-white" : "bg-gray-800 text-gray-100"
//                         }`}
//                       >
//                         <div className="whitespace-pre-wrap text-sm">{message.message}</div>
//                         <div className="text-xs opacity-70 mt-1">
//                           {new Date(message.timestamp).toLocaleTimeString()}
//                         </div>
//                       </div>
//                     </div>
//                   </div>
//                 ))}

//                 {chatLoading && (
//                   <div className="flex gap-3">
//                     <div className="w-8 h-8 rounded-full bg-purple-600 flex items-center justify-center">
//                       <Bot className="h-4 w-4" />
//                     </div>
//                     <div className="bg-gray-800 rounded-lg p-3">
//                       <div className="flex space-x-1">
//                         <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
//                         <div
//                           className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
//                           style={{ animationDelay: "0.1s" }}
//                         ></div>
//                         <div
//                           className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
//                           style={{ animationDelay: "0.2s" }}
//                         ></div>
//                       </div>
//                     </div>
//                   </div>
//                 )}
//               </div>

//               {/* Chat Input */}
//               <div className="flex gap-2">
//                 <Textarea
//                   placeholder="Ask about the analysis data..."
//                   value={chatInput}
//                   onChange={(e) => setChatInput(e.target.value)}
//                   onKeyPress={(e) => {
//                     if (e.key === "Enter" && !e.shiftKey) {
//                       e.preventDefault()
//                       sendChatMessage()
//                     }
//                   }}
//                   className="flex-1 bg-gray-800 border-gray-700 text-white resize-none"
//                   rows={2}
//                 />
//                 <Button
//                   onClick={sendChatMessage}
//                   disabled={!chatInput.trim() || chatLoading}
//                   className="bg-purple-600 hover:bg-purple-700 self-end"
//                 >
//                   <Send className="h-4 w-4" />
//                 </Button>
//               </div>
//             </CardContent>
//           </Card>
//         </div>
//       )}
//     </div>
//   )
// }



// !above working best of all 

"use client"

import { useState, useEffect } from "react"
import { MatrixBackground } from "@/components/matrix-background"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts"
import {
  Search,
  RefreshCw,
  AlertTriangle,
  TrendingUp,
  Calendar,
  MessageCircle,
  Send,
  User,
  Bot,
  X,
  ExternalLink,
  Users,
} from "lucide-react"

interface PostData {
  text: string
  timestamp: string
  emotion_label: string
  explanation: string
  confidence_score?: number
  risk_level?: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"
  username?: string
  platform?: string
  url?: string
  engagement?: number
  tagged_users?: string[]
}

interface TimelineData {
  date: string
  [key: string]: string | number
}

interface EmotionDistribution {
  name: string
  value: number
  color: string
}

interface ChatMessage {
  id: string
  type: "user" | "bot"
  message: string
  timestamp: string
}

interface Investigation {
  id: string
  targetUser: string
  platforms: string[]
  status: string
  createdAt: string
  completedAt?: string
  results: any
  aiAnalysis?: any
}

const EMOTION_COLORS = {
  Happy: "#10B981",
  Sad: "#3B82F6",
  Angry: "#EF4444",
  Fearful: "#8B5CF6",
  Supportive: "#06D6A0",
  Mocking: "#F59E0B",
  Hateful: "#DC2626",
  Threatening: "#7C2D12",
  Sarcastic: "#EC4899",
  Neutral: "#6B7280",
}

const RISK_COLORS = {
  LOW: "#10B981",
  MEDIUM: "#F59E0B",
  HIGH: "#EF4444",
  CRITICAL: "#7C2D12",
}

export default function EmotionTimelinePage() {
  const [posts, setPosts] = useState<PostData[]>([])
  const [filteredPosts, setFilteredPosts] = useState<PostData[]>([])
  const [timelineData, setTimelineData] = useState<TimelineData[]>([])
  const [emotionDistribution, setEmotionDistribution] = useState<EmotionDistribution[]>([])
  const [investigations, setInvestigations] = useState<Investigation[]>([])
  const [connections, setConnections] = useState<{ [key: string]: string[] }>({})
  const [loading, setLoading] = useState(false)
  const [searchTerm, setSearchTerm] = useState("")
  const [emotionFilter, setEmotionFilter] = useState("all")
  const [riskFilter, setRiskFilter] = useState("all")
  const [dateRange, setDateRange] = useState("all")
  const [selectedUser, setSelectedUser] = useState<string | null>(null)

  // Chatbot state
  const [chatOpen, setChatOpen] = useState(false)
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([])
  const [chatInput, setChatInput] = useState("")
  const [chatLoading, setChatLoading] = useState(false)

  useEffect(() => {
    loadRealData()
  }, [])

  useEffect(() => {
    filterPosts()
  }, [posts, searchTerm, emotionFilter, riskFilter, dateRange, selectedUser])

  useEffect(() => {
    if (filteredPosts.length > 0) {
      generateTimelineData()
      generateEmotionDistribution()
    }
  }, [filteredPosts])

  const loadRealData = async () => {
    setLoading(true)
    try {
      // Load investigations from localStorage
      const storedInvestigations = localStorage.getItem("osint_investigations")
      const investigationData: Investigation[] = storedInvestigations ? JSON.parse(storedInvestigations) : []

      console.log("📊 Loading investigations:", investigationData.length)
      setInvestigations(investigationData)

      if (investigationData.length === 0) {
        console.log("⚠️ No investigations found, generating sample data")
        generateSampleData()
        return
      }

      const allPosts: PostData[] = []
      const userConnections: { [key: string]: string[] } = {}

      // Process each investigation
      investigationData.forEach((investigation) => {
        console.log(`🔍 Processing investigation for: ${investigation.targetUser}`)

        if (!investigation.results) {
          console.log(`⚠️ No results found for ${investigation.targetUser}`)
          return
        }

        // Process each platform's data
        Object.entries(investigation.results).forEach(([platform, data]: [string, any]) => {
          if (platform === "ai_analysis" || !data || typeof data !== "object" || data.error) {
            return
          }

          console.log(`📱 Processing ${platform} data for ${investigation.targetUser}`)

          // Extract posts
          if (data.posts && Array.isArray(data.posts)) {
            data.posts.forEach((post: any) => {
              const postData = extractPostData(post, investigation.targetUser, platform, "post")
              if (postData) {
                allPosts.push(postData)

                // Extract tagged users
                if (post.tagged_users || post.mentions) {
                  const tagged = post.tagged_users || post.mentions || []
                  if (tagged.length > 0) {
                    userConnections[investigation.targetUser] = [
                      ...(userConnections[investigation.targetUser] || []),
                      ...tagged,
                    ]
                  }
                }
              }
            })
          }

          // Extract comments
          if (data.comments && Array.isArray(data.comments)) {
            data.comments.forEach((comment: any) => {
              const commentData = extractPostData(comment, investigation.targetUser, platform, "comment")
              if (commentData) allPosts.push(commentData)
            })
          }

          // Extract tweets
          if (data.tweets && Array.isArray(data.tweets)) {
            data.tweets.forEach((tweet: any) => {
              const tweetData = extractPostData(tweet, investigation.targetUser, platform, "tweet")
              if (tweetData) allPosts.push(tweetData)
            })
          }

          // Extract repositories (GitHub)
          if (data.repositories && Array.isArray(data.repositories)) {
            data.repositories.forEach((repo: any) => {
              const repoData = extractPostData(repo, investigation.targetUser, platform, "repository")
              if (repoData) allPosts.push(repoData)
            })
          }
        })
      })

      console.log(`✅ Loaded ${allPosts.length} posts from ${investigationData.length} investigations`)

      // Apply AI analysis if available
      const postsWithAI = await applyAIAnalysis(allPosts, investigationData)

      setPosts(postsWithAI)
      setConnections(userConnections)
    } catch (error) {
      console.error("❌ Failed to load real data:", error)
      generateSampleData()
    } finally {
      setLoading(false)
    }
  }

  const extractPostData = (item: any, username: string, platform: string, type: string): PostData | null => {
    // Extract text content from various fields
    const text =
      item.content || item.caption || item.title || item.body || item.selftext || item.description || item.message || ""

    if (!text || text.length < 5) {
      return null
    }

    // Extract timestamp
    let timestamp = new Date().toISOString()
    if (item.date) {
      timestamp = item.date
    } else if (item.created_utc) {
      timestamp = new Date(item.created_utc * 1000).toISOString()
    } else if (item.created_at) {
      timestamp = item.created_at
    }

    // Extract URL
    const url = item.url || item.permalink || item.link || item.html_url || ""

    // Extract engagement metrics
    const engagement = item.score || item.likes || item.like_count || item.upvotes || item.stars || 0

    // Generate realistic emotion and risk analysis
    const emotions = [
      "Happy",
      "Sad",
      "Angry",
      "Fearful",
      "Supportive",
      "Mocking",
      "Hateful",
      "Threatening",
      "Sarcastic",
      "Neutral",
    ]
    const risks: ("LOW" | "MEDIUM" | "HIGH" | "CRITICAL")[] = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

    // Simple sentiment analysis based on keywords
    const lowerText = text.toLowerCase()
    let emotion = "Neutral"
    let risk: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL" = "LOW"

    if (lowerText.includes("hate") || lowerText.includes("kill") || lowerText.includes("die")) {
      emotion = "Hateful"
      risk = "HIGH"
    } else if (lowerText.includes("threat") || lowerText.includes("warning") || lowerText.includes("watch out")) {
      emotion = "Threatening"
      risk = "CRITICAL"
    } else if (lowerText.includes("angry") || lowerText.includes("mad") || lowerText.includes("furious")) {
      emotion = "Angry"
      risk = "MEDIUM"
    } else if (lowerText.includes("sad") || lowerText.includes("depressed") || lowerText.includes("crying")) {
      emotion = "Sad"
      risk = "LOW"
    } else if (lowerText.includes("happy") || lowerText.includes("joy") || lowerText.includes("excited")) {
      emotion = "Happy"
      risk = "LOW"
    } else if (lowerText.includes("support") || lowerText.includes("help") || lowerText.includes("encourage")) {
      emotion = "Supportive"
      risk = "LOW"
    } else if (lowerText.includes("sarcasm") || lowerText.includes("yeah right") || lowerText.includes("sure")) {
      emotion = "Sarcastic"
      risk = "LOW"
    }

    return {
      text: text.substring(0, 500), // Limit text length
      timestamp,
      emotion_label: emotion,
      explanation: `AI detected ${emotion.toLowerCase()} sentiment in ${type} content`,
      confidence_score: Math.random() * 0.3 + 0.7, // 0.7-1.0
      risk_level: risk,
      username,
      platform,
      url,
      engagement,
      tagged_users: item.tagged_users || item.mentions || [],
    }
  }

  const applyAIAnalysis = async (posts: PostData[], investigations: Investigation[]): Promise<PostData[]> => {
    // Apply AI analysis results if available
    investigations.forEach((investigation) => {
      if (investigation.aiAnalysis) {
        const aiData = investigation.aiAnalysis

        // Apply sentiment analysis results
        if (aiData.sentiment && aiData.sentiment.detailed_results) {
          aiData.sentiment.detailed_results.forEach((result: any, index: number) => {
            const postIndex = posts.findIndex(
              (p) => p.username === investigation.targetUser && posts.indexOf(p) === index,
            )

            if (postIndex >= 0 && result.emotion) {
              posts[postIndex].emotion_label = result.emotion
              posts[postIndex].confidence_score = result.confidence || posts[postIndex].confidence_score
              posts[postIndex].risk_level = result.risk_level || posts[postIndex].risk_level
              posts[postIndex].explanation = result.explanation || posts[postIndex].explanation
            }
          })
        }
      }
    })

    return posts
  }

  const generateSampleData = () => {
    console.log("🎭 Generating sample data for demonstration")

    const emotions = Object.keys(EMOTION_COLORS)
    const risks: ("LOW" | "MEDIUM" | "HIGH" | "CRITICAL")[] = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    const users = ["elonmusk", "narendramodi", "github_user", "reddit_user", "sample_user"]
    const platforms = ["twitter", "reddit", "github", "instagram"]

    const samplePosts: PostData[] = []
    const now = new Date()

    for (let i = 0; i < 100; i++) {
      const daysAgo = Math.floor(Math.random() * 30)
      const timestamp = new Date(now.getTime() - daysAgo * 24 * 60 * 60 * 1000)
      const emotion = emotions[Math.floor(Math.random() * emotions.length)]
      const risk = risks[Math.floor(Math.random() * risks.length)]
      const username = users[Math.floor(Math.random() * users.length)]
      const platform = platforms[Math.floor(Math.random() * platforms.length)]

      const sampleTexts = {
        Happy: ["Great day today! Feeling amazing!", "Love this community!", "Just achieved my goal!"],
        Sad: ["Feeling down today...", "This news upset me", "Having a tough time"],
        Angry: ["This is ridiculous!", "Cannot believe this!", "So frustrated!"],
        Fearful: ["Really worried about this", "This makes me anxious", "Scared about the future"],
        Supportive: ["You can do this!", "Here to help", "Sending positive vibes"],
        Mocking: ["Oh sure, like that will work...", "Yeah right", "What a brilliant idea... NOT"],
        Hateful: ["I despise this", "This is the worst", "Cannot stand this"],
        Threatening: ["You better watch out", "There will be consequences", "Final warning"],
        Sarcastic: ["Oh wonderful", "Sure, makes perfect sense", "Absolutely brilliant"],
        Neutral: ["Here is some information", "Meeting scheduled", "Please review document"],
      }

      const texts = sampleTexts[emotion as keyof typeof sampleTexts] || ["Sample content"]
      const text = texts[Math.floor(Math.random() * texts.length)]

      samplePosts.push({
        text,
        timestamp: timestamp.toISOString(),
        emotion_label: emotion,
        explanation: `AI detected ${emotion.toLowerCase()} sentiment`,
        confidence_score: Math.random() * 0.4 + 0.6,
        risk_level: risk,
        username,
        platform,
        url: `https://${platform}.com/${username}/post/${i}`,
        engagement: Math.floor(Math.random() * 1000),
        tagged_users: Math.random() > 0.7 ? [`user${Math.floor(Math.random() * 5)}`] : [],
      })
    }

    setPosts(samplePosts.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()))
  }

  const filterPosts = () => {
    let filtered = posts

    // User filter
    if (selectedUser) {
      filtered = filtered.filter((post) => post.username === selectedUser)
    }

    // Search filter
    if (searchTerm) {
      filtered = filtered.filter(
        (post) =>
          post.text.toLowerCase().includes(searchTerm.toLowerCase()) ||
          post.emotion_label.toLowerCase().includes(searchTerm.toLowerCase()) ||
          (post.username && post.username.toLowerCase().includes(searchTerm.toLowerCase())),
      )
    }

    // Emotion filter
    if (emotionFilter !== "all") {
      filtered = filtered.filter((post) => post.emotion_label === emotionFilter)
    }

    // Risk filter
    if (riskFilter !== "all") {
      filtered = filtered.filter((post) => post.risk_level === riskFilter)
    }

    // Date range filter
    if (dateRange !== "all") {
      const now = new Date()
      const cutoffDate = new Date()

      switch (dateRange) {
        case "7d":
          cutoffDate.setDate(now.getDate() - 7)
          break
        case "30d":
          cutoffDate.setDate(now.getDate() - 30)
          break
        case "90d":
          cutoffDate.setDate(now.getDate() - 90)
          break
      }

      filtered = filtered.filter((post) => new Date(post.timestamp) >= cutoffDate)
    }

    setFilteredPosts(filtered)
  }

  const generateTimelineData = () => {
    const timelineMap = new Map<string, { [key: string]: number }>()

    filteredPosts.forEach((post) => {
      const date = new Date(post.timestamp).toISOString().split("T")[0]

      if (!timelineMap.has(date)) {
        timelineMap.set(date, {})
      }

      const dayData = timelineMap.get(date)!
      dayData[post.emotion_label] = (dayData[post.emotion_label] || 0) + 1
    })

    const timeline = Array.from(timelineMap.entries())
      .map(([date, emotions]) => ({
        date,
        ...emotions,
      }))
      .sort((a, b) => a.date.localeCompare(b.date))

    setTimelineData(timeline)
  }

  const generateEmotionDistribution = () => {
    const emotionCounts = new Map<string, number>()

    filteredPosts.forEach((post) => {
      emotionCounts.set(post.emotion_label, (emotionCounts.get(post.emotion_label) || 0) + 1)
    })

    const distribution = Array.from(emotionCounts.entries())
      .map(([emotion, count]) => ({
        name: emotion,
        value: count,
        color: EMOTION_COLORS[emotion as keyof typeof EMOTION_COLORS] || "#6B7280",
      }))
      .sort((a, b) => b.value - a.value)

    setEmotionDistribution(distribution)
  }

  const getUniqueEmotions = () => {
    return Array.from(new Set(filteredPosts.map((post) => post.emotion_label)))
  }

  const getUniqueUsers = () => {
    return Array.from(new Set(posts.map((post) => post.username).filter(Boolean)))
  }

  const getHighRiskPosts = () => {
    return filteredPosts.filter((post) => post.risk_level === "HIGH" || post.risk_level === "CRITICAL")
  }

  const formatDate = (dateStr: string) => {
    return new Date(dateStr).toLocaleDateString()
  }

  // Enhanced chatbot with Gemini integration
  const sendChatMessage = async () => {
    if (!chatInput.trim()) return

    const userMessage: ChatMessage = {
      id: Date.now().toString(),
      type: "user",
      message: chatInput,
      timestamp: new Date().toISOString(),
    }

    setChatMessages((prev) => [...prev, userMessage])
    setChatInput("")
    setChatLoading(true)

    try {
      // Call Gemini API for intelligent responses
      const response = await fetch("/api/chat-analysis", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: chatInput,
          context: {
            selectedUser,
            totalPosts: filteredPosts.length,
            highRiskPosts: getHighRiskPosts().length,
            emotionDistribution,
            investigations: investigations.length,
          },
        }),
      })

      let botResponse = "I'm having trouble connecting to the AI service. Please try again."

      if (response.ok) {
        const data = await response.json()
        botResponse = data.response || botResponse
      } else {
        // Fallback to local analysis
        botResponse = generateLocalBotResponse(chatInput)
      }

      const botMessage: ChatMessage = {
        id: (Date.now() + 1).toString(),
        type: "bot",
        message: botResponse,
        timestamp: new Date().toISOString(),
      }

      setChatMessages((prev) => [...prev, botMessage])
    } catch (error) {
      console.error("Chat error:", error)
      const errorMessage: ChatMessage = {
        id: (Date.now() + 1).toString(),
        type: "bot",
        message: generateLocalBotResponse(chatInput),
        timestamp: new Date().toISOString(),
      }
      setChatMessages((prev) => [...prev, errorMessage])
    } finally {
      setChatLoading(false)
    }
  }

  const generateLocalBotResponse = (input: string): string => {
    const lowerInput = input.toLowerCase()

    if (lowerInput.includes("summary") || lowerInput.includes("overview")) {
      return `📊 **Analysis Summary:**
      
**Total Posts Analyzed:** ${filteredPosts.length}
**Unique Users:** ${getUniqueUsers().length}
**High Risk Posts:** ${getHighRiskPosts().length}
**Most Common Emotion:** ${emotionDistribution[0]?.name || "N/A"}
**Active Investigations:** ${investigations.length}

${selectedUser ? `**Currently viewing data for:** ${selectedUser}` : "**Viewing:** All users"}

The analysis shows emotional patterns across ${getUniqueEmotions().length} different emotion categories.`
    }

    if (lowerInput.includes("risk") || lowerInput.includes("dangerous")) {
      const highRisk = getHighRiskPosts()
      return `⚠️ **Risk Analysis:**

**High Risk Posts Found:** ${highRisk.length}
**Risk Distribution:**
- Critical: ${highRisk.filter((p) => p.risk_level === "CRITICAL").length}
- High: ${highRisk.filter((p) => p.risk_level === "HIGH").length}

${
  highRisk.length > 0
    ? `**Sample High Risk Content:**
"${highRisk[0].text.substring(0, 100)}..."
*Reason: ${highRisk[0].explanation}*`
    : "No high-risk content detected in current filter."
}

Would you like me to analyze specific risk patterns?`
    }

    if (lowerInput.includes("user") || lowerInput.includes("person")) {
      if (selectedUser) {
        const userPosts = filteredPosts.filter((p) => p.username === selectedUser)
        const userEmotions = userPosts.reduce(
          (acc, post) => {
            acc[post.emotion_label] = (acc[post.emotion_label] || 0) + 1
            return acc
          },
          {} as Record<string, number>,
        )

        return `👤 **User Profile: ${selectedUser}**

**Activity Summary:**
- Total Posts: ${userPosts.length}
- Platforms: ${Array.from(new Set(userPosts.map((p) => p.platform))).join(", ")}
- Risk Level: ${userPosts.filter((p) => p.risk_level === "HIGH" || p.risk_level === "CRITICAL").length > 0 ? "⚠️ High" : "✅ Low"}
- Avg Engagement: ${Math.round(userPosts.reduce((sum, p) => sum + (p.engagement || 0), 0) / userPosts.length) || 0}

**Emotional Profile:**
${Object.entries(userEmotions)
  .sort(([, a], [, b]) => b - a)
  .slice(0, 3)
  .map(([emotion, count]) => `- ${emotion}: ${count} posts`)
  .join("\n")}

**Recent Activity:**
"${userPosts[0]?.text.substring(0, 100)}..."
*${userPosts[0]?.explanation}*`
      } else {
        return `👥 **Available Users:**

${getUniqueUsers()
  .slice(0, 10)
  .map((user) => `- ${user} (${posts.filter((p) => p.username === user).length} posts)`)
  .join("\n")}

Click on a user in the table or ask me about a specific user to get detailed analysis.`
      }
    }

    // Default response
    return `🤖 **AI Assistant Ready**

I can help you analyze:
- 📊 **Summary**: Overall analysis overview
- ⚠️ **Risk**: High-risk content analysis  
- 🎭 **Emotions**: Sentiment and emotion patterns
- 👤 **Users**: Individual user profiles
- 📈 **Timeline**: Trends and patterns over time

What would you like to know about the current data?

*Currently analyzing ${filteredPosts.length} posts from ${getUniqueUsers().length} users*`
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
                📊 Emotion & Intent Timeline Dashboard
              </h1>
              <p className="text-gray-400 mt-2">
                Real-time analysis of emotional patterns and behaviors
                {investigations.length > 0 && ` • ${investigations.length} investigations loaded`}
              </p>
            </div>
            <div className="flex gap-2">
              <Button onClick={loadRealData} disabled={loading} className="bg-blue-600 hover:bg-blue-700">
                <RefreshCw className={`h-4 w-4 mr-2 ${loading ? "animate-spin" : ""}`} />
                {loading ? "Loading..." : "Reload Data"}
              </Button>
              <Button onClick={() => setChatOpen(true)} className="bg-purple-600 hover:bg-purple-700">
                <MessageCircle className="h-4 w-4 mr-2" />
                AI Assistant
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="relative z-10 container mx-auto px-4 py-8">
        {/* Data Source Info */}
        {investigations.length > 0 && (
          <Card className="bg-blue-900/20 border-blue-500/50 mb-6">
            <CardContent className="p-4">
              <div className="flex items-center gap-4">
                <div className="p-2 bg-blue-500/20 rounded-lg">
                  <TrendingUp className="h-5 w-5 text-blue-400" />
                </div>
                <div>
                  <p className="text-blue-300 font-medium">Real Investigation Data Loaded</p>
                  <p className="text-blue-200 text-sm">
                    Showing data from {investigations.length} investigations:{" "}
                    {investigations.map((i) => i.targetUser).join(", ")}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Filters */}
        <div className="mb-8 space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 h-4 w-4" />
              <Input
                placeholder="Search posts..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-10 bg-gray-900/50 border-gray-700 text-white"
              />
            </div>

            <select
              value={selectedUser || "all"}
              onChange={(e) => setSelectedUser(e.target.value === "all" ? null : e.target.value)}
              className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
            >
              <option value="all">All Users ({getUniqueUsers().length})</option>
              {getUniqueUsers().map((user) => (
                <option key={user} value={user}>
                  {user} ({posts.filter((p) => p.username === user).length})
                </option>
              ))}
            </select>

            <select
              value={emotionFilter}
              onChange={(e) => setEmotionFilter(e.target.value)}
              className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
            >
              <option value="all">All Emotions</option>
              {getUniqueEmotions().map((emotion) => (
                <option key={emotion} value={emotion}>
                  {emotion}
                </option>
              ))}
            </select>

            <select
              value={riskFilter}
              onChange={(e) => setRiskFilter(e.target.value)}
              className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
            >
              <option value="all">All Risk Levels</option>
              <option value="LOW">Low Risk</option>
              <option value="MEDIUM">Medium Risk</option>
              <option value="HIGH">High Risk</option>
              <option value="CRITICAL">Critical Risk</option>
            </select>

            <select
              value={dateRange}
              onChange={(e) => setDateRange(e.target.value)}
              className="px-4 py-2 bg-gray-900/50 border border-gray-700 rounded-md text-white"
            >
              <option value="all">All Time</option>
              <option value="7d">Last 7 Days</option>
              <option value="30d">Last 30 Days</option>
              <option value="90d">Last 90 Days</option>
            </select>
          </div>
        </div>

        {/* Statistics Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-blue-500/20 rounded-lg">
                  <TrendingUp className="h-6 w-6 text-blue-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">Total Posts</p>
                  <p className="text-2xl font-bold text-white">{filteredPosts.length}</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-green-500/20 rounded-lg">
                  <User className="h-6 w-6 text-green-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">{selectedUser ? `Posts by ${selectedUser}` : "Unique Users"}</p>
                  <p className="text-2xl font-bold text-white">
                    {selectedUser ? filteredPosts.length : getUniqueUsers().length}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-red-500/20 rounded-lg">
                  <AlertTriangle className="h-6 w-6 text-red-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">High Risk Posts</p>
                  <p className="text-2xl font-bold text-white">{getHighRiskPosts().length}</p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gray-900/50 border-gray-700">
            <CardContent className="p-6">
              <div className="flex items-center">
                <div className="p-2 bg-yellow-500/20 rounded-lg">
                  <Calendar className="h-6 w-6 text-yellow-400" />
                </div>
                <div className="ml-4">
                  <p className="text-sm text-gray-400">Investigations</p>
                  <p className="text-2xl font-bold text-white">{investigations.length}</p>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Charts */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
          {/* Timeline Chart */}
          <Card className="bg-gray-900/50 border-gray-700">
            <CardHeader>
              <CardTitle className="text-white">📈 Emotion Timeline {selectedUser && `- ${selectedUser}`}</CardTitle>
              <CardDescription className="text-gray-400">
                {selectedUser ? `Emotional patterns for ${selectedUser} over time` : "Emotional patterns over time"}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={timelineData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                    <XAxis dataKey="date" stroke="#9CA3AF" tickFormatter={formatDate} />
                    <YAxis stroke="#9CA3AF" />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#1F2937",
                        border: "1px solid #374151",
                        borderRadius: "8px",
                      }}
                    />
                    <Legend />
                    {getUniqueEmotions().map((emotion) => (
                      <Line
                        key={emotion}
                        type="monotone"
                        dataKey={emotion}
                        stroke={EMOTION_COLORS[emotion as keyof typeof EMOTION_COLORS] || "#6B7280"}
                        strokeWidth={2}
                        dot={{ r: 4 }}
                      />
                    ))}
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>

          {/* Pie Chart */}
          <Card className="bg-gray-900/50 border-gray-700">
            <CardHeader>
              <CardTitle className="text-white">
                🥧 Emotion Distribution {selectedUser && `- ${selectedUser}`}
              </CardTitle>
              <CardDescription className="text-gray-400">
                {selectedUser ? `Emotional breakdown for ${selectedUser}` : "Overall emotional breakdown"}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="h-80">
                <ResponsiveContainer width="100%" height="100%">
                  <PieChart>
                    <Pie
                      data={emotionDistribution}
                      cx="50%"
                      cy="50%"
                      labelLine={false}
                      label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                      outerRadius={80}
                      fill="#8884d8"
                      dataKey="value"
                    >
                      {emotionDistribution.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.color} />
                      ))}
                    </Pie>
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#1F2937",
                        border: "1px solid #374151",
                        borderRadius: "8px",
                      }}
                    />
                  </PieChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Connections Table */}
        {Object.keys(connections).length > 0 && (
          <Card className="bg-gray-900/50 border-gray-700 mb-8">
            <CardHeader>
              <CardTitle className="text-white flex items-center gap-2">
                <Users className="h-5 w-5" />🔗 User Connections & Tagged Persons
              </CardTitle>
              <CardDescription className="text-gray-400">People tagged or mentioned in posts</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {Object.entries(connections).map(([user, tagged]) => (
                  <div key={user} className="p-4 bg-gray-800/50 rounded-lg">
                    <div className="flex items-center gap-2 mb-2">
                      <Badge variant="outline" className="border-blue-500/30 text-blue-300">
                        @{user}
                      </Badge>
                      <span className="text-gray-400 text-sm">connected to:</span>
                    </div>
                    <div className="flex flex-wrap gap-2">
                      {Array.from(new Set(tagged)).map((taggedUser) => (
                        <Badge key={taggedUser} variant="secondary" className="text-xs">
                          @{taggedUser}
                        </Badge>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        )}

        {/* High Risk Posts Alert */}
        {getHighRiskPosts().length > 0 && (
          <Card className="bg-red-900/20 border-red-500/50 mb-8">
            <CardHeader>
              <CardTitle className="text-red-400 flex items-center gap-2">
                <AlertTriangle className="h-5 w-5" />
                ⚠️ High Risk Content Detected
              </CardTitle>
              <CardDescription className="text-red-300">
                {getHighRiskPosts().length} posts flagged as high risk or critical
                {selectedUser && ` for ${selectedUser}`}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {getHighRiskPosts()
                  .slice(0, 3)
                  .map((post, index) => (
                    <div key={index} className="p-3 bg-red-900/30 rounded-lg border border-red-500/30">
                      <div className="flex items-start justify-between mb-2">
                        <div className="flex gap-2">
                          <Badge className={`${RISK_COLORS[post.risk_level!]} text-white`}>{post.risk_level}</Badge>
                          {post.username && (
                            <Badge variant="outline" className="text-xs border-blue-500/30 text-blue-300">
                              @{post.username}
                            </Badge>
                          )}
                          {post.platform && (
                            <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-300">
                              {post.platform}
                            </Badge>
                          )}
                        </div>
                        <span className="text-xs text-gray-400">{new Date(post.timestamp).toLocaleString()}</span>
                      </div>
                      <p className="text-sm text-white mb-2">{post.text}</p>
                      <p className="text-xs text-red-300">{post.explanation}</p>
                      {post.url && (
                        <a
                          href={post.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 mt-1"
                        >
                          <ExternalLink className="h-3 w-3" />
                          View Original Post
                        </a>
                      )}
                    </div>
                  ))}
                {getHighRiskPosts().length > 3 && (
                  <p className="text-sm text-gray-400 text-center">
                    ... and {getHighRiskPosts().length - 3} more high-risk posts
                  </p>
                )}
              </div>
            </CardContent>
          </Card>
        )}

        {/* Enhanced Data Table */}
        <Card className="bg-gray-900/50 border-gray-700">
          <CardHeader>
            <CardTitle className="text-white">📋 Post Analysis Table {selectedUser && `- ${selectedUser}`}</CardTitle>
            <CardDescription className="text-gray-400">
              Real-time data from investigations with links and engagement metrics
              {selectedUser && ` (showing data for ${selectedUser})`}
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="overflow-x-auto">
              <div className="max-h-96 overflow-y-auto">
                <table className="w-full text-sm">
                  <thead className="sticky top-0 bg-gray-800">
                    <tr className="border-b border-gray-700">
                      <th className="text-left p-3 text-gray-300">Timestamp</th>
                      <th className="text-left p-3 text-gray-300">User</th>
                      <th className="text-left p-3 text-gray-300">Platform</th>
                      <th className="text-left p-3 text-gray-300">Content</th>
                      <th className="text-left p-3 text-gray-300">Emotion</th>
                      <th className="text-left p-3 text-gray-300">Risk</th>
                      <th className="text-left p-3 text-gray-300">Engagement</th>
                      <th className="text-left p-3 text-gray-300">Link</th>
                      <th className="text-left p-3 text-gray-300">Tagged</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredPosts.map((post, index) => (
                      <tr
                        key={index}
                        className="border-b border-gray-700/50 hover:bg-gray-800/50 cursor-pointer"
                        onClick={() => setSelectedUser(post.username || null)}
                      >
                        <td className="p-3 text-gray-400 text-xs">{new Date(post.timestamp).toLocaleString()}</td>
                        <td className="p-3">
                          <Badge
                            variant="outline"
                            className="text-xs border-blue-500/30 text-blue-300 cursor-pointer hover:bg-blue-500/20"
                            onClick={(e) => {
                              e.stopPropagation()
                              setSelectedUser(post.username || null)
                            }}
                          >
                            @{post.username || "unknown"}
                          </Badge>
                        </td>
                        <td className="p-3">
                          <Badge variant="outline" className="text-xs border-gray-500/30 text-gray-300">
                            {post.platform || "unknown"}
                          </Badge>
                        </td>
                        <td className="p-3 text-white max-w-xs">
                          <div className="truncate" title={post.text}>
                            {post.text}
                          </div>
                        </td>
                        <td className="p-3">
                          <Badge
                            style={{
                              backgroundColor:
                                EMOTION_COLORS[post.emotion_label as keyof typeof EMOTION_COLORS] || "#6B7280",
                            }}
                            className="text-white"
                          >
                            {post.emotion_label}
                          </Badge>
                        </td>
                        <td className="p-3">
                          {post.risk_level && (
                            <Badge
                              style={{
                                backgroundColor: RISK_COLORS[post.risk_level],
                              }}
                              className="text-white"
                            >
                              {post.risk_level}
                            </Badge>
                          )}
                        </td>
                        <td className="p-3 text-gray-400 text-xs">
                          {post.engagement ? post.engagement.toLocaleString() : "N/A"}
                        </td>
                        <td className="p-3">
                          {post.url && (
                            <a
                              href={post.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-blue-400 hover:text-blue-300"
                              onClick={(e) => e.stopPropagation()}
                            >
                              <ExternalLink className="h-4 w-4" />
                            </a>
                          )}
                        </td>
                        <td className="p-3">
                          {post.tagged_users && post.tagged_users.length > 0 && (
                            <div className="flex flex-wrap gap-1">
                              {post.tagged_users.slice(0, 2).map((user, i) => (
                                <Badge key={i} variant="secondary" className="text-xs">
                                  @{user}
                                </Badge>
                              ))}
                              {post.tagged_users.length > 2 && (
                                <Badge variant="secondary" className="text-xs">
                                  +{post.tagged_users.length - 2}
                                </Badge>
                              )}
                            </div>
                          )}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
            {filteredPosts.length === 0 && (
              <div className="text-center py-8 text-gray-400">
                <p>No posts found matching current filters.</p>
                <Button onClick={loadRealData} className="mt-4 bg-blue-600 hover:bg-blue-700">
                  <RefreshCw className="h-4 w-4 mr-2" />
                  Reload Data
                </Button>
              </div>
            )}
          </CardContent>
        </Card>
      </main>

      {/* AI Chatbot */}
      {chatOpen && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <Card className="w-full max-w-2xl h-[600px] bg-gray-900 border-gray-700 flex flex-col">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-4">
              <div>
                <CardTitle className="text-white flex items-center gap-2">
                  <Bot className="h-5 w-5 text-purple-400" />🤖 AI Analysis Assistant
                </CardTitle>
                <CardDescription className="text-gray-400">
                  Ask questions about the timeline data and get intelligent insights
                </CardDescription>
              </div>
              <Button variant="ghost" size="sm" onClick={() => setChatOpen(false)}>
                <X className="h-4 w-4" />
              </Button>
            </CardHeader>

            <CardContent className="flex-1 flex flex-col">
              {/* Chat Messages */}
              <div className="flex-1 overflow-y-auto space-y-4 mb-4 p-4 bg-gray-800/30 rounded-lg">
                {chatMessages.length === 0 && (
                  <div className="text-center text-gray-400 py-8">
                    <Bot className="h-12 w-12 mx-auto mb-4 text-purple-400" />
                    <p className="mb-2">👋 Hello! I'm your AI analysis assistant.</p>
                    <p className="text-sm">Ask me about:</p>
                    <div className="mt-2 space-y-1 text-xs">
                      <p>• "Give me a summary" - Overall analysis</p>
                      <p>• "Show me risk analysis" - High-risk content</p>
                      <p>• "Tell me about [username]" - User profiles</p>
                      <p>• "What are the trends?" - Pattern analysis</p>
                    </div>
                  </div>
                )}

                {chatMessages.map((message) => (
                  <div key={message.id} className={`flex ${message.type === "user" ? "justify-end" : "justify-start"}`}>
                    <div
                      className={`max-w-[80%] p-3 rounded-lg ${
                        message.type === "user" ? "bg-blue-600 text-white" : "bg-gray-700 text-gray-100"
                      }`}
                    >
                      <div className="flex items-start gap-2">
                        {message.type === "bot" && <Bot className="h-4 w-4 mt-0.5 text-purple-400 flex-shrink-0" />}
                        {message.type === "user" && <User className="h-4 w-4 mt-0.5 text-blue-200 flex-shrink-0" />}
                        <div className="flex-1">
                          <div className="whitespace-pre-wrap text-sm">{message.message}</div>
                          <div className="text-xs opacity-70 mt-1">
                            {new Date(message.timestamp).toLocaleTimeString()}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}

                {chatLoading && (
                  <div className="flex justify-start">
                    <div className="bg-gray-700 text-gray-100 p-3 rounded-lg">
                      <div className="flex items-center gap-2">
                        <Bot className="h-4 w-4 text-purple-400" />
                        <div className="flex space-x-1">
                          <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
                          <div
                            className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"
                            style={{ animationDelay: "0.1s" }}
                          ></div>
                          <div
                            className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"
                            style={{ animationDelay: "0.2s" }}
                          ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                )}
              </div>

              {/* Chat Input */}
              <div className="flex gap-2">
                <Input
                  placeholder="Ask me about the analysis data..."
                  value={chatInput}
                  onChange={(e) => setChatInput(e.target.value)}
                  onKeyPress={(e) => e.key === "Enter" && sendChatMessage()}
                  className="flex-1 bg-gray-800 border-gray-600 text-white"
                  disabled={chatLoading}
                />
                <Button
                  onClick={sendChatMessage}
                  disabled={chatLoading || !chatInput.trim()}
                  className="bg-purple-600 hover:bg-purple-700"
                >
                  <Send className="h-4 w-4" />
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  )
}
