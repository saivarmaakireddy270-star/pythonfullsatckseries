pin='6305'
balance=100000
attempts=0
maxattempts=3
transaction=[]
while True:
    enterpin=input("enter your pin: ")
    if pin==enterpin:
        print("pin is succesfully verified")
        break
    else:
        attempts+=1
        print("invalid pin, remaining attempts are",(maxattempts-attempts))
    if attempts>=maxattempts:
        print("card is blocked due to unsuccessful attempts")
        exit()
print('go to menu')
while True:
    print("menu of banking actions")
    print("press 1 for balance enquiry")
    print("press 2 for deposit money")
    print("press 3 for the withdraw")
    print("press 4 for current balance")
    choice=int(input("enter your choice"))
    if choice==1:
        print("balance are",balance)
    elif choice==2:
        print("deposit money")
    if amount>0:
        balance=amount+balance
        transaction.append(f"deposit amount is: {amount}")
        if len(transaction>5):
            transaction.pop(0)
        print("money is deposit,cureebt balance are")
    else:
        print("valid amount")
    elif choice==3:
        withraqamount=int(input("enter the amount to withdraw"))
        print("withdraw the amount")
        balance=balance-amount
    else:
        print("invalid amount")
    if choice==4:
        currentbalance=int(input("show the current balance"))
        currentbalance=balance+amount
    else:
        print("current balance is 0")




            

    
    