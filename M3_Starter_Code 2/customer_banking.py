# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    savings_account_balance =float(input('Enter your savings starting account balance: '))
    savings_account_interest =float(input("Enter your savings account interest rate:"))
    savings_account_months = int(input("How many months is your savings account term?: "))
    
    # Call the create_savings_account function and pass the variables from the user.
    Updated_savings_balance, Updated_interest_rate = create_savings_account(savings_account_balance,savings_account_interest, savings_account_months)
    

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your interest earned is $ {Updated_interest_rate:,.2f}")
    print(f"Your updated balance is ${Updated_savings_balance:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    CD_account_balance =float(input('Enter your CD account starting balance: '))
    CD_account_interest =float(input("Enter your interest rate:"))
    CD_account_months = int(input("How many months is your term?: "))

    # Call the create_cd_account function and pass the variables from the user.
    new_balance, Interest_earned = create_cd_account(CD_account_balance, CD_account_interest, CD_account_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your interest earned is $ {Interest_earned:,.2f}")
    print(f"Your updated balance is ${new_balance:,.2f}")


    # Call the main function.
if __name__ == "__main__":
    main()