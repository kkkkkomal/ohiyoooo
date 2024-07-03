print("welcome to our ATM\n")
balance=1000
password=4444
change=0

pin=int(input("Enter your pin:\n"))
if pin==password:
    while change!=4:
        print("1:Deposit")
        print("2:Withdraw")
        print("3:Change password")
        print("4:Check balance")
        choice=int(input("choose an option:"))
        if choice==1:
            depo=int(input("Enter amount to deposit"))
            print("Amount deposited")
            balance+=depo 
            print("Balance:",balance)
        elif choice==2:
            draw=int(input("Enter amount to withdraw:"))
            balance-=draw
            print("Balance:",balance)
        elif choice==3:
            po=int(input("Enter new password:"))
            print("New password",po)
        elif choice==4:
            print("Your current balance is:",balance)
else:
    print("Incorrect password")
