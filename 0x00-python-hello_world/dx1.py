#!/usr/bin/python3

def calculate_future_value(principal, interest_rate):
    """
    Calculate the future value of an investment after one year.

    Args:
    - principal (float): The initial deposit amount.
    - interest_rate (float): The fixed interest rate per annum.

    Returns:
    - float: The future value of the investment after one year.
    """
    future_value = principal * (1 + interest_rate / 100)
    return future_value

# Initial deposit amount
initial_deposit = 1800.0

# Fixed interest rate per annum
interest_rate = 10.65

# Calculate the future value of the deposit after one year
future_value = calculate_future_value(initial_deposit, interest_rate)

# Display the result
print(f"Initial Deposit: ${initial_deposit:.2f}")
print(f"Interest Rate: {interest_rate:.2f}%")
print(f"Future Value after one year: ${future_value:.2f}")