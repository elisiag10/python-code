# try:
#     num = int(input("Enter a number: "))
#     r = 10 / num
#     print("Results: ", r)
# except ZeroDivisionError:
#     print("Error: Cant divide by Zero")
# except ValueError:
#     print("Error: enter a valid number")
# except Exception as e:
#     print("An error occured: ", e)
# else:
#     print("No exceptions occurred")
# finally:
#     print("Execution completed")


class InsufficientFundsError(Exception):
    pass 

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds")
    return balance - amount

try:
    account_balance = 500
    withdrawal_amount = int(input("Enter an amount to withdraw: "))
    remaining_balance = withdraw(account_balance, withdrawal_amount)
    print("Remaining balance: ", remaining_balance)
except InsufficientFundsError as ife:
    print("Error: ", ife)