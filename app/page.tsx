// import { MatrixBackground } from "@/components/matrix-background"
// import { Button } from "@/components/ui/button"
// import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
// import { Badge } from "@/components/ui/badge"
// import Link from "next/link"
// import {
//   Shield,
//   Search,
//   Brain,
//   Database,
//   FileText,
//   Github,
//   MessageSquare,
//   Camera,
//   Newspaper,
//   BarChart3,
//   Download,
//   Eye,
//   Zap,
// } from "lucide-react"

// export default function HomePage() {
//   const features = [
//     {
//       icon: <Search className="h-8 w-8" />,
//       title: "Multi-Platform OSINT",
//       description: "Gather intelligence from Reddit, Twitter/X, GitHub, Instagram, and news sources",
//       platforms: ["Reddit", "Twitter/X", "GitHub", "Instagram", "News"],
//     },
//     {
//       icon: <Brain className="h-8 w-8" />,
//       title: "AI-Powered Analysis",
//       description: "Advanced sentiment analysis, NER, toxicity detection using Hugging Face models",
//       platforms: ["Sentiment", "NER", "Toxicity", "Summarization"],
//     },
//     {
//       icon: <BarChart3 className="h-8 w-8" />,
//       title: "Visual Intelligence",
//       description: "Interactive dashboards, word clouds, timeline analysis, and network graphs",
//       platforms: ["Dashboards", "Word Clouds", "Timelines", "Networks"],
//     },
//     {
//       icon: <Download className="h-8 w-8" />,
//       title: "Export & Reporting",
//       description: "Generate comprehensive reports in CSV and PDF formats",
//       platforms: ["CSV Export", "PDF Reports", "Raw Data", "Analytics"],
//     },
//   ]

//   const platforms = [
//     { name: "Reddit", icon: <MessageSquare className="h-6 w-6" />, color: "bg-orange-500" },
//     { name: "Twitter/X", icon: <MessageSquare className="h-6 w-6" />, color: "bg-blue-500" },
//     { name: "GitHub", icon: <Github className="h-6 w-6" />, color: "bg-gray-500" },
//     { name: "Instagram", icon: <Camera className="h-6 w-6" />, color: "bg-pink-500" },
//     { name: "News Sites", icon: <Newspaper className="h-6 w-6" />, color: "bg-green-500" },
//   ]

//   return (
//     <div className="min-h-screen bg-black text-white relative overflow-hidden">
//       <MatrixBackground />

//       {/* Header */}
//       <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
//         <div className="container mx-auto px-4 py-4 flex items-center justify-between">
//           <div className="flex items-center space-x-2">
//             <Shield className="h-8 w-8 text-blue-400" />
//             <span className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
//               OSINT Platform
//             </span>
//           </div>
//           <nav className="hidden md:flex items-center space-x-6">
//             <Link href="/analyze" className="hover:text-blue-400 transition-colors">
//               Analyze
//             </Link>
//             <Link href="/dashboard" className="hover:text-blue-400 transition-colors">
//               Dashboard
//             </Link>
//             <Link href="/reports" className="hover:text-blue-400 transition-colors">
//               Reports
//             </Link>
//           </nav>
//         </div>
//       </header>

//       {/* Hero Section */}
//       <section className="relative z-10 py-20 px-4">
//         <div className="container mx-auto text-center">
//           <div className="cyber-glow inline-block p-1 rounded-lg mb-8">
//             <h1 className="text-6xl md:text-8xl font-bold bg-gradient-to-r from-blue-400 via-cyan-400 to-blue-600 bg-clip-text text-transparent">
//               AI-POWERED
//             </h1>
//             <h2 className="text-4xl md:text-6xl font-bold text-white mt-2">OSINT PLATFORM</h2>
//           </div>

//           <p className="text-xl md:text-2xl text-gray-300 mb-8 max-w-4xl mx-auto">
//             Advanced Open Source Intelligence gathering and analysis for ethical research, journalism, and cybersecurity
//             audits in India 🇮🇳
//           </p>

