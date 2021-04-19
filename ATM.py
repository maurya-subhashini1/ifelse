
print("welcome")
card=input("enter the ATM card:")
if card=="debit":
    print("start proses")
    language=input("enter the languege:")
    if language=="english" or "hindi":
        print("language is crrocet")
        pin=input("enter the pin number:")
        if pin=="3456":
            print("inprosses")
            account=input("salect the account ")
            if account=="seving account" or "currant account":
                print("inprosses")
                amount=input("enter the amount")
                if amount<="10000":
                    print("Collect your cash")
                    recpect=input("enter the recpect")
                    if recpect=="yes" or recpect=="no":
                        print("take the recpect") 
                        print("thank you baking") 
                    else:
                        print("ok good luck")
                        print("thank you for banking with as")
                else:
                    print("enter the currect amount")
            else:
                print("your account in ccurect try again")  
        else:
            print("try again pin") 
    else:
        print("your language is inccurect")
else:
    print("instart card again")                                          