from bank import Bank

def main():
    bank = Bank()
    while True:
        print("/nWelcome to Agi's Bank/n")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4.Check Balance")
        print("5. Exist")
        choice = input("Enter your prefered choice")


        if choice == "1":
            name = input("Enter your name:")
            initial_deposit = float(input("Enter initial deposit amount"))
            bank.create_account(name,initial_deposit)

        elif choice == "2":
            name = input("Enter your account name:")
            amount = float(input("Enter  deposit amount"))
            bank.deposit(name,amount)

        elif choice == "3":
            name = input("Enter your  name:")
            amount =  float(input("Enter  your withdrawal amount"))
            bank.withdraw(name,amount)


        elif choice == "4":
            name = ("Enter your name")
            bank.check_balance(name)

            

        elif choice== "5":
           print("Thank you for banking With Us!.")
           break
         
        else:
         print("invalid choice entered")

if __name__  == main():
    main()      
   