//           <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
//             <Link href="/analyze">
//               <Button size="lg" className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 text-lg cyber-glow">
//                 <Zap className="mr-2 h-5 w-5" />
//                 Start Investigation
//               </Button>
//             </Link>
//             <Link href="/dashboard">
//               <Button
//                 size="lg"
//                 variant="outline"
//                 className="border-blue-500 text-blue-400 hover:bg-blue-500/10 px-8 py-4 text-lg bg-transparent"
//               >
//                 <Eye className="mr-2 h-5 w-5" />
//                 View Dashboard
//               </Button>
//             </Link>
//           </div>

//           {/* Platform Badges */}
//           <div className="flex flex-wrap justify-center gap-3 mb-16">
//             {platforms.map((platform) => (
//               <Badge key={platform.name} variant="secondary" className="px-4 py-2 text-sm">
//                 <div className={`w-3 h-3 rounded-full ${platform.color} mr-2`} />
//                 {platform.name}
//               </Badge>
//             ))}
//           </div>
//         </div>
//       </section>

//       {/* Features Section */}
//       <section className="relative z-10 py-20 px-4 bg-gradient-to-b from-transparent to-blue-950/20">
//         <div className="container mx-auto">
//           <h3 className="text-4xl font-bold text-center mb-16 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
//             Platform Capabilities
//           </h3>

//           <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
//             {features.map((feature, index) => (
//               <Card
//                 key={index}
//                 className="bg-gray-900/50 border-blue-500/20 hover:border-blue-400/40 transition-all duration-300 scan-effect"
//               >
//                 <CardHeader>
//                   <div className="text-blue-400 mb-4">{feature.icon}</div>
//                   <CardTitle className="text-white">{feature.title}</CardTitle>
//                   <CardDescription className="text-gray-300">{feature.description}</CardDescription>
//                 </CardHeader>
//                 <CardContent>
//                   <div className="flex flex-wrap gap-2">
//                     {feature.platforms.map((platform) => (
//                       <Badge key={platform} variant="outline" className="text-xs border-blue-500/30 text-blue-300">
//                         {platform}
//                       </Badge>
//                     ))}
//                   </div>
//                 </CardContent>
//               </Card>
//             ))}
//           </div>
//         </div>
//       </section>

//       {/* Technical Specs */}
//       <section className="relative z-10 py-20 px-4">
//         <div className="container mx-auto">
//           <div className="grid md:grid-cols-3 gap-8">
//             <Card className="bg-gray-900/50 border-blue-500/20">
//               <CardHeader>
//                 <CardTitle className="text-blue-400 flex items-center">
//                   <Database className="mr-2 h-5 w-5" />
//                   Data Sources
//                 </CardTitle>
//               </CardHeader>
//               <CardContent className="space-y-2">
//                 <div className="text-sm text-gray-300">• Reddit API (praw)</div>
//                 <div className="text-sm text-gray-300">• Twitter/X Scraper (snscrape)</div>
//                 <div className="text-sm text-gray-300">• GitHub API (PyGithub)</div>
//                 <div className="text-sm text-gray-300">• Instagram Scraper (instaloader)</div>
//                 <div className="text-sm text-gray-300">• News Sites (newspaper3k)</div>
//               </CardContent>
//             </Card>

//             <Card className="bg-gray-900/50 border-blue-500/20">
//               <CardHeader>
//                 <CardTitle className="text-blue-400 flex items-center">
//                   <Brain className="mr-2 h-5 w-5" />
//                   AI Models
//                 </CardTitle>
//               </CardHeader>
//               <CardContent className="space-y-2">
//                 <div className="text-sm text-gray-300">• Sentiment Analysis (DistilBERT)</div>
//                 <div className="text-sm text-gray-300">• Named Entity Recognition</div>
//                 <div className="text-sm text-gray-300">• Toxicity Detection (ToxicBERT)</div>
//                 <div className="text-sm text-gray-300">• Content Summarization (Gemini)</div>
//                 <div className="text-sm text-gray-300">• Language Translation (mBART)</div>
//               </CardContent>
//             </Card>

