def printmenu():
    print()
printmenu()
print(""" 
    1. Check balance
    2. Deposit
    3. Withdrawal
    4. Exit 
    """)

i = int(input("Type in transaction number (1, 2, 3, 4): "))
if (i==1):
    import check_balance_daiva
    print(check_balance_daiva.balance())
elif(i==2):
    import testdeposit_daiva
    print(testdeposit_daiva.testdeposit())
elif(i==3):
    import testwithdrawal_daiva
    print(testwithdrawal_daiva.testwithd())
elif(i==4):
    print("Thank you for using ATM. You exit the program")
else:
    print("Choose number 1, 2, 3, 4")