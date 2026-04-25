balance = 0
transactions =[]


def checkbalance():
  print(f"Your Current Balance: {balance}")


def deposit():
  global balance
  amount = int(input("Enter Amount :"))
  balance += amount
  transactions.append(f"Deposited {amount}")
  print("Deposit Successful!")


def withdraw():
  global balance
  amount = int(input("Enter Amount :"))
  if amount <= balance:
    balance -= amount
    transactions.append(f"Withdrew {amount}")
    print("Withdrawal successful!")
  else:
    print("Insufficient Balance")


def statement():
  print("\nTransactions History:")
  if len(transactions) == 0:
    print("No Transactions Yet.")
  else:
    for i in transactions:
      print("-", i)


print("Welcome!")
print("Please choose an option:")
print("1.Check Amount")
print("2.Deposite Amount")
print("3.Withdraw")
print("4.Statement")
print("5.Exit")

while True:
    choice = input("Enter choice:")
    if choice == "1":
        checkbalance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        statement()
    elif choice == "5":
        print("Thank you for using our service!")
        break
    else:
        print("Invalid Choice!")
