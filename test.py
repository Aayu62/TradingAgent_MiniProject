from tradingagents.agents.news_analyst import NewsAnalyst
from tradingagents.agents.Reasoning import NewsReasoningAgent
from tradingagents.agents.decision_agent import DecisionAgent

# Initialize agents
news_agent = NewsAnalyst()
reasoning_agent = NewsReasoningAgent()
decision_agent = DecisionAgent()

ticker = "TSLA"

articles = news_agent.fetch_news(ticker, max_articles=15)

news_analysis = reasoning_agent.analyze(ticker, articles)
print("RAW NEWS ANALYSIS:\n", news_analysis["raw_response"])

news_score = news_analysis["news_score"]
technical_signal = news_analysis["sentiment"]
print("##############################################")
decision = decision_agent.decide(
    ticker=ticker,
    news_score=news_score,
    technical_signal=technical_signal
)

print("\nFINAL DECISION:")
for k, v in decision.items():
    print(f"{k}: {v}")
