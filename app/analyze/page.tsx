// "use client"

// import { useState } from "react"
// import { MatrixBackground } from "@/components/matrix-background"
// import { Button } from "@/components/ui/button"
// import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
// import { Input } from "@/components/ui/input"
// import { Label } from "@/components/ui/label"
// import { Checkbox } from "@/components/ui/checkbox"
// import { Progress } from "@/components/ui/progress"
// import { Badge } from "@/components/ui/badge"
// import { useToast } from "@/hooks/use-toast"
// import { Search, Shield, MessageSquare, Github, Camera, Newspaper, Brain, Download, Play, Loader2 } from "lucide-react"
// import Link from "next/link"

// interface AnalysisConfig {
//   username: string
//   platforms: string[]
//   aiModels: string[]
//   exportFormats: string[]
// }

// export default function AnalyzePage() {
//   const [config, setConfig] = useState<AnalysisConfig>({
//     username: "",
//     platforms: [],
//     aiModels: ["sentiment", "ner"],
//     exportFormats: ["csv"],
//   })
//   const [isAnalyzing, setIsAnalyzing] = useState(false)
//   const [progress, setProgress] = useState(0)
//   const [currentStep, setCurrentStep] = useState("")
//   const { toast } = useToast()

//   const platforms = [
//     { id: "reddit", name: "Reddit", icon: <MessageSquare className="h-4 w-4" />, color: "bg-orange-500" },
//     { id: "twitter", name: "Twitter/X", icon: <MessageSquare className="h-4 w-4" />, color: "bg-blue-500" },
//     { id: "github", name: "GitHub", icon: <Github className="h-4 w-4" />, color: "bg-gray-500" },
//     { id: "instagram", name: "Instagram", icon: <Camera className="h-4 w-4" />, color: "bg-pink-500" },
//     { id: "news", name: "News Sites", icon: <Newspaper className="h-4 w-4" />, color: "bg-green-500" },
//   ]

//   const aiModels = [
//     { id: "sentiment", name: "Sentiment Analysis", description: "Analyze emotional tone" },
//     { id: "ner", name: "Named Entity Recognition", description: "Extract entities and locations" },
//     { id: "toxicity", name: "Toxicity Detection", description: "Identify harmful content" },
//     { id: "summary", name: "Content Summarization", description: "Generate AI summaries" },
//   ]

//   const exportFormats = [
//     { id: "csv", name: "CSV Export", description: "Structured data format" },
//     { id: "pdf", name: "PDF Report", description: "Formatted analysis report" },
//     { id: "json", name: "JSON Data", description: "Raw data export" },
//   ]

//   const handlePlatformToggle = (platformId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       platforms: prev.platforms.includes(platformId)
//         ? prev.platforms.filter((p) => p !== platformId)
//         : [...prev.platforms, platformId],
//     }))
//   }

//   const handleAIModelToggle = (modelId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       aiModels: prev.aiModels.includes(modelId)
//         ? prev.aiModels.filter((m) => m !== modelId)
//         : [...prev.aiModels, modelId],
//     }))
//   }

//   const handleExportToggle = (formatId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       exportFormats: prev.exportFormats.includes(formatId)
//         ? prev.exportFormats.filter((f) => f !== formatId)
//         : [...prev.exportFormats, formatId],
//     }))
//   }

//   const startAnalysis = async () => {
//     if (!config.username.trim()) {
//       toast({
//         title: "Username Required",
//         description: "Please enter a username to analyze",
//         variant: "destructive",
//       })
//       return
//     }

//     if (config.platforms.length === 0) {
//       toast({
//         title: "Platform Required",
//         description: "Please select at least one platform to analyze",
//         variant: "destructive",
//       })
//       return
//     }

//     setIsAnalyzing(true)
//     setProgress(0)

//     try {
//       // Simulate analysis steps
//       const steps = [
//         "Initializing scrapers...",
//         "Collecting data from platforms...",
//         "Processing with AI models...",
//         "Generating visualizations...",
//         "Creating reports...",
//         "Analysis complete!",
//       ]

//       for (let i = 0; i < steps.length; i++) {
//         setCurrentStep(steps[i])
//         setProgress(((i + 1) / steps.length) * 100)
//         await new Promise((resolve) => setTimeout(resolve, 2000))
//       }

//       // Call backend API
//       const response = await fetch("/api/analyze", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(config),
//       })

//       if (response.ok) {
//         const result = await response.json()
//         toast({
//           title: "Analysis Complete",
//           description: `Successfully analyzed ${config.username} across ${config.platforms.length} platforms`,
//         })
//         // Redirect to results page
//         window.location.href = `/results/${result.investigationId}`
//       } else {
//         throw new Error("Analysis failed")
//       }
//     } catch (error) {
//       toast({
//         title: "Analysis Failed",
//         description: "An error occurred during analysis. Please try again.",
//         variant: "destructive",
//       })
//     } finally {
//       setIsAnalyzing(false)
//       setProgress(0)
//       setCurrentStep("")
//     }
//   }

//   return (
//     <div className="min-h-screen bg-black text-white relative">
//       <MatrixBackground />

//       {/* Header */}
//       <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
//         <div className="container mx-auto px-4 py-4 flex items-center justify-between">
//           <Link href="/" className="flex items-center space-x-2">
//             <Shield className="h-8 w-8 text-blue-400" />
//             <span className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
//               OSINT Platform
//             </span>
//           </Link>
//           <nav className="flex items-center space-x-6">
//             <Link href="/dashboard" className="hover:text-blue-400 transition-colors">
//               Dashboard
//             </Link>
//             <Link href="/reports" className="hover:text-blue-400 transition-colors">
//               Reports
//             </Link>
//           </nav>
//         </div>
//       </header>

//       <div className="relative z-10 container mx-auto px-4 py-8">
//         <div className="max-w-4xl mx-auto">
//           <div className="text-center mb-8">
//             <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent mb-4">
//               Intelligence Analysis
//             </h1>
//             <p className="text-gray-300 text-lg">Configure your OSINT investigation parameters</p>
//           </div>

//           <div className="grid lg:grid-cols-3 gap-8">
//             {/* Configuration Panel */}
//             <div className="lg:col-span-2 space-y-6">
//               {/* Target Configuration */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Search className="mr-2 h-5 w-5" />
//                     Target Configuration
//                   </CardTitle>
//                   <CardDescription>Specify the target username and investigation scope</CardDescription>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   <div>
//                     <Label htmlFor="username">Target Username</Label>
//                     <Input
//                       id="username"
//                       placeholder="Enter username to investigate"
//                       value={config.username}
//                       onChange={(e) => setConfig((prev) => ({ ...prev, username: e.target.value }))}
//                       className="bg-gray-800 border-gray-700 text-white"
//                     />
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Platform Selection */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Data Sources</CardTitle>
//                   <CardDescription>Select platforms to gather intelligence from</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="grid sm:grid-cols-2 gap-4">
//                     {platforms.map((platform) => (
//                       <div
//                         key={platform.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={platform.id}
//                           checked={config.platforms.includes(platform.id)}
//                           onCheckedChange={() => handlePlatformToggle(platform.id)}
//                         />
//                         <div className="flex items-center space-x-2 flex-1">
//                           <div className={`w-3 h-3 rounded-full ${platform.color}`} />
//                           {platform.icon}
//                           <Label htmlFor={platform.id} className="text-white cursor-pointer">
//                             {platform.name}
//                           </Label>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* AI Models */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Brain className="mr-2 h-5 w-5" />
//                     AI Analysis Models
//                   </CardTitle>
//                   <CardDescription>Choose AI models for content analysis</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="space-y-3">
//                     {aiModels.map((model) => (
//                       <div
//                         key={model.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={model.id}
//                           checked={config.aiModels.includes(model.id)}
//                           onCheckedChange={() => handleAIModelToggle(model.id)}
//                         />
//                         <div className="flex-1">
//                           <Label htmlFor={model.id} className="text-white cursor-pointer font-medium">
//                             {model.name}
//                           </Label>
//                           <p className="text-sm text-gray-400">{model.description}</p>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Export Options */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Download className="mr-2 h-5 w-5" />
//                     Export Formats
//                   </CardTitle>
//                   <CardDescription>Select output formats for your analysis</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="space-y-3">
//                     {exportFormats.map((format) => (
//                       <div
//                         key={format.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={format.id}
//                           checked={config.exportFormats.includes(format.id)}
//                           onCheckedChange={() => handleExportToggle(format.id)}
//                         />
//                         <div className="flex-1">
//                           <Label htmlFor={format.id} className="text-white cursor-pointer font-medium">
//                             {format.name}
//                           </Label>
//                           <p className="text-sm text-gray-400">{format.description}</p>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>
//             </div>

