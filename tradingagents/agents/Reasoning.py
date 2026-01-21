from tradingagents.llm.ollama_client import OllamaClient
import re

class NewsReasoningAgent:
    """
    News impact scoring agent.
    This agent does NOT decide BUY/SELL.
    It only scores how news impacts the future of a stock.
    """

    def __init__(self, model="llama3.1:8b"):
        self.llm = OllamaClient(model=model)

    def _build_prompt(self, ticker, articles):
        news_block = ""

        for i, article in enumerate(articles, start=1):
            news_block += f"""
Article {i}:
Title: {article.get('title', '')}
Summary: {article.get('description', '')}
"""

        prompt = f"""
You are an institutional-level financial analysis AI.

You are given recent news related to a publicly traded company,
identified only by its stock ticker symbol.

Ticker Symbol: {ticker}

Recent News Articles:
{news_block}

Task:
Analyze the combined impact of ALL news articles on the company's
future business performance and stock price trend.

Consider:
- Earnings, revenue, margins
- Product launches, innovation
- Regulations, lawsuits, fines
- Management changes
- Industry and macroeconomic impact
- Competitive positioning

Ignore:
- Day trading noise
- Clickbait headlines
- Unverified rumors

Output STRICTLY in the following format:

NewsScore: <integer from -10 to +10>
Sentiment: <BULLISH / BEARISH / NEUTRAL>
Impact: <SHORT_TERM / LONG_TERM / BOTH>
Explanation: <3–5 concise sentences>

Scoring Rules:
+7 to +10  = Strong positive long-term impact
+3 to +6   = Moderately positive
-2 to +2   = Mixed or unclear
-3 to -6   = Moderately negative
-7 to -10  = Severe negative risk

Think carefully. Base your judgment on fundamentals.
"""

        return prompt
    
    def _extract(self, raw_response):
        """
        Extract structured values from LLM response.
        """

        try:
            score = int(re.search(r"NewsScore:\s*(-?\d+)", raw_response).group(1))
        except:
            score = 0

        try:
            sentiment = re.search(
                r"Sentiment:\s*(BULLISH|BEARISH|NEUTRAL)",
                raw_response
            ).group(1)
        except:
            sentiment = "NEUTRAL"

        try:
            impact = re.search(
                r"Impact:\s*(SHORT_TERM|LONG_TERM|BOTH)",
                raw_response
            ).group(1)
        except:
            impact = "UNKNOWN"

        try:
            explanation = re.search(
                r"Explanation:\s*(.*)",
                raw_response,
                re.DOTALL
            ).group(1).strip()
        except:
            explanation = raw_response.strip()

        return {
            "news_score": score,
            "sentiment": sentiment,
            "impact": impact,
            "explanation": explanation
        }

    def analyze(self, ticker, articles):
        if not articles:
            return {
                "news_score": 0,
                "sentiment": "NEUTRAL",
                "impact": "NONE",
                "explanation": "No relevant news available."
            }

        prompt = self._build_prompt(ticker, articles)
        response = self.llm.generate(prompt)

        extracted = self._extract(response)
        extracted["raw_response"] = response

        return extracted
