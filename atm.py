class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber,
        self.pinNumber = pinNumber

    def balanceEnquiry(self):
        print("Your available balance is 1,00,000")
        
    def cashWithdrawal(self, cash):
        balance = 100000 - cash
        print("₹", str(cash), "has been withdrawn")
        print("The remaining balance is ₹", str(balance))

if __name__ == "__main__":
    x  = int(input('Enter Card Number: '))
    y = int(input("Enter your PIN: "))

    myCard = Atm(x,y)

    y = input("Do you want to know your balance(enter b) or do you want to withdraw cash(enter c): ")

    if y == "b" or y == "B":
        myCard.balanceEnquiry()
    elif y == "c" or y == "C":
        z = int(input("Enetr amount of cash: "))
        myCard.cashWithdrawal(z)
