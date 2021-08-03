class Atm:
    def __init__(self, card, pin):
        self.card = card
        self.pin = pin

    
    def checkBalance(self):
         print("Your balance is 50000")

    def withdrawal(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))


def main():
        cardVar = input("Please enter your card number: ")
        pinVar = input("Please enter your PIN: ")

        new_user =  Atm(cardVar ,pinVar)
            
        print("Choose your activity ")
        print("1.Balance Enquriy   2.withdrawl")
        activity = int(input("enter activity number :- "))

        if (activity == 1):
            new_user.check_balance()
        elif (activity == 2):
            amount = int(input("enter the amount:- "))
            new_user.withdrawal(amount)
  
if __name__ == "__main__":
    main()



