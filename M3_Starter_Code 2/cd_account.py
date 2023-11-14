"""Import the Account class from the Account.py file."""
from Account import Account


"""Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """

def create_cd_account(balance, interest_rate, months):
    interest_earned = float(balance * (interest_rate/100 * months/12))
    balance += interest_earned
    print(f"The new balance is: {balance}")
    return balance, interest_earned

# Create an instance of the `Account` class and pass in the balance and interest parameters.
#  Hint: You need to add the interest as a value, i.e, 0.
cd_account =Account(balance,interest)
Interest= 0
   
    # Calculate interest earned
Interest_earned = balance * (interest_rate/100 * months/12)


# Update the savings account balance by adding the interest earned
new_balance = balance + Interest_earned


# Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
cd_account.set_balance(new_balance)


# Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
cd_account.set_interest(Interest_earned)

# Return the updated balance and interest earned.
return new_balance, Interest_earned