//             <Card className="bg-gray-900/50 border-blue-500/20">
//               <CardHeader>
//                 <CardTitle className="text-blue-400 flex items-center">
//                   <FileText className="mr-2 h-5 w-5" />
//                   Export Formats
//                 </CardTitle>
//               </CardHeader>
//               <CardContent className="space-y-2">
//                 <div className="text-sm text-gray-300">• CSV Data Export</div>
//                 <div className="text-sm text-gray-300">• PDF Reports</div>
//                 <div className="text-sm text-gray-300">• JSON Raw Data</div>
//                 <div className="text-sm text-gray-300">• Interactive Dashboards</div>
//                 <div className="text-sm text-gray-300">• Visual Analytics</div>
//               </CardContent>
//             </Card>
//           </div>
//         </div>
//       </section>

//       {/* CTA Section */}
//       <section className="relative z-10 py-20 px-4 bg-gradient-to-t from-blue-950/30 to-transparent">
//         <div className="container mx-auto text-center">
//           <h3 className="text-4xl font-bold mb-8 text-white">Ready to Start Your Investigation?</h3>
//           <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
//             Ethical OSINT for research, journalism, and cybersecurity professionals
//           </p>
//           <Link href="/analyze">
//             <Button
//               size="lg"
//               className="bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-700 hover:to-cyan-700 text-white px-12 py-4 text-lg cyber-glow"
//             >
//               <Search className="mr-2 h-5 w-5" />
//               Begin Analysis
//             </Button>
//           </Link>
//         </div>
//       </section>

//       {/* Footer */}
//       <footer className="relative z-10 border-t border-blue-500/20 bg-black/50 backdrop-blur-sm py-8">
//         <div className="container mx-auto px-4 text-center text-gray-400">
//           <p className="mb-2">🇮🇳 AI-Based Human OSINT Platform for India</p>
//           <p className="text-sm">Ethical intelligence gathering • Public data only • Research & journalism use</p>
//         </div>
//       </footer>
//     </div>
//   )
// }




"use client"

import { useState } from "react"
import Link from "next/link"
import { MatrixBackground } from "@/components/matrix-background"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import {
  Search,
  BarChart3,
  FileText,
  Settings,
  Shield,
  TrendingUp,
  Camera,
  Brain,
  Eye,
  Globe,
  Zap,
  Target,
} from "lucide-react"

