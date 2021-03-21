print("Welcome to the Toronto Bank.")

class atm:
    def __init__(self,cardNo,pin):
        self.cardNo=cardNo
        self.pin=pin

    def check_balance(self):
        print("Your balance is 50K.")
      
    def withdrawl(self,amount):
        if amount<50000:
            new_amount=50000-amount
            print("You have withdrawn $" + str(amount)+ ". Your remaining balance is $ "+str(new_amount))
        elif amount>50000:
            print("Insufficient funds!")
            amount=int(input("Please enter amount again: "))
            new_amount=50000-amount
            print("You have withdrawn $" + str(amount)+ ". Your remaining balance is $ "+str(new_amount))
            
    
def main():
    card_number=(input("Insert card number: "))
    pin_number=(input("Insert pin number: "))
    new_user=atm(card_number, pin_number)

    print("Please choose your activity")
    print("1)Balance enquiry 2)Withdrawl")
    activity=int(input("Enter activity number: "))

    if(activity==1):
        new_user.check_balance()
    elif(activity==2): 
        amount=int(input("Enter amount: "))
        new_user.withdrawl(amount)
    #If a person chooses a wrong number, then the function should happen again.
    else:
        print("Please enter a valid number!")
        activity=int(input("Enter activity number: "))
        if(activity==1):
            new_user.check_balance()
        elif(activity==2): 
            amount=int(input("Enter amount: "))
            new_user.withdrawl(amount)

if __name__=="__main__":
    main()