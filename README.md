# Portfolio Risk & Optimization Engine

IndiQuant is a professional-grade risk management framework tailored for Indian equities. It provides a modular pipeline to analyze market risk using industry-standard metrics like **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)**, validates those models through statistical backtesting, and optimizes portfolio weights to minimize downside risk.

---

##  Features

* **Automated Data Pipeline:** Seamless integration with `yfinance` to fetch live NSE data (Reliance, TCS, HDFC Bank, etc.).
* **Risk Modeling:**
    * **Historical VaR:** Non-parametric approach using actual historical price movements.
    * **Parametric (Gaussian) VaR:** Uses mean-variance math and the Normal Distribution.
    * **Monte Carlo Simulation:** Simulates 10,000+ potential market paths to forecast risk.
* **Tail Risk Analysis:** Calculates **CVaR (Expected Shortfall)** to measure the average loss in worst-case scenarios.
* **Statistical Backtesting:** Implements the **Kupiec Proportion of Failures (POF) Test** to ensure model reliability.
* **Portfolio Optimization:** Uses **Linear Programming (Mean-CVaR)** to find the most efficient asset allocation for a target return.

---

##  The Mathematics

### Value at Risk (VaR)
We calculate the maximum expected loss over a 1-day horizon at a 95% confidence level. 
$$VaR_{\alpha}(X) = -\inf\{x \in \mathbb{R} : P(X \le x) > 1-\alpha\}$$



### Kupiec Test (Backtesting)
To verify our VaR model, we use a Likelihood Ratio (LR) test to check if the number of actual breaches matches the expected failure rate.
$$LR_{POF} = -2 \ln \left[ \frac{(1-p)^{T-x} p^x}{(1-\hat{p})^{T-x} \hat{p}^x} \right]$$
