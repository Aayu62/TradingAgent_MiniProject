# TradingAgents (News-Analyst)

A multi-agent AI system for news-based stock analysis and decision making.

## Agents
- NewsAnalyst – Fetches financial news
- NewsReasoningAgent – Scores news impact using LLM
- DecisionAgent – Produces BUY / SELL / HOLD decisions

## Tech
- Python
- Ollama (local LLM)
- Modular multi-agent architecture

## Ouput
--- RAW LLM RESPONSE ---
NewsScore: 6
Sentiment: BULLISH
Impact: LONG_TERM
Explanation: Strong earnings growth and AI expansion...

--- STRUCTURED NEWS SIGNAL ---
news_score: 6
sentiment: BULLISH
impact: LONG_TERM
explanation: Strong earnings growth...

--- FINAL DECISION ---
ticker: TSLA
decision: BUY
confidence: HIGH
news_score: 6
technical_signal: BULLISH

