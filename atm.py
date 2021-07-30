class ATM():
    def __init__(self, user, card, pin, balance):
        self.user = user
        self.card = card
        self.pin = pin
        self.balance = balance

    def getUser(self):
        return self.user
    
    def checkBalance(self):
        return self.balance
    
    def login(self):
        cardVar = input("Please enter your card number: ")

        if cardVar == self.card:
            pinVar = input("Please enter your PIN: ")
            
            if pinVar == self.pin:
                print("Successfully logged in")
                print("Current User: "+John.getUser())
                print("Current Balance: "+John.checkBalance())

            else:
                print("Incorrect PIN")
        
        else:
            print("Sorry, that card could not be located on our database")


John = ATM("John", 123456, 1111, "$1000")

John.login()



