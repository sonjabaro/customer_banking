"""Imports the SavingsAccount class and attributes from the Account.py file."""
from Account import Account

# Define a function for the Savings Account

"""Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """

def savings_account(balance, interest_rate, months):
    interest_earned = float(balance * (interest_rate/100 * months/12))
    balance = float(200)
    balance += interest_earned
    print(f"The new balance is: {balance}")
    return balance, interest_earned

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.

your_savings_account = Account(self,balance,interest_rate)
def get_balance(self):
        return self.balance
def get_interest_rate(self):
        return self.interest(self)
    
    # Calculate interest earned
Interest_earned = balance * (apr/100 * months/12)
starting_interest = 0
    

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
