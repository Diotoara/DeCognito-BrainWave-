"use client";

import type React from "react";
import { useState, useRef } from "react";
import { MatrixBackground } from "@/components/matrix-background";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { Separator } from "@/components/ui/separator";
import {
  Upload,
  Camera,
  ExternalLink,
  Download,
  AlertTriangle,
  CheckCircle,
  Clock,
  Eye,
  Search,
  FileText,
  Users,
  TrendingUp,
} from "lucide-react";
import Image from "next/image";

interface IdentifiedPerson {
  name: string;
  description: string;
  confidence: number;
  method: string;
}

interface SocialProfile {
  [platform: string]: string[];
}

interface NewsArticle {
  title: string;
  description: string;
  url: string;
  source: string;
  published_at: string;
  image?: string;
}

interface TimelineEvent {
  date: string;
  title: string;
  description: string;
  significance: string;
}

interface AnalysisResult {
  status: string;
  identified_person?: IdentifiedPerson;
  social_media_profiles?: SocialProfile;
  news_articles?: NewsArticle[];
  ai_summary?: any;
  comprehensive_report?: any;
  pdf_report_base64?: string;
  analysis_metadata?: any;
  error?: string;
}

export default function FacialRecognitionPage() {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(
    null
  );
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [currentStep, setCurrentStep] = useState("");
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setSelectedImage(e.target?.result as string);
        setAnalysisResult(null);
      };
      reader.readAsDataURL(file);
    }
  };

  const analyzeImage = async () => {
    if (!selectedImage) return;

    setLoading(true);
    setProgress(0);
    setCurrentStep("Initializing analysis...");

    try {
      // Simulate progress steps
      const steps = [
        "Analyzing facial features...",
        "Identifying person...",
        "Verifying person status...",
        "Searching official profiles...",
        "Fetching news articles...",
        "Generating AI summary...",
        "Creating comprehensive report...",
      ];

      for (let i = 0; i < steps.length; i++) {
        setCurrentStep(steps[i]);
        setProgress((i + 1) * 14.28); // 100 / 7 steps
        await new Promise((resolve) => setTimeout(resolve, 800));
      }

      const response = await fetch("/api/facial-recognition", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          image_data: selectedImage,
          search_platforms: ["twitter", "instagram", "linkedin", "facebook"],
        }),
      });

      const data = await response.json();
      setAnalysisResult(data);
      setProgress(100);
      setCurrentStep("Analysis complete!");
    } catch (error) {
      console.error("Analysis failed:", error);
      setAnalysisResult({
        status: "error",
        error: "Analysis failed. Please try again.",
      });
    } finally {
      setLoading(false);
    }
  };

  const downloadReport = (format: "json" | "pdf") => {
    if (!analysisResult) return;

    if (format === "json" && analysisResult.comprehensive_report) {
      const reportData = JSON.stringify(
        analysisResult.comprehensive_report,
        null,
        2
      );
      const blob = new Blob([reportData], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `osint_report_${analysisResult.comprehensive_report.report_id}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } else if (format === "pdf" && analysisResult.pdf_report_base64) {
      const link = document.createElement("a");
      link.href = `data:application/pdf;base64,${analysisResult.pdf_report_base64}`;
      link.download = `osint_report_${
        analysisResult.comprehensive_report?.report_id || "report"
      }.pdf`;
      link.click();
    }
  };

  const getRiskColor = (level: string) => {
    switch (level?.toLowerCase()) {
      case "low":
        return "text-green-400";
      case "medium":
        return "text-yellow-400";
      case "high":
        return "text-red-400";
      case "critical":
        return "text-red-600";
      default:
        return "text-gray-400";
    }
  };

  return (
    <div className="min-h-screen bg-black text-white relative">
      <MatrixBackground />

      {/* Header */}
      <header className="relative z-10 border-b border-blue-500/20 bg-black/50 backdrop-blur-sm">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">
                🧠 AI-Based Facial Recognition OSINT
              </h1>
              <p className="text-gray-400 mt-2">
                Upload an image to identify famous personalities and analyze
                their digital footprint
              </p>
            </div>
            <div className="flex gap-2">
              <Button
                onClick={() => fileInputRef.current?.click()}
                className="bg-blue-600 hover:bg-blue-700"
              >
                <Upload className="h-4 w-4 mr-2" />
                Upload Image
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="relative z-10 container mx-auto px-4 py-8">
        {/* Upload Section */}
        <Card className="bg-gray-900/50 border-gray-700 mb-8">
          <CardHeader>
            <CardTitle className="text-white flex items-center gap-2">
              <Camera className="h-5 w-5" />
              📸 Image Upload & Analysis
            </CardTitle>
            <CardDescription className="text-gray-400">
              Upload a clear image of a famous personality for identification
              and analysis
            </CardDescription>
          </CardHeader>
          <CardContent>
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handleImageUpload}
              className="hidden"
            />

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Image Preview */}
              <div className="space-y-4">
                <div className="border-2 border-dashed border-gray-600 rounded-lg p-8 text-center">
                  {selectedImage ? (
                    <div className="space-y-4">
                      <div className="relative w-full h-64 mx-auto">
                        <Image
                          src={selectedImage || "/placeholder.svg"}
                          alt="Uploaded image"
                          fill
                          className="object-contain rounded-lg"
                        />
                      </div>
                      <div className="flex gap-2 justify-center">
                        <Button
                          onClick={() => fileInputRef.current?.click()}
                          variant="outline"
                          className="border-gray-600"
                        >
                          <Upload className="h-4 w-4 mr-2" />
                          Change Image
                        </Button>
                        <Button
                          onClick={analyzeImage}
                          disabled={loading}
                          className="bg-green-600 hover:bg-green-700"
                        >
                          <Search className="h-4 w-4 mr-2" />
                          {loading ? "Analyzing..." : "Analyze Image"}
                        </Button>
                      </div>
                    </div>
                  ) : (
                    <div className="space-y-4">
                      <Camera className="h-16 w-16 mx-auto text-gray-400" />
                      <div>
                        <p className="text-gray-300 mb-2">
                          Upload an image to get started
                        </p>
                        <p className="text-sm text-gray-500">
                          Supports JPG, PNG, and other image formats
                        </p>
                      </div>
                      <Button
                        onClick={() => fileInputRef.current?.click()}
                        className="bg-blue-600 hover:bg-blue-700"
                      >
                        <Upload className="h-4 w-4 mr-2" />
                        Choose Image
                      </Button>
                    </div>
                  )}
                </div>
              </div>

              {/* Analysis Progress */}
              <div className="space-y-4">
                <h3 className="text-lg font-semibold text-white">
                  Analysis Progress
                </h3>

                {loading && (
                  <div className="space-y-3">
                    <Progress value={progress} className="w-full" />
                    <div className="flex items-center gap-2 text-sm text-gray-300">
                      <Clock className="h-4 w-4 animate-spin" />
                      {currentStep}
                    </div>
                  </div>
                )}

                <div className="space-y-2">
                  <div className="flex items-center gap-2 text-sm">
                    <div
                      className={`w-2 h-2 rounded-full ${
                        selectedImage ? "bg-green-400" : "bg-gray-600"
                      }`}
                    />
                    <span
                      className={
                        selectedImage ? "text-green-400" : "text-gray-400"
                      }
                    >
                      Image uploaded
                    </span>
                  </div>
                  <div className="flex items-center gap-2 text-sm">
                    <div
                      className={`w-2 h-2 rounded-full ${
                        analysisResult?.identified_person
                          ? "bg-green-400"
                          : "bg-gray-600"
                      }`}
                    />
                    <span
                      className={
                        analysisResult?.identified_person
                          ? "text-green-400"
                          : "text-gray-400"
                      }
                    >
                      Person identified
                    </span>
                  </div>
                  <div className="flex items-center gap-2 text-sm">
                    <div
                      className={`w-2 h-2 rounded-full ${
                        analysisResult?.social_media_profiles
                          ? "bg-green-400"
                          : "bg-gray-600"
                      }`}
                    />
                    <span
                      className={
                        analysisResult?.social_media_profiles
                          ? "text-green-400"
                          : "text-gray-400"
                      }
                    >
                      Official profiles found
                    </span>
                  </div>
                  <div className="flex items-center gap-2 text-sm">
                    <div
                      className={`w-2 h-2 rounded-full ${
                        analysisResult?.news_articles
                          ? "bg-green-400"
                          : "bg-gray-600"
                      }`}
                    />
                    <span
                      className={
                        analysisResult?.news_articles
                          ? "text-green-400"
                          : "text-gray-400"
                      }
                    >
                      News articles fetched
                    </span>
                  </div>
                  <div className="flex items-center gap-2 text-sm">
                    <div
                      className={`w-2 h-2 rounded-full ${
                        analysisResult?.ai_summary
                          ? "bg-green-400"
                          : "bg-gray-600"
                      }`}
                    />
                    <span
                      className={
                        analysisResult?.ai_summary
                          ? "text-green-400"
                          : "text-gray-400"
                      }
                    >
                      AI analysis complete
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Analysis Results */}
        {analysisResult && (
          <div className="space-y-6">
            {/* Error State */}
              {analysisResult.status === "error" && (
      <Card className="bg-red-900/20 border-red-500/50">
        <CardContent className="p-6">
          <div className="flex items-center gap-3">
            <AlertTriangle className="h-6 w-6 text-red-400" />
            <div>
              <h3 className="text-red-400 font-semibold">Analysis Failed</h3>
              <p className="text-red-300 text-sm">{analysisResult.error}</p>
              {analysisResult.analysis_metadata?.error_details && (
                <p className="text-red-200 text-xs mt-2">
                  Details: {analysisResult.analysis_metadata.error_details}
                </p>
              )}
            </div>
          </div>
        </CardContent>
      </Card>
    )}

            {/* No Match State */}
            {analysisResult.status === "no_match" && (
              <Card className="bg-yellow-900/20 border-yellow-500/50">
                <CardContent className="p-6">
                  <div className="flex items-center gap-3">
                    <Eye className="h-6 w-6 text-yellow-400" />
                    <div>
                      <h3 className="text-yellow-400 font-semibold">
                        No Match Found
                      </h3>
                      <p className="text-yellow-300 text-sm">
                        The person in the image was not found in our database of
                        known personalities.
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Success State */}
            {analysisResult.status === "success" &&
              analysisResult.identified_person && (
                <>
                  {/* Identified Person */}
                  <Card className="bg-green-900/20 border-green-500/50">
                    <CardHeader>
                      <CardTitle className="text-green-400 flex items-center gap-2">
                        <CheckCircle className="h-5 w-5" />✅ Person Identified
                      </CardTitle>
                      {analysisResult.analysis_metadata?.is_deceased && (
                        <div className="bg-red-900/50 p-2 rounded-md">
                          <span className="text-red-300 font-medium">
                            Deceased Person
                          </span>
                          <p className="text-red-200 text-sm">
                            Only official profiles are shown
                          </p>
                        </div>
                      )}
                    </CardHeader>
                    <CardContent>
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="space-y-3">
                          <div>
                            <h3 className="text-xl font-bold text-white">
                              {analysisResult.identified_person.name}
                            </h3>
                            <p className="text-gray-300">
                              {analysisResult.identified_person.description}
                            </p>
                          </div>
                          <div className="flex items-center gap-4">
                            <Badge className="bg-green-600 text-white">
                              {Math.round(
                                analysisResult.identified_person.confidence *
                                  100
                              )}
                              % Confidence
                            </Badge>
                            <Badge
                              variant="outline"
                              className="border-gray-500 text-gray-300"
                            >
                              {analysisResult.identified_person.method}
                            </Badge>
                          </div>
                        </div>
                        <div className="flex justify-end gap-2">
                          <Button
                            onClick={() => downloadReport("json")}
                            className="bg-blue-600 hover:bg-blue-700"
                          >
                            <Download className="h-4 w-4 mr-2" />
                            JSON Report
                          </Button>
                          <Button
                            onClick={() => downloadReport("pdf")}
                            className="bg-red-600 hover:bg-red-700"
                            disabled={!analysisResult.pdf_report_base64}
                          >
                            <Download className="h-4 w-4 mr-2" />
                            PDF Report
                          </Button>
                        </div>
                      </div>
                    </CardContent>
                  </Card>

                  {/* Social Media Profiles */}
                  {analysisResult.social_media_profiles &&
                    Object.keys(analysisResult.social_media_profiles).length >
                      0 && (
                      <Card className="bg-gray-900/50 border-gray-700">
                        <CardHeader>
                          <CardTitle className="text-white flex items-center gap-2">
                            <Users className="h-5 w-5" />
                            🔗 Official Social Profiles
                          </CardTitle>
                          <CardDescription className="text-gray-400">
                            Verified and official profiles only
                          </CardDescription>
                        </CardHeader>
                        <CardContent>
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            {Object.entries(
                              analysisResult.social_media_profiles
                            ).map(([platform, links]) => (
                              <div
                                key={platform}
                                className="p-4 bg-gray-800/50 rounded-lg"
                              >
                                <h4 className="font-semibold text-white capitalize mb-2">
                                  {platform}
                                </h4>
                                <div className="space-y-2">
                                  {links.map((link, index) => (
                                    <a
                                      key={index}
                                      href={link}
                                      target="_blank"
                                      rel="noopener noreferrer"
                                      className="flex items-center gap-2 text-blue-400 hover:text-blue-300 text-sm"
                                    >
                                      <ExternalLink className="h-3 w-3" />
                                      {link}
                                    </a>
                                  ))}
                                </div>
                              </div>
                            ))}
                          </div>
                        </CardContent>
                      </Card>
                    )}

                  {/* News Articles */}
                  {analysisResult.news_articles &&
                    analysisResult.news_articles.length > 0 && (
                      <Card className="bg-gray-900/50 border-gray-700">
                        <CardHeader>
                          <CardTitle className="text-white flex items-center gap-2">
                            <FileText className="h-5 w-5" />
                            📰 Recent News Articles
                          </CardTitle>
                          <CardDescription className="text-gray-400">
                            Latest news from reliable sources
                          </CardDescription>
                        </CardHeader>
                        <CardContent>
                          <div className="space-y-4">
                            {analysisResult.news_articles.map(
                              (article, index) => (
                                <div
                                  key={index}
                                  className="p-4 bg-gray-800/50 rounded-lg border border-gray-700/50"
                                >
                                  <div className="flex gap-4">
                                    {article.image && (
                                      <div className="relative w-24 h-24 flex-shrink-0">
                                        <Image
                                          src={article.image}
                                          alt={article.title}
                                          fill
                                          className="object-cover rounded-md"
                                        />
                                      </div>
                                    )}
                                    <div className="flex-1">
                                      <h4 className="font-semibold text-white mb-1">
                                        {article.title}
                                      </h4>
                                      <p className="text-gray-300 text-sm mb-2">
                                        {article.description}
                                      </p>
                                      <div className="flex items-center gap-3 text-xs text-gray-400">
                                        <span>{article.source}</span>
                                        <span>•</span>
                                        <span>
                                          {new Date(
                                            article.published_at
                                          ).toLocaleDateString()}
                                        </span>
                                      </div>
                                    </div>
                                    <a
                                      href={article.url}
                                      target="_blank"
                                      rel="noopener noreferrer"
                                      className="text-blue-400 hover:text-blue-300 ml-4 self-center"
                                    >
                                      <ExternalLink className="h-4 w-4" />
                                    </a>
                                  </div>
                                </div>
                              )
                            )}
                          </div>
                        </CardContent>
                      </Card>
                    )}

                  {/* AI Summary */}
                  {analysisResult.ai_summary &&
                    !analysisResult.ai_summary.error && (
                      <Card className="bg-purple-900/20 border-purple-500/50">
                        <CardHeader>
                          <CardTitle className="text-purple-400 flex items-center gap-2">
                            <TrendingUp className="h-5 w-5" />
                            🤖 AI Analysis Summary
                          </CardTitle>
                          <CardDescription className="text-purple-300">
                            Generated by Gemini 1.5 Flash
                          </CardDescription>
                        </CardHeader>
                        <CardContent>
                          <div className="prose prose-invert max-w-none">
                            <div className="whitespace-pre-wrap text-gray-200">
                              {analysisResult.ai_summary.summary}
                            </div>
                            {analysisResult.ai_summary.model && (
                              <div className="mt-4 text-xs text-gray-400">
                                Generated by: {analysisResult.ai_summary.model}
                              </div>
                            )}
                          </div>
                        </CardContent>
                      </Card>
                    )}

                  {/* Comprehensive Report Preview */}
                  {analysisResult.comprehensive_report && (
                    <Card className="bg-gray-900/50 border-gray-700">
                      <CardHeader>
                        <CardTitle className="text-white flex items-center gap-2">
                          <FileText className="h-5 w-5" />
                          📄 Comprehensive Report
                        </CardTitle>
                        <CardDescription className="text-gray-400">
                          Complete OSINT analysis report with timeline and risk
                          assessment
                        </CardDescription>
                      </CardHeader>
                      <CardContent>
                        <div className="space-y-6">
                          {/* Report Metadata */}
                          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div className="p-3 bg-gray-800/50 rounded-lg">
                              <div className="text-sm text-gray-400">
                                Report ID
                              </div>
                              <div className="font-mono text-xs text-white">
                                {analysisResult.comprehensive_report.report_id}
                              </div>
                            </div>
                            <div className="p-3 bg-gray-800/50 rounded-lg">
                              <div className="text-sm text-gray-400">
                                Generated
                              </div>
                              <div className="text-sm text-white">
                                {new Date(
                                  analysisResult.comprehensive_report.generated_at
                                ).toLocaleString()}
                              </div>
                            </div>
                            <div className="p-3 bg-gray-800/50 rounded-lg">
                              <div className="text-sm text-gray-400">
                                Subject
                              </div>
                              <div className="text-sm text-white">
                                {analysisResult.comprehensive_report.subject}
                              </div>
                            </div>
                          </div>

                          {/* Risk Assessment */}
                          {analysisResult.comprehensive_report
                            .risk_assessment && (
                            <div className="p-4 bg-gray-800/30 rounded-lg">
                              <h4 className="font-semibold text-white mb-3">
                                ⚠️ Risk Assessment
                              </h4>
                              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                  <div className="space-y-2">
                                    <div className="flex justify-between">
                                      <span className="text-gray-400">
                                        Overall Risk Level:
                                      </span>
                                      <Badge
                                        className={getRiskColor(
                                          analysisResult.comprehensive_report
                                            .risk_assessment.overall_risk_level
                                        )}
                                      >
                                        {
                                          analysisResult.comprehensive_report
                                            .risk_assessment.overall_risk_level
                                        }
                                      </Badge>
                                    </div>
                                    <div className="flex justify-between">
                                      <span className="text-gray-400">
                                        Public Sentiment:
                                      </span>
                                      <span className="text-white">
                                        {
                                          analysisResult.comprehensive_report
                                            .risk_assessment.public_sentiment
                                        }
                                      </span>
                                    </div>
                                    <div className="flex justify-between">
                                      <span className="text-gray-400">
                                        Media Attention:
                                      </span>
                                      <span className="text-white">
                                        {
                                          analysisResult.comprehensive_report
                                            .risk_assessment.media_attention
                                        }
                                      </span>
                                    </div>
                                  </div>
                                </div>
                                <div>
                                  <div className="text-sm text-gray-400 mb-2">
                                    Recommendations:
                                  </div>
                                  <ul className="text-sm text-gray-300 space-y-1">
                                    {analysisResult.comprehensive_report.risk_assessment.recommendations?.map(
                                      (rec: string, index: number) => (
                                        <li
                                          key={index}
                                          className="flex items-start gap-2"
                                        >
                                          <span className="text-blue-400">
                                            •
                                          </span>
                                          {rec}
                                        </li>
                                      )
                                    )}
                                  </ul>
                                </div>
                              </div>
                            </div>
                          )}

                          {/* Controversies Timeline */}
                          {analysisResult.comprehensive_report
                            .controversies_timeline && (
                            <div className="p-4 bg-gray-800/30 rounded-lg">
                              <h4 className="font-semibold text-white mb-3">
                                📅 Timeline of Controversies
                              </h4>
                              <div className="space-y-3">
                                {analysisResult.comprehensive_report.controversies_timeline.map(
                                  (controversy: any, index: number) => (
                                    <div
                                      key={index}
                                      className="flex gap-4 p-3 bg-gray-700/30 rounded-lg"
                                    >
                                      <div className="text-xs text-gray-400 min-w-[80px]">
                                        {new Date(
                                          controversy.date
                                        ).toLocaleDateString()}
                                      </div>
                                      <div className="flex-1">
                                        <div className="font-medium text-white text-sm">
                                          {controversy.title}
                                        </div>
                                        <div className="text-xs text-gray-300 mt-1">
                                          {controversy.description}
                                        </div>
                                        <div className="flex items-center gap-2 mt-2">
                                          <Badge
                                            variant="outline"
                                            className="text-xs border-gray-600"
                                          >
                                            {controversy.source}
                                          </Badge>
                                          <Badge
                                            className={`text-xs ${getRiskColor(
                                              controversy.impact_level
                                            )}`}
                                          >
                                            {controversy.impact_level} Impact
                                          </Badge>
                                        </div>
                                      </div>
                                    </div>
                                  )
                                )}
                              </div>
                            </div>
                          )}

                          <Separator className="bg-gray-700" />

                          <div className="flex justify-center">
                            <Button
                              onClick={() => downloadReport("json")}
                              className="bg-green-600 hover:bg-green-700"
                            >
                              <Download className="h-4 w-4 mr-2" />
                              Download Complete Report (JSON)
                            </Button>
                          </div>
                        </div>
                      </CardContent>
                    </Card>
                  )}
                </>
              )}
          </div>
        )}

        {/* Feature Info */}
        {!analysisResult && (
          <Card className="bg-blue-900/20 border-blue-500/50">
            <CardHeader>
              <CardTitle className="text-blue-400">🚀 How It Works</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div className="text-center p-4">
                  <Camera className="h-8 w-8 mx-auto mb-2 text-blue-400" />
                  <h4 className="font-semibold text-white mb-1">
                    1. Upload Image
                  </h4>
                  <p className="text-sm text-gray-400">
                    Upload a clear photo of a famous personality
                  </p>
                </div>
                <div className="text-center p-4">
                  <Eye className="h-8 w-8 mx-auto mb-2 text-green-400" />
                  <h4 className="font-semibold text-white mb-1">
                    2. Face Recognition
                  </h4>
                  <p className="text-sm text-gray-400">
                    AI identifies the person using facial recognition
                  </p>
                </div>
                <div className="text-center p-4">
                  <Search className="h-8 w-8 mx-auto mb-2 text-yellow-400" />
                  <h4 className="font-semibold text-white mb-1">
                    3. Social Lookup
                  </h4>
                  <p className="text-sm text-gray-400">
                    Find social media profiles and news articles
                  </p>
                </div>
                <div className="text-center p-4">
                  <FileText className="h-8 w-8 mx-auto mb-2 text-purple-400" />
                  <h4 className="font-semibold text-white mb-1">
                    4. Generate Report
                  </h4>
                  <p className="text-sm text-gray-400">
                    Create comprehensive OSINT analysis report
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        )}
      </main>
    </div>
  );
}
