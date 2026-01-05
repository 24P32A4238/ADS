balance = 10000

print("Welcome to ATM")
amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Please collect your cash")
    print("Remaining balance:", balance)

print("Thank you for using ATM")