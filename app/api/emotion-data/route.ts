import { type NextRequest, NextResponse } from "next/server"
import fs from "fs"
import path from "path"
import { parse } from "csv-parse/sync"

export async function GET(request: NextRequest) {
  try {
    // Try to read from data/scraped_data.csv
    const csvPath = path.join(process.cwd(), "data", "scraped_data.csv")

    if (fs.existsSync(csvPath)) {
      const csvContent = fs.readFileSync(csvPath, "utf-8")
      const records = parse(csvContent, {
        columns: true,
        skip_empty_lines: true,
      })

      // Process CSV data and add emotion analysis
      const processedData = records.map((record: any) => {
        // Simple emotion detection based on keywords
        const text = record.text || record.content || record.message || ""
        const emotion = detectEmotion(text)
        const riskLevel = assessRisk(text, emotion)

        return {
          text: text,
          timestamp: record.timestamp || record.date || new Date().toISOString(),
          emotion_label: emotion.label,
          explanation: emotion.explanation,
          confidence_score: emotion.confidence,
          risk_level: riskLevel,
        }
      })

      return NextResponse.json(processedData)
    } else {
      // Return empty array if no CSV file found
      return NextResponse.json([])
    }
  } catch (error) {
    console.error("Error reading emotion data:", error)
    return NextResponse.json({ error: "Failed to load emotion data" }, { status: 500 })
  }
}

function detectEmotion(text: string) {
  const lowerText = text.toLowerCase()

  // Simple keyword-based emotion detection
  const emotionPatterns = {
    Happy: {
      keywords: ["happy", "joy", "excited", "great", "awesome", "love", "amazing", "wonderful", "fantastic"],
      explanation: "Contains positive emotional expressions",
    },
    Sad: {
      keywords: ["sad", "depressed", "down", "upset", "crying", "hurt", "disappointed", "miserable"],
      explanation: "Shows signs of sadness or disappointment",
    },
    Angry: {
      keywords: ["angry", "mad", "furious", "rage", "hate", "stupid", "ridiculous", "frustrated", "pissed"],
      explanation: "Contains angry language and frustration",
    },
    Fearful: {
      keywords: ["scared", "afraid", "worried", "anxious", "fear", "terrified", "nervous", "panic"],
      explanation: "Expresses worry, anxiety, or fear",
    },
    Threatening: {
      keywords: ["threat", "kill", "hurt", "destroy", "revenge", "payback", "consequences", "warning"],
      explanation: "Contains threatening language or implications",
    },
    Hateful: {
      keywords: ["hate", "despise", "loathe", "disgusting", "terrible", "awful", "worst"],
      explanation: "Contains hateful expressions",
    },
    Supportive: {
      keywords: ["support", "help", "encourage", "believe", "together", "solidarity", "assist"],
      explanation: "Offers support or encouragement",
    },
    Sarcastic: {
      keywords: ["yeah right", "sure", "obviously", "brilliant", "genius", "perfect"],
      explanation: "Uses sarcasm or irony",
    },
  }

  let bestMatch = { label: "Neutral", explanation: "Neutral tone without strong emotional content", confidence: 0.5 }
  let maxScore = 0

  for (const [emotion, pattern] of Object.entries(emotionPatterns)) {
    let score = 0
    for (const keyword of pattern.keywords) {
      if (lowerText.includes(keyword)) {
        score += 1
      }
    }

    if (score > maxScore) {
      maxScore = score
      bestMatch = {
        label: emotion,
        explanation: pattern.explanation,
        confidence: Math.min(0.6 + score * 0.1, 0.95),
      }
    }
  }

  return bestMatch
}

function assessRisk(text: string, emotion: any): "LOW" | "MEDIUM" | "HIGH" | "CRITICAL" {
  const lowerText = text.toLowerCase()

  // Critical risk indicators
  const criticalKeywords = ["kill", "murder", "bomb", "attack", "violence", "weapon"]
  if (criticalKeywords.some((keyword) => lowerText.includes(keyword))) {
    return "CRITICAL"
  }

  // High risk indicators
  const highRiskKeywords = ["threat", "hurt", "destroy", "revenge", "payback"]
  if (highRiskKeywords.some((keyword) => lowerText.includes(keyword)) || emotion.label === "Threatening") {
    return "HIGH"
  }

  // Medium risk indicators
  if (emotion.label === "Hateful" || emotion.label === "Angry") {
    return "MEDIUM"
  }

  return "LOW"
}
