import numpy as np

def VaR(returns, confidence=0.95, principal=1):
    """
    Calculate historical Value at Risk (VaR)

    :param returns: array of portfolio returns
    :param confidence: confidence level (0.95 means 95%)
    :param principal: portfolio value
    :return: VaR amount (positively stated)
    """
    returns = np.array(returns)
    # Calculate the percentile of losses
    var_percentile = np.percentile(returns, (1-confidence)*100)
    var_amount = -var_percentile * principal  # positive number for loss
    return var_amount

# Example usage:
# returns = np.random.normal(0, 0.01, 1000)
# print("VaR 95%:", VaR(returns, 0.95, 100000))
