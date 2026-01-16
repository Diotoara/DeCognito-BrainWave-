"use client"

import { useState, useEffect } from "react"
import { MatrixBackground } from "@/components/matrix-background"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Progress } from "@/components/ui/progress"
import Link from "next/link"
import {
  Shield,
  Search,
  BarChart3,
  Clock,
  CheckCircle,
  XCircle,
  AlertCircle,
  Download,
  Eye,
  Trash2,
  RefreshCw,
} from "lucide-react"

interface Investigation {
  id: string
  targetUser: string
  platforms: string[]
  status: "PENDING" | "IN_PROGRESS" | "COMPLETED" | "FAILED"
  createdAt: string
  completedAt?: string
  results?: any
}

export default function DashboardPage() {
  const [investigations, setInvestigations] = useState<Investigation[]>([])
  const [loading, setLoading] = useState(true)
  const [stats, setStats] = useState({
    total: 0,
    completed: 0,
    pending: 0,
    failed: 0,
  })

  useEffect(() => {
    loadInvestigations()
  }, [])

  const loadInvestigations = async () => {
    try {
      // For now, load from localStorage since we don't have database
      const stored = localStorage.getItem("osint_investigations")
      if (stored) {
        const data = JSON.parse(stored)
        setInvestigations(data)

        // Calculate stats
        const stats = data.reduce(
          (acc: any, inv: Investigation) => {
            acc.total++
            acc[inv.status.toLowerCase()]++
            return acc
          },
          { total: 0, completed: 0, pending: 0, failed: 0, in_progress: 0 },
        )

        setStats(stats)
      }
    } catch (error) {
      console.error("Failed to load investigations:", error)
    } finally {
      setLoading(false)
    }
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case "COMPLETED":
        return <CheckCircle className="h-4 w-4 text-green-400" />
      case "FAILED":
        return <XCircle className="h-4 w-4 text-red-400" />
      case "IN_PROGRESS":
        return <RefreshCw className="h-4 w-4 text-blue-400 animate-spin" />
      default:
        return <Clock className="h-4 w-4 text-yellow-400" />
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case "COMPLETED":
        return "bg-green-500/20 text-green-400 border-green-500/30"
      case "FAILED":
        return "bg-red-500/20 text-red-400 border-red-500/30"
      case "IN_PROGRESS":
        return "bg-blue-500/20 text-blue-400 border-blue-500/30"
      default:
        return "bg-yellow-500/20 text-yellow-400 border-yellow-500/30"
    }
  }

  const deleteInvestigation = (id: string) => {
    const updated = investigations.filter((inv) => inv.id !== id)
    setInvestigations(updated)
    localStorage.setItem("osint_investigations", JSON.stringify(updated))
    loadInvestigations() // Refresh stats
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
            <Link href="/analyze" className="hover:text-blue-400 transition-colors">
              Analyze
            </Link>
            <Link href="/reports" className="hover:text-blue-400 transition-colors">
              Reports
            </Link>
          </nav>
        </div>
      </header>

      <div className="relative z-10 container mx-auto px-4 py-8">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent mb-4">
              Investigation Dashboard
            </h1>
            <p className="text-gray-300 text-lg">Monitor and manage your OSINT investigations</p>
          </div>

          {/* Stats Cards */}
          <div className="grid md:grid-cols-4 gap-6 mb-8">
            <Card className="bg-gray-900/50 border-blue-500/20">
              <CardHeader className="pb-2">
                <CardTitle className="text-blue-400 flex items-center text-sm">
                  <BarChart3 className="mr-2 h-4 w-4" />
                  Total Investigations
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">{stats.total}</div>
              </CardContent>
            </Card>

            <Card className="bg-gray-900/50 border-green-500/20">
              <CardHeader className="pb-2">
                <CardTitle className="text-green-400 flex items-center text-sm">
                  <CheckCircle className="mr-2 h-4 w-4" />
                  Completed
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">{stats.completed}</div>
              </CardContent>
            </Card>

            <Card className="bg-gray-900/50 border-yellow-500/20">
              <CardHeader className="pb-2">
                <CardTitle className="text-yellow-400 flex items-center text-sm">
                  <Clock className="mr-2 h-4 w-4" />
                  Pending
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">{stats.pending + (stats as any).in_progress}</div>
              </CardContent>
            </Card>

            <Card className="bg-gray-900/50 border-red-500/20">
              <CardHeader className="pb-2">
                <CardTitle className="text-red-400 flex items-center text-sm">
                  <XCircle className="mr-2 h-4 w-4" />
                  Failed
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-white">{stats.failed}</div>
              </CardContent>
            </Card>
          </div>

          {/* Quick Actions */}
          <div className="flex flex-wrap gap-4 mb-8">
            <Link href="/analyze">
              <Button className="bg-blue-600 hover:bg-blue-700 text-white">
                <Search className="mr-2 h-4 w-4" />
                New Investigation
              </Button>
            </Link>
            <Button
              variant="outline"
              onClick={loadInvestigations}
              className="border-blue-500/30 text-blue-400 bg-transparent"
            >
              <RefreshCw className="mr-2 h-4 w-4" />
              Refresh
            </Button>
          </div>

          {/* Investigations List */}
          <Card className="bg-gray-900/50 border-blue-500/20">
            <CardHeader>
              <CardTitle className="text-blue-400">Recent Investigations</CardTitle>
              <CardDescription>Track the progress of your OSINT investigations</CardDescription>
            </CardHeader>
            <CardContent>
              {loading ? (
                <div className="text-center py-8">
                  <RefreshCw className="h-8 w-8 animate-spin text-blue-400 mx-auto mb-4" />
                  <p className="text-gray-400">Loading investigations...</p>
                </div>
              ) : investigations.length === 0 ? (
                <div className="text-center py-8">
                  <AlertCircle className="h-8 w-8 text-gray-400 mx-auto mb-4" />
                  <p className="text-gray-400 mb-4">No investigations found</p>
                  <Link href="/analyze">
                    <Button className="bg-blue-600 hover:bg-blue-700">
                      <Search className="mr-2 h-4 w-4" />
                      Start Your First Investigation
                    </Button>
                  </Link>
                </div>
              ) : (
                <div className="space-y-4">
                  {investigations.map((investigation) => (
                    <div
                      key={investigation.id}
                      className="border border-gray-700 rounded-lg p-4 hover:border-blue-500/50 transition-colors"
                    >
                      <div className="flex items-center justify-between mb-3">
                        <div className="flex items-center space-x-3">
                          {getStatusIcon(investigation.status)}
                          <div>
                            <h3 className="font-semibold text-white">Investigation: {investigation.targetUser}</h3>
                            <p className="text-sm text-gray-400">ID: {investigation.id}</p>
                          </div>
                        </div>
                        <div className="flex items-center space-x-2">
                          <Badge className={getStatusColor(investigation.status)}>{investigation.status}</Badge>
                          <Button
                            size="sm"
                            variant="ghost"
                            onClick={() => deleteInvestigation(investigation.id)}
                            className="text-red-400 hover:text-red-300 hover:bg-red-500/10"
                          >
                            <Trash2 className="h-4 w-4" />
                          </Button>
                        </div>
                      </div>

                      <div className="grid md:grid-cols-3 gap-4 text-sm">
                        <div>
                          <span className="text-gray-400">Target:</span>
                          <p className="text-white font-mono">{investigation.targetUser}</p>
                        </div>
                        <div>
                          <span className="text-gray-400">Platforms:</span>
                          <div className="flex flex-wrap gap-1 mt-1">
                            {investigation.platforms?.map((platform) => (
                              <Badge key={platform} variant="secondary" className="text-xs">
                                {platform}
                              </Badge>
                            ))}
                          </div>
                        </div>
                        <div>
                          <span className="text-gray-400">Created:</span>
                          <p className="text-white">{new Date(investigation.createdAt).toLocaleDateString()}</p>
                        </div>
                      </div>

                      {investigation.status === "IN_PROGRESS" && (
                        <div className="mt-4">
                          <div className="flex items-center justify-between mb-2">
                            <span className="text-sm text-gray-400">Progress</span>
                            <span className="text-sm text-blue-400">Processing...</span>
                          </div>
                          <Progress value={65} className="w-full" />
                        </div>
                      )}

                      {investigation.status === "COMPLETED" && (
                        <div className="mt-4 flex space-x-2">
                          <Button
                            size="sm"
                            variant="outline"
                            className="border-blue-500/30 text-blue-400 bg-transparent"
                          >
                            <Eye className="mr-2 h-3 w-3" />
                            View Results
                          </Button>
                          <Button
                            size="sm"
                            variant="outline"
                            className="border-green-500/30 text-green-400 bg-transparent"
                          >
                            <Download className="mr-2 h-3 w-3" />
                            Export
                          </Button>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}