//             {/* Analysis Panel */}
//             <div className="space-y-6">
//               {/* Configuration Summary */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Configuration Summary</CardTitle>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   <div>
//                     <Label className="text-sm text-gray-400">Target</Label>
//                     <p className="text-white font-mono">{config.username || "Not specified"}</p>
//                   </div>

//                   <div>
//                     <Label className="text-sm text-gray-400">Platforms ({config.platforms.length})</Label>
//                     <div className="flex flex-wrap gap-1 mt-1">
//                       {config.platforms.map((platformId) => {
//                         const platform = platforms.find((p) => p.id === platformId)
//                         return platform ? (
//                           <Badge key={platformId} variant="secondary" className="text-xs">
//                             {platform.name}
//                           </Badge>
//                         ) : null
//                       })}
//                     </div>
//                   </div>

//                   <div>
//                     <Label className="text-sm text-gray-400">AI Models ({config.aiModels.length})</Label>
//                     <div className="flex flex-wrap gap-1 mt-1">
//                       {config.aiModels.map((modelId) => {
//                         const model = aiModels.find((m) => m.id === modelId)
//                         return model ? (
//                           <Badge key={modelId} variant="outline" className="text-xs border-blue-500/30 text-blue-300">
//                             {model.name}
//                           </Badge>
//                         ) : null
//                       })}
//                     </div>
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Analysis Control */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Analysis Control</CardTitle>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   {isAnalyzing ? (
//                     <div className="space-y-4">
//                       <div className="flex items-center space-x-2">
//                         <Loader2 className="h-4 w-4 animate-spin text-blue-400" />
//                         <span className="text-sm text-gray-300">{currentStep}</span>
//                       </div>
//                       <Progress value={progress} className="w-full" />
//                       <p className="text-xs text-gray-400 text-center">{Math.round(progress)}% Complete</p>
//                     </div>
//                   ) : (
//                     <Button
//                       onClick={startAnalysis}
//                       className="w-full bg-blue-600 hover:bg-blue-700 text-white cyber-glow"
//                       size="lg"
//                     >
//                       <Play className="mr-2 h-4 w-4" />
//                       Start Analysis
//                     </Button>
//                   )}
//                 </CardContent>
//               </Card>

//               {/* Legal Notice */}
//               <Card className="bg-yellow-900/20 border-yellow-500/20">
//                 <CardContent className="pt-6">
//                   <div className="flex items-start space-x-2">
//                     <Shield className="h-5 w-5 text-yellow-400 mt-0.5 flex-shrink-0" />
//                     <div>
//                       <p className="text-sm text-yellow-200 font-medium mb-1">Ethical Use Only</p>
//                       <p className="text-xs text-yellow-300/80">
//                         This tool is designed for ethical research, journalism, and cybersecurity audits. Only public,
//                         non-authenticated data is collected.
//                       </p>
//                     </div>
//                   </div>
//                 </CardContent>
//               </Card>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   )
// }


// new 

// "use client"

// import { useState } from "react"
// import { MatrixBackground } from "@/components/matrix-background"
// import { Button } from "@/components/ui/button"
// import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
// import { Input } from "@/components/ui/input"
// import { Label } from "@/components/ui/label"
// import { Checkbox } from "@/components/ui/checkbox"
// import { Progress } from "@/components/ui/progress"
// import { Badge } from "@/components/ui/badge"
// import { useToast } from "@/hooks/use-toast"
// import { Search, Shield, MessageSquare, Github, Camera, Newspaper, Brain, Download, Play, Loader2 } from "lucide-react"
// import Link from "next/link"

// interface AnalysisConfig {
//   username: string
//   platforms: string[]
//   aiModels: string[]
//   exportFormats: string[]
// }

// export default function AnalyzePage() {
//   const [config, setConfig] = useState<AnalysisConfig>({
//     username: "",
//     platforms: [],
//     aiModels: ["sentiment", "ner"],
//     exportFormats: ["csv"],
//   })
//   const [isAnalyzing, setIsAnalyzing] = useState(false)
//   const [progress, setProgress] = useState(0)
//   const [currentStep, setCurrentStep] = useState("")
//   const { toast } = useToast()

//   const platforms = [
//     { id: "reddit", name: "Reddit", icon: <MessageSquare className="h-4 w-4" />, color: "bg-orange-500" },
//     { id: "twitter", name: "Twitter/X", icon: <MessageSquare className="h-4 w-4" />, color: "bg-blue-500" },
//     { id: "github", name: "GitHub", icon: <Github className="h-4 w-4" />, color: "bg-gray-500" },
//     { id: "instagram", name: "Instagram", icon: <Camera className="h-4 w-4" />, color: "bg-pink-500" },
//     { id: "news", name: "News Sites", icon: <Newspaper className="h-4 w-4" />, color: "bg-green-500" },
//   ]

//   const aiModels = [
//     { id: "sentiment", name: "Sentiment Analysis", description: "Analyze emotional tone" },
//     { id: "ner", name: "Named Entity Recognition", description: "Extract entities and locations" },
//     { id: "toxicity", name: "Toxicity Detection", description: "Identify harmful content" },
//     { id: "summary", name: "Content Summarization", description: "Generate AI summaries" },
//   ]

//   const exportFormats = [
//     { id: "csv", name: "CSV Export", description: "Structured data format" },
//     { id: "pdf", name: "PDF Report", description: "Formatted analysis report" },
//     { id: "json", name: "JSON Data", description: "Raw data export" },
//   ]

//   const handlePlatformToggle = (platformId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       platforms: prev.platforms.includes(platformId)
//         ? prev.platforms.filter((p) => p !== platformId)
//         : [...prev.platforms, platformId],
//     }))
//   }

//   const handleAIModelToggle = (modelId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       aiModels: prev.aiModels.includes(modelId)
//         ? prev.aiModels.filter((m) => m !== modelId)
//         : [...prev.aiModels, modelId],
//     }))
//   }

//   const handleExportToggle = (formatId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       exportFormats: prev.exportFormats.includes(formatId)
//         ? prev.exportFormats.filter((f) => f !== formatId)
//         : [...prev.exportFormats, formatId],
//     }))
//   }

//   const startAnalysis = async () => {
//     if (!config.username.trim()) {
//       toast({
//         title: "Username Required",
//         description: "Please enter a username to analyze",
//         variant: "destructive",
//       })
//       return
//     }

//     if (config.platforms.length === 0) {
//       toast({
//         title: "Platform Required",
//         description: "Please select at least one platform to analyze",
//         variant: "destructive",
//       })
//       return
//     }

//     setIsAnalyzing(true)
//     setProgress(0)

//     try {
//       // Simulate analysis steps
//       const steps = [
//         "Initializing scrapers...",
//         "Collecting data from platforms...",
//         "Processing with AI models...",
//         "Generating visualizations...",
//         "Creating reports...",
//         "Analysis complete!",
//       ]

//       for (let i = 0; i < steps.length; i++) {
//         setCurrentStep(steps[i])
//         setProgress(((i + 1) / steps.length) * 100)
//         await new Promise((resolve) => setTimeout(resolve, 2000))
//       }

//       // Call backend API
//       const response = await fetch("/api/analyze", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify(config),
//       })

//       // After successful API response
//       if (response.ok) {
//         const result = await response.json()

//         // Store investigation in localStorage
//         const investigation = {
//           id: result.investigationId,
//           targetUser: config.username,
//           platforms: config.platforms,
//           status: "COMPLETED",
//           createdAt: new Date().toISOString(),
//           completedAt: new Date().toISOString(),
//           results: result.results,
//         }

//         const stored = localStorage.getItem("osint_investigations")
//         const investigations = stored ? JSON.parse(stored) : []
//         investigations.unshift(investigation)
//         localStorage.setItem("osint_investigations", JSON.stringify(investigations))

//         toast({
//           title: "Analysis Complete",
//           description: `Successfully analyzed ${config.username} across ${config.platforms.length} platforms`,
//         })

//         // Redirect to dashboard
//         window.location.href = `/dashboard`
//       } else {
//         throw new Error("Analysis failed")
//       }
//     } catch (error) {
//       toast({
//         title: "Analysis Failed",
//         description: "An error occurred during analysis. Please try again.",
//         variant: "destructive",
//       })
//     } finally {
//       setIsAnalyzing(false)
//       setProgress(0)
//       setCurrentStep("")
//     }
//   }

//   return (
//     <div className="min-h-screen bg-black text-white relative">
//       <MatrixBackground />

//       {/* Header */}
//       <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
//         <div className="container mx-auto px-4 py-4 flex items-center justify-between">
//           <Link href="/" className="flex items-center space-x-2">
//             <Shield className="h-8 w-8 text-blue-400" />
//             <span className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
//               OSINT Platform
//             </span>
//           </Link>
//           <nav className="flex items-center space-x-6">
//             <Link href="/dashboard" className="hover:text-blue-400 transition-colors">
//               Dashboard
//             </Link>
//             <Link href="/reports" className="hover:text-blue-400 transition-colors">
//               Reports
//             </Link>
//           </nav>
//         </div>
//       </header>

//       <div className="relative z-10 container mx-auto px-4 py-8">
//         <div className="max-w-4xl mx-auto">
//           <div className="text-center mb-8">
//             <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent mb-4">
//               Intelligence Analysis
//             </h1>
//             <p className="text-gray-300 text-lg">Configure your OSINT investigation parameters</p>
//           </div>

//           <div className="grid lg:grid-cols-3 gap-8">
//             {/* Configuration Panel */}
//             <div className="lg:col-span-2 space-y-6">
//               {/* Target Configuration */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Search className="mr-2 h-5 w-5" />
//                     Target Configuration
//                   </CardTitle>
//                   <CardDescription>Specify the target username and investigation scope</CardDescription>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   <div>
//                     <Label htmlFor="username">Target Username</Label>
//                     <Input
//                       id="username"
//                       placeholder="Enter username to investigate"
//                       value={config.username}
//                       onChange={(e) => setConfig((prev) => ({ ...prev, username: e.target.value }))}
//                       className="bg-gray-800 border-gray-700 text-white"
//                     />
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Platform Selection */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Data Sources</CardTitle>
//                   <CardDescription>Select platforms to gather intelligence from</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="grid sm:grid-cols-2 gap-4">
//                     {platforms.map((platform) => (
//                       <div
//                         key={platform.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={platform.id}
//                           checked={config.platforms.includes(platform.id)}
//                           onCheckedChange={() => handlePlatformToggle(platform.id)}
//                         />
//                         <div className="flex items-center space-x-2 flex-1">
//                           <div className={`w-3 h-3 rounded-full ${platform.color}`} />
//                           {platform.icon}
//                           <Label htmlFor={platform.id} className="text-white cursor-pointer">
//                             {platform.name}
//                           </Label>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* AI Models */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Brain className="mr-2 h-5 w-5" />
//                     AI Analysis Models
//                   </CardTitle>
//                   <CardDescription>Choose AI models for content analysis</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="space-y-3">
//                     {aiModels.map((model) => (
//                       <div
//                         key={model.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={model.id}
//                           checked={config.aiModels.includes(model.id)}
//                           onCheckedChange={() => handleAIModelToggle(model.id)}
//                         />
//                         <div className="flex-1">
//                           <Label htmlFor={model.id} className="text-white cursor-pointer font-medium">
//                             {model.name}
//                           </Label>
//                           <p className="text-sm text-gray-400">{model.description}</p>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Export Options */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Download className="mr-2 h-5 w-5" />
//                     Export Formats
//                   </CardTitle>
//                   <CardDescription>Select output formats for your analysis</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="space-y-3">
//                     {exportFormats.map((format) => (
//                       <div
//                         key={format.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={format.id}
//                           checked={config.exportFormats.includes(format.id)}
//                           onCheckedChange={() => handleExportToggle(format.id)}
//                         />
//                         <div className="flex-1">
//                           <Label htmlFor={format.id} className="text-white cursor-pointer font-medium">
//                             {format.name}
//                           </Label>
//                           <p className="text-sm text-gray-400">{format.description}</p>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>
//             </div>

//             {/* Analysis Panel */}
//             <div className="space-y-6">
//               {/* Configuration Summary */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Configuration Summary</CardTitle>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   <div>
//                     <Label className="text-sm text-gray-400">Target</Label>
//                     <p className="text-white font-mono">{config.username || "Not specified"}</p>
//                   </div>

//                   <div>
//                     <Label className="text-sm text-gray-400">Platforms ({config.platforms.length})</Label>
//                     <div className="flex flex-wrap gap-1 mt-1">
//                       {config.platforms.map((platformId) => {
//                         const platform = platforms.find((p) => p.id === platformId)
//                         return platform ? (
//                           <Badge key={platformId} variant="secondary" className="text-xs">
//                             {platform.name}
//                           </Badge>
//                         ) : null
//                       })}
//                     </div>
//                   </div>

//                   <div>
//                     <Label className="text-sm text-gray-400">AI Models ({config.aiModels.length})</Label>
//                     <div className="flex flex-wrap gap-1 mt-1">
//                       {config.aiModels.map((modelId) => {
//                         const model = aiModels.find((m) => m.id === modelId)
//                         return model ? (
//                           <Badge key={modelId} variant="outline" className="text-xs border-blue-500/30 text-blue-300">
//                             {model.name}
//                           </Badge>
//                         ) : null
//                       })}
//                     </div>
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Analysis Control */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Analysis Control</CardTitle>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   {isAnalyzing ? (
//                     <div className="space-y-4">
//                       <div className="flex items-center space-x-2">
//                         <Loader2 className="h-4 w-4 animate-spin text-blue-400" />
//                         <span className="text-sm text-gray-300">{currentStep}</span>
//                       </div>
//                       <Progress value={progress} className="w-full" />
//                       <p className="text-xs text-gray-400 text-center">{Math.round(progress)}% Complete</p>
//                     </div>
//                   ) : (
//                     <Button
//                       onClick={startAnalysis}
//                       className="w-full bg-blue-600 hover:bg-blue-700 text-white cyber-glow"
//                       size="lg"
//                     >
//                       <Play className="mr-2 h-4 w-4" />
//                       Start Analysis
//                     </Button>
//                   )}
//                 </CardContent>
//               </Card>

//               {/* Legal Notice */}
//               <Card className="bg-yellow-900/20 border-yellow-500/20">
//                 <CardContent className="pt-6">
//                   <div className="flex items-start space-x-2">
//                     <Shield className="h-5 w-5 text-yellow-400 mt-0.5 flex-shrink-0" />
//                     <div>
//                       <p className="text-sm text-yellow-200 font-medium mb-1">Ethical Use Only</p>
//                       <p className="text-xs text-yellow-300/80">
//                         This tool is designed for ethical research, journalism, and cybersecurity audits. Only public,
//                         non-authenticated data is collected.
//                       </p>
//                     </div>
//                   </div>
//                 </CardContent>
//               </Card>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   )
// }


//new 

// "use client"

// import { useState } from "react"
// import { MatrixBackground } from "@/components/matrix-background"
// import { Button } from "@/components/ui/button"
// import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
// import { Input } from "@/components/ui/input"
// import { Label } from "@/components/ui/label"
// import { Checkbox } from "@/components/ui/checkbox"
// import { Progress } from "@/components/ui/progress"
// import { Badge } from "@/components/ui/badge"
// import { Alert, AlertDescription } from "@/components/ui/alert"
// import { useToast } from "@/hooks/use-toast"
// import {
//   Search,
//   Shield,
//   MessageSquare,
//   Github,
//   Camera,
//   Newspaper,
//   Brain,
//   Download,
//   Play,
//   Loader2,
//   AlertCircle,
//   CheckCircle,
// } from "lucide-react"
// import Link from "next/link"

// interface AnalysisConfig {
//   username: string
//   platforms: string[]
//   aiModels: string[]
//   exportFormats: string[]
// }

// interface ErrorDetails {
//   error: string
//   details?: any
//   solution?: string
//   timestamp?: string
// }

// export default function AnalyzePage() {
//   const [config, setConfig] = useState<AnalysisConfig>({
//     username: "",
//     platforms: [],
//     aiModels: ["sentiment", "ner"],
//     exportFormats: ["csv"],
//   })
//   const [isAnalyzing, setIsAnalyzing] = useState(false)
//   const [progress, setProgress] = useState(0)
//   const [currentStep, setCurrentStep] = useState("")
//   const [backendStatus, setBackendStatus] = useState<"unknown" | "online" | "offline">("unknown")
//   const [errorDetails, setErrorDetails] = useState<ErrorDetails | null>(null)
//   const { toast } = useToast()

//   const platforms = [
//     { id: "reddit", name: "Reddit", icon: <MessageSquare className="h-4 w-4" />, color: "bg-orange-500" },
//     { id: "twitter", name: "Twitter/X", icon: <MessageSquare className="h-4 w-4" />, color: "bg-blue-500" },
//     { id: "github", name: "GitHub", icon: <Github className="h-4 w-4" />, color: "bg-gray-500" },
//     { id: "instagram", name: "Instagram", icon: <Camera className="h-4 w-4" />, color: "bg-pink-500" },
//     { id: "news", name: "News Sites", icon: <Newspaper className="h-4 w-4" />, color: "bg-green-500" },
//   ]

//   const aiModels = [
//     { id: "sentiment", name: "Sentiment Analysis", description: "Analyze emotional tone" },
//     { id: "ner", name: "Named Entity Recognition", description: "Extract entities and locations" },
//     { id: "toxicity", name: "Toxicity Detection", description: "Identify harmful content" },
//     { id: "summary", name: "Content Summarization", description: "Generate AI summaries" },
//   ]

//   const exportFormats = [
//     { id: "csv", name: "CSV Export", description: "Structured data format" },
//     { id: "pdf", name: "PDF Report", description: "Formatted analysis report" },
//     { id: "json", name: "JSON Data", description: "Raw data export" },
//   ]

//   // Check backend status
//   const checkBackendStatus = async () => {
//     try {
//       const response = await fetch("/api/analyze", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({
//           username: "test",
//           platforms: ["github"],
//           aiModels: [],
//           exportFormats: [],
//         }),
//       })

//       if (response.status === 503) {
//         setBackendStatus("offline")
//         const errorData = await response.json()
//         setErrorDetails(errorData)
//       } else {
//         setBackendStatus("online")
//         setErrorDetails(null)
//       }
//     } catch (error) {
//       setBackendStatus("offline")
//       setErrorDetails({
//         error: "Cannot connect to backend",
//         details: "Make sure the Python backend is running on port 8000",
//         solution: "Run: cd backend && python main.py",
//       })
//     }
//   }

//   const handlePlatformToggle = (platformId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       platforms: prev.platforms.includes(platformId)
//         ? prev.platforms.filter((p) => p !== platformId)
//         : [...prev.platforms, platformId],
//     }))
//   }

//   const handleAIModelToggle = (modelId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       aiModels: prev.aiModels.includes(modelId)
//         ? prev.aiModels.filter((m) => m !== modelId)
//         : [...prev.aiModels, modelId],
//     }))
//   }

//   const handleExportToggle = (formatId: string) => {
//     setConfig((prev) => ({
//       ...prev,
//       exportFormats: prev.exportFormats.includes(formatId)
//         ? prev.exportFormats.filter((f) => f !== formatId)
//         : [...prev.exportFormats, formatId],
//     }))
//   }

//   const startAnalysis = async () => {
//     console.log("=== Starting Analysis ===")
//     console.log("Config:", config)

//     if (!config.username.trim()) {
//       toast({
//         title: "Username Required",
//         description: "Please enter a username to analyze",
//         variant: "destructive",
//       })
//       return
//     }

//     if (config.platforms.length === 0) {
//       toast({
//         title: "Platform Required",
//         description: "Please select at least one platform to analyze",
//         variant: "destructive",
//       })
//       return
//     }

//     setIsAnalyzing(true)
//     setProgress(0)
//     setErrorDetails(null)

//     try {
//       // Simulate analysis steps with progress
//       const steps = [
//         "Checking backend connection...",
//         "Initializing scrapers...",
//         "Collecting data from platforms...",
//         "Processing with AI models...",
//         "Generating reports...",
//         "Analysis complete!",
//       ]

//       for (let i = 0; i < steps.length - 1; i++) {
//         setCurrentStep(steps[i])
//         setProgress(((i + 1) / steps.length) * 100)
//         await new Promise((resolve) => setTimeout(resolve, 1000))
//       }

//       console.log("Calling backend API...")

//       // Call backend API
//       const response = await fetch("/api/analyze", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify(config),
//       })

//       console.log("Response status:", response.status)
//       console.log("Response headers:", Object.fromEntries(response.headers.entries()))

//       const responseData = await response.json()
//       console.log("Response data:", responseData)

//       if (response.ok) {
//         setCurrentStep(steps[steps.length - 1])
//         setProgress(100)

//         // Store investigation in localStorage
//         const investigation = {
//           id: responseData.investigationId,
//           targetUser: config.username,
//           platforms: config.platforms,
//           status: "COMPLETED",
//           createdAt: new Date().toISOString(),
//           completedAt: new Date().toISOString(),
//           results: responseData.results,
//         }

//         const stored = localStorage.getItem("osint_investigations")
//         const investigations = stored ? JSON.parse(stored) : []
//         investigations.unshift(investigation)
//         localStorage.setItem("osint_investigations", JSON.stringify(investigations))

//         toast({
//           title: "Analysis Complete",
//           description: `Successfully analyzed ${config.username} across ${config.platforms.length} platforms`,
//         })

//         // Wait a moment then redirect
//         setTimeout(() => {
//           window.location.href = `/dashboard`
//         }, 2000)
//       } else {
//         throw new Error(`Analysis failed: ${response.status}`)
//       }
//     } catch (error) {
//       console.error("Analysis error:", error)

//       let errorMessage = "An error occurred during analysis"
//       let errorDetails = "Please try again"

//       if (error instanceof TypeError && error.message.includes("fetch")) {
//         errorMessage = "Cannot connect to backend"
//         errorDetails = "Make sure the Python backend is running on port 8000"
//       } else if (error instanceof Error) {
//         errorMessage = error.message
//       }

//       setErrorDetails({
//         error: errorMessage,
//         details: errorDetails,
//         timestamp: new Date().toISOString(),
//       })

//       toast({
//         title: "Analysis Failed",
//         description: errorMessage,
//         variant: "destructive",
//       })
//     } finally {
//       setIsAnalyzing(false)
//       if (progress < 100) {
//         setProgress(0)
//         setCurrentStep("")
//       }
//     }
//   }

//   return (
//     <div className="min-h-screen bg-black text-white relative">
//       <MatrixBackground />

//       {/* Header */}
//       <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
//         <div className="container mx-auto px-4 py-4 flex items-center justify-between">
//           <Link href="/" className="flex items-center space-x-2">
//             <Shield className="h-8 w-8 text-blue-400" />
//             <span className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
//               OSINT Platform
//             </span>
//           </Link>
//           <nav className="flex items-center space-x-6">
//             <Link href="/dashboard" className="hover:text-blue-400 transition-colors">
//               Dashboard
//             </Link>
//             <Button
//               variant="outline"
//               size="sm"
//               onClick={checkBackendStatus}
//               className="border-blue-500/30 text-blue-400 bg-transparent"
//             >
//               Check Backend
//             </Button>
//           </nav>
//         </div>
//       </header>

//       <div className="relative z-10 container mx-auto px-4 py-8">
//         <div className="max-w-4xl mx-auto">
//           <div className="text-center mb-8">
//             <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent mb-4">
//               Intelligence Analysis
//             </h1>
//             <p className="text-gray-300 text-lg">Configure your OSINT investigation parameters</p>
//           </div>

//           {/* Backend Status Alert */}
//           {backendStatus === "offline" && (
//             <Alert className="mb-6 border-red-500/50 bg-red-900/20">
//               <AlertCircle className="h-4 w-4" />
//               <AlertDescription>
//                 <div className="space-y-2">
//                   <p className="font-semibold text-red-400">Backend Connection Failed</p>
//                   {errorDetails && (
//                     <div className="text-sm text-red-300">
//                       <p>
//                         <strong>Error:</strong> {errorDetails.error}
//                       </p>
//                       {errorDetails.details && (
//                         <p>
//                           <strong>Details:</strong> {errorDetails.details}
//                         </p>
//                       )}
//                       {errorDetails.solution && (
//                         <p>
//                           <strong>Solution:</strong> {errorDetails.solution}
//                         </p>
//                       )}
//                     </div>
//                   )}
//                 </div>
//               </AlertDescription>
//             </Alert>
//           )}

//           {backendStatus === "online" && (
//             <Alert className="mb-6 border-green-500/50 bg-green-900/20">
//               <CheckCircle className="h-4 w-4" />
//               <AlertDescription>
//                 <p className="font-semibold text-green-400">Backend Connected Successfully</p>
//               </AlertDescription>
//             </Alert>
//           )}

//           {/* Error Details */}
//           {errorDetails && isAnalyzing === false && (
//             <Alert className="mb-6 border-red-500/50 bg-red-900/20">
//               <AlertCircle className="h-4 w-4" />
//               <AlertDescription>
//                 <div className="space-y-2">
//                   <p className="font-semibold text-red-400">Analysis Error</p>
//                   <div className="text-sm text-red-300">
//                     <p>
//                       <strong>Error:</strong> {errorDetails.error}
//                     </p>
//                     {errorDetails.details && (
//                       <p>
//                         <strong>Details:</strong> {errorDetails.details}
//                       </p>
//                     )}
//                     {errorDetails.solution && (
//                       <p>
//                         <strong>Solution:</strong> {errorDetails.solution}
//                       </p>
//                     )}
//                     {errorDetails.timestamp && (
//                       <p>
//                         <strong>Time:</strong> {new Date(errorDetails.timestamp).toLocaleString()}
//                       </p>
//                     )}
//                   </div>
//                 </div>
//               </AlertDescription>
//             </Alert>
//           )}

//           <div className="grid lg:grid-cols-3 gap-8">
//             {/* Configuration Panel */}
//             <div className="lg:col-span-2 space-y-6">
//               {/* Target Configuration */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Search className="mr-2 h-5 w-5" />
//                     Target Configuration
//                   </CardTitle>
//                   <CardDescription>Specify the target username and investigation scope</CardDescription>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   <div>
//                     <Label htmlFor="username">Target Username</Label>
//                     <Input
//                       id="username"
//                       placeholder="Enter username to investigate (e.g., octocat)"
//                       value={config.username}
//                       onChange={(e) => setConfig((prev) => ({ ...prev, username: e.target.value }))}
//                       className="bg-gray-800 border-gray-700 text-white"
//                     />
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Platform Selection */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Data Sources</CardTitle>
//                   <CardDescription>Select platforms to gather intelligence from</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="grid sm:grid-cols-2 gap-4">
//                     {platforms.map((platform) => (
//                       <div
//                         key={platform.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={platform.id}
//                           checked={config.platforms.includes(platform.id)}
//                           onCheckedChange={() => handlePlatformToggle(platform.id)}
//                         />
//                         <div className="flex items-center space-x-2 flex-1">
//                           <div className={`w-3 h-3 rounded-full ${platform.color}`} />
//                           {platform.icon}
//                           <Label htmlFor={platform.id} className="text-white cursor-pointer">
//                             {platform.name}
//                           </Label>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* AI Models */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Brain className="mr-2 h-5 w-5" />
//                     AI Analysis Models
//                   </CardTitle>
//                   <CardDescription>Choose AI models for content analysis</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="space-y-3">
//                     {aiModels.map((model) => (
//                       <div
//                         key={model.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={model.id}
//                           checked={config.aiModels.includes(model.id)}
//                           onCheckedChange={() => handleAIModelToggle(model.id)}
//                         />
//                         <div className="flex-1">
//                           <Label htmlFor={model.id} className="text-white cursor-pointer font-medium">
//                             {model.name}
//                           </Label>
//                           <p className="text-sm text-gray-400">{model.description}</p>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Export Options */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400 flex items-center">
//                     <Download className="mr-2 h-5 w-5" />
//                     Export Formats
//                   </CardTitle>
//                   <CardDescription>Select output formats for your analysis</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="space-y-3">
//                     {exportFormats.map((format) => (
//                       <div
//                         key={format.id}
//                         className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
//                       >
//                         <Checkbox
//                           id={format.id}
//                           checked={config.exportFormats.includes(format.id)}
//                           onCheckedChange={() => handleExportToggle(format.id)}
//                         />
//                         <div className="flex-1">
//                           <Label htmlFor={format.id} className="text-white cursor-pointer font-medium">
//                             {format.name}
//                           </Label>
//                           <p className="text-sm text-gray-400">{format.description}</p>
//                         </div>
//                       </div>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>
//             </div>

//             {/* Analysis Panel */}
//             <div className="space-y-6">
//               {/* Configuration Summary */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Configuration Summary</CardTitle>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   <div>
//                     <Label className="text-sm text-gray-400">Target</Label>
//                     <p className="text-white font-mono">{config.username || "Not specified"}</p>
//                   </div>

//                   <div>
//                     <Label className="text-sm text-gray-400">Platforms ({config.platforms.length})</Label>
//                     <div className="flex flex-wrap gap-1 mt-1">
//                       {config.platforms.map((platformId) => {
//                         const platform = platforms.find((p) => p.id === platformId)
//                         return platform ? (
//                           <Badge key={platformId} variant="secondary" className="text-xs">
//                             {platform.name}
//                           </Badge>
//                         ) : null
//                       })}
//                     </div>
//                   </div>

//                   <div>
//                     <Label className="text-sm text-gray-400">AI Models ({config.aiModels.length})</Label>
//                     <div className="flex flex-wrap gap-1 mt-1">
//                       {config.aiModels.map((modelId) => {
//                         const model = aiModels.find((m) => m.id === modelId)
//                         return model ? (
//                           <Badge key={modelId} variant="outline" className="text-xs border-blue-500/30 text-blue-300">
//                             {model.name}
//                           </Badge>
//                         ) : null
//                       })}
//                     </div>
//                   </div>
//                 </CardContent>
//               </Card>

//               {/* Analysis Control */}
//               <Card className="bg-gray-900/50 border-blue-500/20">
//                 <CardHeader>
//                   <CardTitle className="text-blue-400">Analysis Control</CardTitle>
//                 </CardHeader>
//                 <CardContent className="space-y-4">
//                   {isAnalyzing ? (
//                     <div className="space-y-4">
//                       <div className="flex items-center space-x-2">
//                         <Loader2 className="h-4 w-4 animate-spin text-blue-400" />
//                         <span className="text-sm text-gray-300">{currentStep}</span>
//                       </div>
//                       <Progress value={progress} className="w-full" />
//                       <p className="text-xs text-gray-400 text-center">{Math.round(progress)}% Complete</p>
//                     </div>
//                   ) : (
//                     <Button
//                       onClick={startAnalysis}
//                       className="w-full bg-blue-600 hover:bg-blue-700 text-white cyber-glow"
//                       size="lg"
//                       disabled={backendStatus === "offline"}
//                     >
//                       <Play className="mr-2 h-4 w-4" />
//                       {backendStatus === "offline" ? "Backend Offline" : "Start Analysis"}
//                     </Button>
//                   )}
//                 </CardContent>
//               </Card>

//               {/* Legal Notice */}
//               <Card className="bg-yellow-900/20 border-yellow-500/20">
//                 <CardContent className="pt-6">
//                   <div className="flex items-start space-x-2">
//                     <Shield className="h-5 w-5 text-yellow-400 mt-0.5 flex-shrink-0" />
//                     <div>
//                       <p className="text-sm text-yellow-200 font-medium mb-1">Ethical Use Only</p>
//                       <p className="text-xs text-yellow-300/80">
//                         This tool is designed for ethical research, journalism, and cybersecurity audits. Only public,
//                         non-authenticated data is collected.
//                       </p>
//                     </div>
//                   </div>
//                 </CardContent>
//               </Card>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   )
// }


// above best 
"use client"

import { useState } from "react"
import { MatrixBackground } from "@/components/matrix-background"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Checkbox } from "@/components/ui/checkbox"
import { Progress } from "@/components/ui/progress"
import { Badge } from "@/components/ui/badge"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { useToast } from "@/hooks/use-toast"
import {
  Search,
  Shield,
  MessageSquare,
  Github,
  Camera,
  Newspaper,
  Brain,
  Download,
  Play,
  Loader2,
  AlertCircle,
  CheckCircle,
  Eye,
  TrendingUp,
} from "lucide-react"
import Link from "next/link"

interface AnalysisConfig {
  username: string
  platforms: string[]
  aiModels: string[]
  exportFormats: string[]
}

interface ErrorDetails {
  error: string
  details?: any
  solution?: string
  timestamp?: string
}

export default function AnalyzePage() {
  const [config, setConfig] = useState<AnalysisConfig>({
    username: "",
    platforms: [],
    aiModels: ["sentiment", "ner"],
    exportFormats: ["csv"],
  })
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [progress, setProgress] = useState(0)
  const [currentStep, setCurrentStep] = useState("")
  const [backendStatus, setBackendStatus] = useState<"unknown" | "online" | "offline">("unknown")
  const [errorDetails, setErrorDetails] = useState<ErrorDetails | null>(null)
  const [analysisComplete, setAnalysisComplete] = useState(false)
  const [analysisResults, setAnalysisResults] = useState<any>(null)
  const { toast } = useToast()

  const platforms = [
    { id: "reddit", name: "Reddit", icon: <MessageSquare className="h-4 w-4" />, color: "bg-orange-500" },
    { id: "twitter", name: "Twitter/X", icon: <MessageSquare className="h-4 w-4" />, color: "bg-blue-500" },
    { id: "github", name: "GitHub", icon: <Github className="h-4 w-4" />, color: "bg-gray-500" },
    { id: "instagram", name: "Instagram", icon: <Camera className="h-4 w-4" />, color: "bg-pink-500" },
    { id: "news", name: "News Sites", icon: <Newspaper className="h-4 w-4" />, color: "bg-green-500" },
  ]

  const aiModels = [
    { id: "sentiment", name: "Sentiment Analysis", description: "Analyze emotional tone" },
    { id: "ner", name: "Named Entity Recognition", description: "Extract entities and locations" },
    { id: "toxicity", name: "Toxicity Detection", description: "Identify harmful content" },
    { id: "summary", name: "Content Summarization", description: "Generate AI summaries" },
  ]

  const exportFormats = [
    { id: "csv", name: "CSV Export", description: "Structured data format" },
    { id: "pdf", name: "PDF Report", description: "Formatted analysis report" },
    { id: "json", name: "JSON Data", description: "Raw data export" },
  ]

  // Check backend status
  const checkBackendStatus = async () => {
    try {
      const response = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: "test",
          platforms: ["github"],
          aiModels: [],
          exportFormats: [],
        }),
      })

      if (response.status === 503) {
        setBackendStatus("offline")
        const errorData = await response.json()
        setErrorDetails(errorData)
      } else {
        setBackendStatus("online")
        setErrorDetails(null)
      }
    } catch (error) {
      setBackendStatus("offline")
      setErrorDetails({
        error: "Cannot connect to backend",
        details: "Make sure the Python backend is running on port 8000",
        solution: "Run: cd backend && python main.py",
      })
    }
  }

  const handlePlatformToggle = (platformId: string) => {
    setConfig((prev) => ({
      ...prev,
      platforms: prev.platforms.includes(platformId)
        ? prev.platforms.filter((p) => p !== platformId)
        : [...prev.platforms, platformId],
    }))
  }

  const handleAIModelToggle = (modelId: string) => {
    setConfig((prev) => ({
      ...prev,
      aiModels: prev.aiModels.includes(modelId)
        ? prev.aiModels.filter((m) => m !== modelId)
        : [...prev.aiModels, modelId],
    }))
  }

  const handleExportToggle = (formatId: string) => {
    setConfig((prev) => ({
      ...prev,
      exportFormats: prev.exportFormats.includes(formatId)
        ? prev.exportFormats.filter((f) => f !== formatId)
        : [...prev.exportFormats, formatId],
    }))
  }

  const startAnalysis = async () => {
    console.log("=== Starting Analysis ===")
    console.log("Config:", config)

    if (!config.username.trim()) {
      toast({
        title: "Username Required",
        description: "Please enter a username to analyze",
        variant: "destructive",
      })
      return
    }

    if (config.platforms.length === 0) {
      toast({
        title: "Platform Required",
        description: "Please select at least one platform to analyze",
        variant: "destructive",
      })
      return
    }

    setIsAnalyzing(true)
    setProgress(0)
    setErrorDetails(null)
    setAnalysisComplete(false)

    try {
      // Simulate analysis steps with progress
      const steps = [
        "Checking backend connection...",
        "Initializing scrapers...",
        "Collecting data from platforms...",
        "Processing with AI models...",
        "Generating reports...",
        "Analysis complete!",
      ]

      for (let i = 0; i < steps.length - 1; i++) {
        setCurrentStep(steps[i])
        setProgress(((i + 1) / steps.length) * 100)
        await new Promise((resolve) => setTimeout(resolve, 1000))
      }

      console.log("Calling backend API...")

      // Call backend API
      const response = await fetch("/api/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(config),
      })

      console.log("Response status:", response.status)
      console.log("Response headers:", Object.fromEntries(response.headers.entries()))

      const responseData = await response.json()
      console.log("Response data:", responseData)

      if (response.ok) {
        setCurrentStep(steps[steps.length - 1])
        setProgress(100)
        setAnalysisResults(responseData)
        setAnalysisComplete(true)

        // Store investigation in localStorage
        const investigation = {
          id: responseData.investigationId,
          targetUser: config.username,
          platforms: config.platforms,
          aiModels: config.aiModels,
          exportFormats: config.exportFormats,
          status: "COMPLETED",
          createdAt: new Date().toISOString(),
          completedAt: new Date().toISOString(),
          results: responseData.results,
        }

        const stored = localStorage.getItem("osint_investigations")
        const investigations = stored ? JSON.parse(stored) : []
        investigations.unshift(investigation)
        localStorage.setItem("osint_investigations", JSON.stringify(investigations))

        toast({
          title: "Analysis Complete",
          description: `Successfully analyzed ${config.username} across ${config.platforms.length} platforms`,
        })
      } else {
        throw new Error(`Analysis failed: ${response.status}`)
      }
    } catch (error) {
      console.error("Analysis error:", error)

      let errorMessage = "An error occurred during analysis"
      let errorDetails = "Please try again"

      if (error instanceof TypeError && error.message.includes("fetch")) {
        errorMessage = "Cannot connect to backend"
        errorDetails = "Make sure the Python backend is running on port 8000"
      } else if (error instanceof Error) {
        errorMessage = error.message
      }

      setErrorDetails({
        error: errorMessage,
        details: errorDetails,
        timestamp: new Date().toISOString(),
      })

      toast({
        title: "Analysis Failed",
        description: errorMessage,
        variant: "destructive",
      })
    } finally {
      setIsAnalyzing(false)
      if (progress < 100) {
        setProgress(0)
        setCurrentStep("")
      }
    }
  }

  return (
    <div className="min-h-screen bg-black text-white relative">
      <MatrixBackground />

      {/* Header */}
      <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
        <div className="container mx-auto px-4 py-4 flex items-center justify-between">
          <Link href="/" className="flex items-center space-x-2">
            <Shield className="h-8 w-8 text-blue-400" />
            <span className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
              OSINT Platform
            </span>
          </Link>
          <nav className="flex items-center space-x-6">
            <Link href="/dashboard" className="hover:text-blue-400 transition-colors">
              Dashboard
            </Link>
            <Link href="/reports" className="hover:text-blue-400 transition-colors">
              Reports
            </Link>
            <Button
              variant="outline"
              size="sm"
              onClick={checkBackendStatus}
              className="border-blue-500/30 text-blue-400 bg-transparent"
            >
              Check Backend
            </Button>
          </nav>
        </div>
      </header>

      <div className="relative z-10 container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent mb-4">
              Intelligence Analysis
            </h1>
            <p className="text-gray-300 text-lg">Configure your OSINT investigation parameters</p>
          </div>

          {/* Backend Status Alert */}
          {backendStatus === "offline" && (
            <Alert className="mb-6 border-red-500/50 bg-red-900/20">
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>
                <div className="space-y-2">
                  <p className="font-semibold text-red-400">Backend Connection Failed</p>
                  {errorDetails && (
                    <div className="text-sm text-red-300">
                      <p>
                        <strong>Error:</strong> {errorDetails.error}
                      </p>
                      {errorDetails.details && (
                        <p>
                          <strong>Details:</strong> {errorDetails.details}
                        </p>
                      )}
                      {errorDetails.solution && (
                        <p>
                          <strong>Solution:</strong> {errorDetails.solution}
                        </p>
                      )}
                    </div>
                  )}
                </div>
              </AlertDescription>
            </Alert>
          )}

          {backendStatus === "online" && (
            <Alert className="mb-6 border-green-500/50 bg-green-900/20">
              <CheckCircle className="h-4 w-4" />
              <AlertDescription>
                <p className="font-semibold text-green-400">Backend Connected Successfully</p>
              </AlertDescription>
            </Alert>
          )}

          {/* Error Details */}
          {errorDetails && isAnalyzing === false && (
            <Alert className="mb-6 border-red-500/50 bg-red-900/20">
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>
                <div className="space-y-2">
                  <p className="font-semibold text-red-400">Analysis Error</p>
                  <div className="text-sm text-red-300">
                    <p>
                      <strong>Error:</strong> {errorDetails.error}
                    </p>
                    {errorDetails.details && (
                      <p>
                        <strong>Details:</strong> {errorDetails.details}
                      </p>
                    )}
                    {errorDetails.solution && (
                      <p>
                        <strong>Solution:</strong> {errorDetails.solution}
                      </p>
                    )}
                    {errorDetails.timestamp && (
                      <p>
                        <strong>Time:</strong> {new Date(errorDetails.timestamp).toLocaleString()}
                      </p>
                    )}
                  </div>
                </div>
              </AlertDescription>
            </Alert>
          )}

          {/* Success Message */}
          {analysisComplete && (
            <Alert className="mb-6 border-green-500/50 bg-green-900/20">
              <CheckCircle className="h-4 w-4" />
              <AlertDescription>
                <div className="space-y-3">
                  <p className="font-semibold text-green-400">Analysis Completed Successfully!</p>
                  <p className="text-sm text-green-300">
                    Successfully analyzed {config.username} across {config.platforms.length} platforms with{" "}
                    {config.aiModels.length} AI models.
                  </p>
                  <div className="flex flex-wrap gap-2">
                    <Button
                      onClick={() => window.open("/reports", "_blank")}
                      size="sm"
                      className="bg-green-600 hover:bg-green-700"
                    >
                      <Eye className="h-4 w-4 mr-2" />
                      View in Reports
                    </Button>
                    <Button
                      onClick={() => window.open("/dashboard/emotion-timeline", "_blank")}
                      size="sm"
                      className="bg-purple-600 hover:bg-purple-700"
                    >
                      <TrendingUp className="h-4 w-4 mr-2" />
                      Emotion Timeline
                    </Button>
                  </div>
                </div>
              </AlertDescription>
            </Alert>
          )}

          <div className="grid lg:grid-cols-3 gap-8">
            {/* Configuration Panel */}
            <div className="lg:col-span-2 space-y-6">
              {/* Target Configuration */}
              <Card className="bg-gray-900/50 border-blue-500/20">
                <CardHeader>
                  <CardTitle className="text-blue-400 flex items-center">
                    <Search className="mr-2 h-5 w-5" />
                    Target Configuration
                  </CardTitle>
                  <CardDescription>Specify the target username and investigation scope</CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div>
                    <Label htmlFor="username">Target Username</Label>
                    <Input
                      id="username"
                      placeholder="Enter username to investigate (e.g., octocat)"
                      value={config.username}
                      onChange={(e) => setConfig((prev) => ({ ...prev, username: e.target.value }))}
                      className="bg-gray-800 border-gray-700 text-white"
                    />
                  </div>
                </CardContent>
              </Card>

              {/* Platform Selection */}
              <Card className="bg-gray-900/50 border-blue-500/20">
                <CardHeader>
                  <CardTitle className="text-blue-400">Data Sources</CardTitle>
                  <CardDescription>Select platforms to gather intelligence from</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="grid sm:grid-cols-2 gap-4">
                    {platforms.map((platform) => (
                      <div
                        key={platform.id}
                        className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
                      >
                        <Checkbox
                          id={platform.id}
                          checked={config.platforms.includes(platform.id)}
                          onCheckedChange={() => handlePlatformToggle(platform.id)}
                        />
                        <div className="flex items-center space-x-2 flex-1">
                          <div className={`w-3 h-3 rounded-full ${platform.color}`} />
                          {platform.icon}
                          <Label htmlFor={platform.id} className="text-white cursor-pointer">
                            {platform.name}
                          </Label>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* AI Models */}
              <Card className="bg-gray-900/50 border-blue-500/20">
                <CardHeader>
                  <CardTitle className="text-blue-400 flex items-center">
                    <Brain className="mr-2 h-5 w-5" />
                    AI Analysis Models
                  </CardTitle>
                  <CardDescription>Choose AI models for content analysis</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {aiModels.map((model) => (
                      <div
                        key={model.id}
                        className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
                      >
                        <Checkbox
                          id={model.id}
                          checked={config.aiModels.includes(model.id)}
                          onCheckedChange={() => handleAIModelToggle(model.id)}
                        />
                        <div className="flex-1">
                          <Label htmlFor={model.id} className="text-white cursor-pointer font-medium">
                            {model.name}
                          </Label>
                          <p className="text-sm text-gray-400">{model.description}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Export Options */}
              <Card className="bg-gray-900/50 border-blue-500/20">
                <CardHeader>
                  <CardTitle className="text-blue-400 flex items-center">
                    <Download className="mr-2 h-5 w-5" />
                    Export Formats
                  </CardTitle>
                  <CardDescription>Select output formats for your analysis</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {exportFormats.map((format) => (
                      <div
                        key={format.id}
                        className="flex items-center space-x-3 p-3 rounded-lg border border-gray-700 hover:border-blue-500/50 transition-colors"
                      >
                        <Checkbox
                          id={format.id}
                          checked={config.exportFormats.includes(format.id)}
                          onCheckedChange={() => handleExportToggle(format.id)}
                        />
                        <div className="flex-1">
                          <Label htmlFor={format.id} className="text-white cursor-pointer font-medium">
                            {format.name}
                          </Label>
                          <p className="text-sm text-gray-400">{format.description}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Analysis Panel */}
            <div className="space-y-6">
              {/* Configuration Summary */}
              <Card className="bg-gray-900/50 border-blue-500/20">
                <CardHeader>
                  <CardTitle className="text-blue-400">Configuration Summary</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div>
                    <Label className="text-sm text-gray-400">Target</Label>
                    <p className="text-white font-mono">{config.username || "Not specified"}</p>
                  </div>

                  <div>
                    <Label className="text-sm text-gray-400">Platforms ({config.platforms.length})</Label>
                    <div className="flex flex-wrap gap-1 mt-1">
                      {config.platforms.map((platformId) => {
                        const platform = platforms.find((p) => p.id === platformId)
                        return platform ? (
                          <Badge key={platformId} variant="secondary" className="text-xs">
                            {platform.name}
                          </Badge>
                        ) : null
                      })}
                    </div>
                  </div>

                  <div>
                    <Label className="text-sm text-gray-400">AI Models ({config.aiModels.length})</Label>
                    <div className="flex flex-wrap gap-1 mt-1">
                      {config.aiModels.map((modelId) => {
                        const model = aiModels.find((m) => m.id === modelId)
                        return model ? (
                          <Badge key={modelId} variant="outline" className="text-xs border-blue-500/30 text-blue-300">
                            {model.name}
                          </Badge>
                        ) : null
                      })}
                    </div>
                  </div>

                  <div>
                    <Label className="text-sm text-gray-400">Export Formats ({config.exportFormats.length})</Label>
                    <div className="flex flex-wrap gap-1 mt-1">
                      {config.exportFormats.map((formatId) => {
                        const format = exportFormats.find((f) => f.id === formatId)
                        return format ? (
                          <Badge
                            key={formatId}
                            variant="outline"
                            className="text-xs border-green-500/30 text-green-300"
                          >
                            {format.name}
                          </Badge>
                        ) : null
                      })}
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Analysis Control */}
              <Card className="bg-gray-900/50 border-blue-500/20">
                <CardHeader>
                  <CardTitle className="text-blue-400">Analysis Control</CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  {isAnalyzing ? (
                    <div className="space-y-4">
                      <div className="flex items-center space-x-2">
                        <Loader2 className="h-4 w-4 animate-spin text-blue-400" />
                        <span className="text-sm text-gray-300">{currentStep}</span>
                      </div>
                      <Progress value={progress} className="w-full" />
                      <p className="text-xs text-gray-400 text-center">{Math.round(progress)}% Complete</p>
                    </div>
                  ) : (
                    <Button
                      onClick={startAnalysis}
                      className="w-full bg-blue-600 hover:bg-blue-700 text-white cyber-glow"
                      size="lg"
                      disabled={backendStatus === "offline"}
                    >
                      <Play className="mr-2 h-4 w-4" />
                      {backendStatus === "offline" ? "Backend Offline" : "Start Analysis"}
                    </Button>
                  )}
                </CardContent>
              </Card>

              {/* Legal Notice */}
              <Card className="bg-yellow-900/20 border-yellow-500/20">
                <CardContent className="pt-6">
                  <div className="flex items-start space-x-2">
                    <Shield className="h-5 w-5 text-yellow-400 mt-0.5 flex-shrink-0" />
                    <div>
                      <p className="text-sm text-yellow-200 font-medium mb-1">Ethical Use Only</p>
                      <p className="text-xs text-yellow-300/80">
                        This tool is designed for ethical research, journalism, and cybersecurity audits. Only public,
                        non-authenticated data is collected.
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
