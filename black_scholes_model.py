"""Black-Scholes model for option pricing. See https://www.investopedia.com/terms/b/blackscholes.asp 
or https://www.quantstart.com/articles/European-Vanilla-Call-Put-Option-Pricing-with-Python/"""

from math import log, pi, exp


def norm_pdf(x):
    """Probability density function for the standard normal distribution."""
    return (1.0 / (2.0 * pi) ** 0.5) * exp(-0.5 * x ** 2)


def norm_cdf(x):
    """Cumulative distribution function for the standard normal distribution."""
    k = 1.0 / (1.0 + 0.2316419 * abs(x))
    k_sum = k * (0.319381530 + k * (-0.356563782 + k *
                 (1.781477937 + k * (-1.821255978 + 1.330274429 * k))))
    if x >= 0.0:
        return (1.0 - (1.0 / (2.0 * pi) ** 0.5) * exp(-0.5 * x ** 2) * k_sum)
    return 1.0 - norm_cdf(-x)