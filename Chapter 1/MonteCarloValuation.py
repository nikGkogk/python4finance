import math
import numpy as np

# Initialise Parameters
S0 = 100.  # initial index level
K = 105.  # strike price
T = 1.0  # time to maturity
r = 0.05  # risk-less short rate
sigma = 0.2  # volatility

I: int = 100000  # number of simulations

# Draw I pseudo-random numbers z (i ), i ∈ {1, 2, ..., I }, from the standard normal distribution.
np.random.seed(666)  # some random seed
z = np.random.standard_normal(I)

# Calculate all resulting index levels at maturity with Black-Scholes-Merton (End-of-period values are simulated)
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * z)

# Calculate all inner values of the option at maturity (payoff at maturity)
hT = np.maximum(ST - K, 0)

# Estimate the option present value via the Monte Carlo estimator
C0 = math.exp(-r * T) * np.mean(hT)

# Result Output
print('Value of the European call option %5.3f.' % C0)
