class DecisionAgent:
    """
    Demo Decision AI Agent.
    Combines news sentiment score + technical signal
    to produce a BUY / SELL / HOLD decision.
    """

    def __init__(self,
                 buy_threshold=4,
                 sell_threshold=-4):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    def decide(self, ticker, news_score, technical_signal):
        """
        Args:
            ticker (str): Stock ticker
            news_score (int): -10 to +10
            technical_signal (str): BULLISH / BEARISH / NEUTRAL

        Returns:
            dict: decision output
        """

        # Decision logic
        if news_score >= self.buy_threshold and technical_signal == "BULLISH":
            decision = "BUY"
            confidence = "HIGH"

        elif news_score <= self.sell_threshold and technical_signal == "BEARISH":
            decision = "SELL"
            confidence = "HIGH"

        elif abs(news_score) >= 3:
            decision = "HOLD"
            confidence = "MEDIUM"

        else:
            decision = "HOLD"
            confidence = "LOW"

        explanation = (
            f"Decision based on news score ({news_score}) and "
            f"technical signal ({technical_signal})."
        )

        return {
            "ticker": ticker,
            "decision": decision,
            "confidence": confidence,
            "news_score": news_score,
            "technical_signal": technical_signal,
            "explanation": explanation
        }
