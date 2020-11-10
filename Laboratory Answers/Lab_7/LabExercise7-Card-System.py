from abc import ABC, abstractmethod
'''
  --------Lab Exercise 7 (Designing an OOP System)-------
  Owner: Cyrus David G. Pastelero
  Subject: Programming Paradigms
  Section: A
  Date: Nov 8, 2020
  -------------------------------------------------------
'''

class Date:
    def __init__(self, month: int, day: int, year: int):
        self.__month = month
        self.__day = day
        self.__year = year
    
    def mdyFormat(self) -> str:
        return (str(self.__month) 
                + "/" + str(self.__day) 
                + "/" + str(self.__year))

    def daysGap(self, today) -> int:
        months: [int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days: int = (today.__year - self.__year)* 365

        for month in range(self.__month - 1, today.__month - 1):
            days += months[month]

        days += today.__day - self.__day
        return days


class Card(ABC):
    def __init__(self, name:str, date:Date):
        self.name = name
        self.status = True  #True - Active, else False
        self.date = date

    @abstractmethod
    def withdraw(self, amount: int) -> bool:
        pass

    @abstractmethod
    def checkBalance(self) -> str:
        pass

    def accountInfo(self) -> str:
        status: str = "Active" if self.status else "Deactivated"

        if isinstance(self, Credit):
            cType: str = "Credit"
        elif isinstance(self, Debit):
            cType: str = "Debit"
        else:
            cType: str = "Payroll"

        return ("Owner: " + self.name 
                + "\nStatus: " + status 
                + "\nCard Type: " + cType)

    def statusUpdate(self, status: bool):
        stat: str = "Activated" if status else "Deactivated"
        if (status != self.status):
            self.status = status
            print("Account is Succesfully " + stat)
        else:
            print ("Account is already " + stat)


class BankOfCyrus:
    def __init__(self, date: Date):
        self.accounts = {}
        self.currentDate = date

    def addAccount(self, acc: Card):
        if acc not in self.accounts:
            self.accounts[acc] = self.currentDate
            acc.date = self.currentDate #register its date with bank's current date

    def deleteAccount(self, acc: Card):
        if acc in self.accounts:
            self.accounts.pop(acc)
    
    def listAccounts(self, spec: str):
        allStat: bool = False
        stat: bool = False
        if spec.lower() == "inactive":
            stat: bool = False
        elif spec.lower() == "active":
            stat: bool = True
        elif spec.lower() == "all":
            allStat: bool = True
        else:
            print ("INVALID")
            return

        for acc in self.accounts:
            if (acc.status == stat) or allStat:
                print ("Account Holder Since: " 
                        + self.accounts[acc].mdyFormat())
                print(acc.accountInfo() + "\n")

    def updateDate(self, date: Date):
        self.currentDate = date #updates the date
        for acc in self.accounts:
            if not isinstance(acc, Payroll):
                acc.updateStanding(date) #update every cards' standing



class Payroll(Card):
    def __init__(self, name: str, date: Date):
        Card.__init__(self, name, date) #inherit
        self.balance = 0

    def withdraw(self, amount: float):
        if not self.status:
            print ("Your account is deactivated.")
        elif (self.balance - amount) < 0:
            print ("Insufficient Funds")
        elif (amount <= 0):
            print ("Invalid Amount")
        else:  
            self.balance -= amount
            print ("Succesfully withdrawn: {} $".format(amount))
            self.checkBalance()

    def checkBalance(self):
        print ("Current Balance: {} $".format(round(self.balance, 2)))

    
class Debit(Card):
    def __init__(self, name: str, initBalance: float, version: str, date: Date):
        Card.__init__(self, name, date)

        self.reqBalance = 1000
        self.interest = 0.02
        self.balance = initBalance

    def withdraw(self, amount:int) -> bool:
        if self.status:
            if self.balance - amount >= 0 and amount > 0:
                self.balance -= amount
                print ("Succesfully withdrawn: {} $".format(amount))
                print ("Current Blanance: {} $".format(self.balance))
                return True
            else:
                print ("amount is Invalid")
        else:
            return False

    def transfer(self, amount: int, card: Card) -> bool:
        if (self.status and self.balance - amount >= 0 
            and card.status and amount > 0):
            if isinstance(card, Credit):
                card.credit -= amount
                if card.credit < card.limit and not card.status:
                    card.statusUpdate(True) #If deactivated, activate
            else:
                card.balance += amount
                if isinstance(card, Debit) and not card.status:
                    if card.balance >= card.reqBalance:
                        card.statusUpdate(True) #If deactivated, activate

            self.balance -= amount 
            out: str = ("Successfully Transferred " + str(amount) 
                    + "$ to:\n"+ format(card.accountInfo()))
            print(out)
            return True
        else:
            if self.balance - amount < 0:
                print("Out of Limit")
            elif not self.status:
                print("Your Account is Deactivated")
            elif not card.status:
                print("The Account to Recieve is Deactivated")
            else:
                print("Invalid amount to Transfer")
            return False

    def checkBalance(self):
        return "Current Balance: " + str(self.balance) + "$"
    
    def updateStanding(self, date: Date) -> bool:
        months: float = self.date.daysGap(date) / 30
        if (months >= 0 and self.status):
            self.date = date   #updating new date

            if self.balance < self.reqBalance and months > 0 :
                self.statusUpdate(False)
                return False

            newBalance: float = self.balance * ((1.0 + self.interest) ** months)
            self.balance = round(newBalance,2)

            return True
        else:
            return False
            


class Credit(Card):
    def __init__(self, name: str, version: str, date: Date):
        Card.__init__(self, name, date)

        self.credit = 0.0
        self.limit = 10000
        self.interest = 0.02

    def withdraw(self, amount: int) -> bool:
        if self.status:
            if self.credit + amount <= self.limit and amount > 0:
                self.credit += amount
                print ("Succesfully withdrawn: {} $".format(amount))
                print ("Current Credit: {} $".format(self.credit))
                return True
            else:
                print ("amount is Invalid")
        else:
            return False
 
    def transfer(self, amount: int, card: Card) -> bool:
        if (self.status and self.credit + amount <= self.limit
            and card.status and amount > 0):
            if isinstance(card, Credit):
                card.credit -= amount
                if card.credit < card.limit and not card.status:
                    card.statusUpdate(True) #If account was deactivated, activate
            else:
                card.balance += amount
                if isinstance(card, Debit) and not card.status:
                    if card.balance >= card.reqBalance:
                        card.statusUpdate(True) #If account was deactivated, activate
                        
            self.credit += amount #increase the credit(Debt)
            out:str = ("Successfully Transferred " + str(amount) 
                    + "$ to:\n"+ format(card.accountInfo()))
            print(out)
            return True
        else:
            if self.credit + amount > self.limit:
                print("Out of Limit")
            elif not self.status:
                print("Your Account is Deactivated")
            elif not card.status:
                print("The Account to Recieve is Deactivated")
            else:
                print("Invalid amount to Transfer")
            return False
    
    def checkBalance(self, date: Date):
            return "Current Credit: " + str(self.credit) + "$"
    
    def updateStanding(self, date: Date) -> bool:
        months: float = self.date.daysGap(date) / 30
        if (months >= 0 and self.status):
            self.date = date   #updating new date
            
            newCredit: float = self.credit * ((1.0 + self.interest) ** months)
            
            self.credit = round(newCredit, 2)
            if self.credit > self.limit:
                self.statusUpdate(False)
            return True
        else:
            return False

#List Cards made
card1:Card = Payroll("Person 1", Date(1,1,2020))
card2:Card = Debit("Person 2", 1000, "senior", Date(1,1,2020))
card3:Card = Debit("Person 3", 1000, "junior", Date(1,1,2020))
card4:Card = Credit("Person 4", "premium", Date(1,1,2020))
card5:Card = Credit("Person 5", "regular", Date(1,1,2020))
print(card1.accountInfo()) #person 1 checks his account
print(card1.date.mdyFormat()) #The date he made his account

print("\n")
#A banking busines has arised and person 1 is the first costumer
CDP: BankOfCyrus = BankOfCyrus(Date(1,2,2020))
CDP.addAccount(card1)
CDP.addAccount(card2) #person two registered his account to the new bank
CDP.addAccount(card3) #persone three followed
CDP.listAccounts("All") #List all current bank's costumer


print(card1.accountInfo()) #Person 1 checked his account
print(card1.date.mdyFormat()) #His account's date was updated
card1.withdraw(0) #
card1.checkBalance()

print("\n" + card2.accountInfo()) #Person 2 checks her account
card2.withdraw(100) #Withdrawn 100$

card2.checkBalance()
card2.checkBalance()
print(card2.transfer(120, card1))
card2.checkBalance()
print(card2.transfer(120, card3))

print("\n" + card1.accountInfo())
card1.checkBalance()
card1.withdraw(100)


print("\n" + card3.accountInfo())
card3.withdraw(100)

print("\nAfter one year:\n")
CDP.updateDate(Date(1,2,2021)) #One year has passed
CDP.addAccount(card4) #new account
CDP.addAccount(card5) #new account
card1.statusUpdate(False) # Deactivate person 1
print("\n")

# CDP.listAccounts("inactive")

CDP.listAccounts("active")

card1.statusUpdate(True) # Activate person 1 again
CDP.listAccounts("sdkjhal") # wrong specification