export default function HomePage() {
  const [hoveredCard, setHoveredCard] = useState<string | null>(null)

  const features = [
    {
      id: "analyze",
      title: "🔍 Multi-Platform Analysis",
      description: "Comprehensive OSINT analysis across Twitter, Reddit, GitHub, Instagram, and News sources",
      icon: Search,
      href: "/analyze",
      color: "from-blue-500 to-cyan-500",
      stats: "5+ Platforms",
    },
    {
      id: "facial",
      title: "🧠 AI Facial Recognition",
      description: "Upload images to identify famous personalities and analyze their digital footprint",
      icon: Camera,
      href: "/facial-recognition",
      color: "from-purple-500 to-pink-500",
      stats: "AI-Powered",
      badge: "NEW",
    },
    {
      id: "dashboard",
      title: "📊 Analytics Dashboard",
      description: "Real-time insights, sentiment analysis, and behavioral pattern detection",
      icon: BarChart3,
      href: "/dashboard",
      color: "from-green-500 to-emerald-500",
      stats: "Real-time",
    },
    {
      id: "timeline",
      title: "📈 Emotion Timeline",
      description: "Track emotional patterns and behavioral changes over time with AI analysis",
      icon: TrendingUp,
      href: "/dashboard/emotion-timeline",
      color: "from-orange-500 to-red-500",
      stats: "AI Analysis",
    },
    {
      id: "reports",
      title: "📄 Intelligence Reports",
      description: "Generate comprehensive PDF reports with findings and risk assessments",
      icon: FileText,
      href: "/reports",
      color: "from-indigo-500 to-purple-500",
      stats: "PDF Export",
    },
    {
      id: "troubleshoot",
      title: "🔧 System Diagnostics",
      description: "Test scrapers, AI models, and system components for optimal performance",
      icon: Settings,
      href: "/troubleshoot",
      color: "from-gray-500 to-slate-500",
      stats: "Diagnostics",
    },
  ]

  const capabilities = [
    {
      icon: Brain,
      title: "AI-Powered Analysis",
      description: "Advanced machine learning models for sentiment, toxicity, and behavioral analysis",
    },
    {
      icon: Eye,
      title: "Facial Recognition",
      description: "Identify famous personalities and analyze their social media presence",
    },
    {
      icon: Shield,
      title: "Risk Assessment",
      description: "Automated threat detection and security risk evaluation",
    },
    {
      icon: Globe,
      title: "Multi-Platform",
      description: "Comprehensive coverage across major social media platforms",
    },
    {
      icon: Zap,
      title: "Real-Time Processing",
      description: "Live data collection and instant analysis capabilities",
    },
    {
      icon: Target,
      title: "Precision Targeting",
      description: "Focused investigation tools for specific users and topics",
    },
  ]

  return (
    <div className="min-h-screen bg-black text-white relative overflow-hidden">
      <MatrixBackground />

      {/* Hero Section */}
      <section className="relative z-10 min-h-screen flex items-center justify-center">
        <div className="container mx-auto px-4 text-center">
          <div className="max-w-4xl mx-auto">
            <div className="mb-8">
              <Badge className="mb-4 bg-blue-600/20 text-blue-300 border-blue-500/30">
                🚀 Advanced OSINT Platform v2.0
              </Badge>
              <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-blue-400 via-cyan-400 to-purple-400 bg-clip-text text-transparent">
                AI-Powered OSINT Intelligence
              </h1>
              <p className="text-xl md:text-2xl text-gray-300 mb-8 leading-relaxed">
                Advanced Open Source Intelligence platform with facial recognition, multi-platform analysis, and
                AI-driven insights for comprehensive digital investigations.
              </p>
            </div>

            <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
              <Link href="/analyze">
                <Button size="lg" className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3">
                  <Search className="mr-2 h-5 w-5" />
                  Start Investigation
                </Button>
              </Link>
              <Link href="/facial-recognition">
                <Button
                  size="lg"
                  variant="outline"
                  className="border-purple-500 text-purple-300 hover:bg-purple-500/10 px-8 py-3 bg-transparent"
                >
                  <Camera className="mr-2 h-5 w-5" />
                  Try Facial Recognition
                </Button>
              </Link>
            </div>

            {/* Quick Stats */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-2xl mx-auto">
              <div className="p-4 bg-gray-900/50 rounded-lg border border-gray-700/50">
                <div className="text-2xl font-bold text-blue-400">5+</div>
                <div className="text-sm text-gray-400">Platforms</div>
              </div>
              <div className="p-4 bg-gray-900/50 rounded-lg border border-gray-700/50">
                <div className="text-2xl font-bold text-green-400">AI</div>
                <div className="text-sm text-gray-400">Powered</div>
              </div>
              <div className="p-4 bg-gray-900/50 rounded-lg border border-gray-700/50">
                <div className="text-2xl font-bold text-purple-400">Real-time</div>
                <div className="text-sm text-gray-400">Analysis</div>
              </div>
              <div className="p-4 bg-gray-900/50 rounded-lg border border-gray-700/50">
                <div className="text-2xl font-bold text-orange-400">24/7</div>
                <div className="text-sm text-gray-400">Monitoring</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="relative z-10 py-20">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold mb-4 bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
              🛠️ Platform Features
            </h2>
            <p className="text-xl text-gray-400 max-w-2xl mx-auto">
              Comprehensive suite of OSINT tools powered by advanced AI and machine learning
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((feature) => {
              const Icon = feature.icon
              return (
                <Link key={feature.id} href={feature.href}>
                  <Card
                    className={`bg-gray-900/50 border-gray-700 hover:border-gray-600 transition-all duration-300 cursor-pointer h-full ${
                      hoveredCard === feature.id ? "transform scale-105 shadow-2xl" : ""
                    }`}
                    onMouseEnter={() => setHoveredCard(feature.id)}
                    onMouseLeave={() => setHoveredCard(null)}
                  >
                    <CardHeader>
                      <div className="flex items-center justify-between mb-2">
                        <div className={`p-3 rounded-lg bg-gradient-to-r ${feature.color} bg-opacity-20`}>
                          <Icon className="h-6 w-6 text-white" />
                        </div>
                        <div className="flex gap-2">
                          {feature.badge && (
                            <Badge className="bg-green-600/20 text-green-300 border-green-500/30 text-xs">
                              {feature.badge}
                            </Badge>
                          )}
                          <Badge variant="outline" className="border-gray-600 text-gray-300 text-xs">
                            {feature.stats}
                          </Badge>
                        </div>
                      </div>
                      <CardTitle className="text-white text-lg">{feature.title}</CardTitle>
                      <CardDescription className="text-gray-400">{feature.description}</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <div className="flex items-center text-sm text-blue-400 hover:text-blue-300">
                        Launch Tool
                        <Search className="ml-2 h-4 w-4" />
                      </div>
                    </CardContent>
                  </Card>
                </Link>
              )
            })}
          </div>
        </div>
      </section>

      {/* Capabilities Section */}
      <section className="relative z-10 py-20 bg-gray-900/30">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold mb-4 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
              🎯 Core Capabilities
            </h2>
            <p className="text-xl text-gray-400 max-w-2xl mx-auto">
              Advanced intelligence gathering and analysis capabilities
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {capabilities.map((capability, index) => {
              const Icon = capability.icon
              return (
                <div key={index} className="text-center p-6">
                  <div className="mb-4">
                    <div className="inline-flex p-4 rounded-full bg-gradient-to-r from-blue-500/20 to-purple-500/20 border border-blue-500/30">
                      <Icon className="h-8 w-8 text-blue-400" />
                    </div>
                  </div>
                  <h3 className="text-xl font-semibold text-white mb-2">{capability.title}</h3>
                  <p className="text-gray-400">{capability.description}</p>
                </div>
              )
            })}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative z-10 py-20">
        <div className="container mx-auto px-4 text-center">
          <div className="max-w-3xl mx-auto">
            <h2 className="text-4xl font-bold mb-6 bg-gradient-to-r from-green-400 to-blue-400 bg-clip-text text-transparent">
              🚀 Ready to Start Your Investigation?
            </h2>
            <p className="text-xl text-gray-300 mb-8">
              Begin your OSINT analysis with our advanced AI-powered platform
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link href="/analyze">
                <Button size="lg" className="bg-green-600 hover:bg-green-700 text-white px-8 py-3">
                  <Target className="mr-2 h-5 w-5" />
                  Start Multi-Platform Analysis
                </Button>
              </Link>
              <Link href="/facial-recognition">
                <Button
                  size="lg"
                  variant="outline"
                  className="border-purple-500 text-purple-300 hover:bg-purple-500/10 px-8 py-3 bg-transparent"
                >
                  <Brain className="mr-2 h-5 w-5" />
                  Try Facial Recognition
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="relative z-10 border-t border-gray-800 py-8">
        <div className="container mx-auto px-4 text-center">
          <p className="text-gray-400">
            © 2024 AI-Powered OSINT Platform. Advanced intelligence gathering and analysis.
          </p>
        </div>
      </footer>
    </div>
  )
}
