import enum

class CardType(enum.Enum):
    Credit = 0
    Debit = 1
    Payroll = 2

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


class Card:
    def __init__(
        self, 
        name: str = "Null", 
        date: Date = Date(1, 1, 2020),
        cardType: CardType = CardType.Payroll,
        stat: bool = True,
        balance: float = 0.0
    ):
        self._name = name
        self._date = date
        self._cardType = cardType
        self._status = stat 
        self._balance = balance

    def accountInfo(self) -> str:
        status: str = "Active" if self._status else "Deactivated"
        return ("Owner: " + self._name 
                + "\nStatus: " + status 
                + "\nCard Type: " + self._cardType.name)

    def statusUpdate(self, status: bool):
        stat: str = "Activated" if status else "Deactivated"
        if (status != self._status):
            self._status = status
            print("Account Name " + self._name + " is Succesfully " + stat)
        else:
            print ("Account is already " + stat)
    
    def checkBalance(self):
        print ("Current Balance: {} $".format(round(self._balance, 2)))

class Bank:
    def __init__(self, date: Date = Date(1, 1,2020)):
        self._accounts = {}
        self._currentDate = date

    def addAccount(self, acc: Card):
        if acc not in self._accounts:
            self._accounts[acc] = self._currentDate
            acc.date = self._currentDate #register its date with bank's current date

    def deleteAccount(self, acc: Card):
        if acc in self._accounts:
            self._accounts.pop(acc)
    
    def listAccounts(self, spec: str = "All"):
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

        for acc in self._accounts:
            if (acc._status == stat) or allStat:
                print ("Account Holder Since: " 
                        + self._accounts[acc].mdyFormat())
                print(acc.accountInfo() + "\n")

    def updateDate(self, date: Date):
        days = self._currentDate.daysGap(date)
        if days > 1:
            self._currentDate = date #updates the date
            for acc in self._accounts:
                if not isinstance(acc, Payroll):
                    acc.updateStanding(date) #update every cards' standing
                    acc.statusCheck()
        else:
            print("Can't Go Back Time")

class Withdraw(Card):
    def withdraw(self, amount: float):
        if not self._status:
            print ("Your account is deactivated.")
        elif (self._balance - amount) < 0:
            print ("Insufficient Funds")
        elif (amount <= 0):
            print ("Invalid Amount")
        else:  
            self._balance -= amount
            print ("Succesfully withdrawn: {} $".format(amount))
            self.checkBalance()

class Transfer(Card):
    def transfer(self, amount: int, card: Card) -> bool:
        if not self._status:
            print("Your Account is Deactivated")
        elif self._balance - amount < 0:
            print("Insuffecient Funds")
        elif not card._status:
            print("The Account to Recieve is Deactivated")
        elif amount <= 0:
             print("Invalid amount to Transfer")
        else:
            card._balance += amount
            out: str = ("Successfully Transferred " + str(amount) 
                    + "$ to:\n"+ format(card.accountInfo()))
            print(out)

class Deposit(Card):
    def deposit(self, amount: float):
        if self._status:
            self._balance += amount
        else:
            print("Account is Deactivated")

class Interest(Card):
    def __init__(
        self, 
        name: str = "Null", 
        date: Date = Date(1, 1, 2020),
        cardType: CardType = CardType.Payroll,
        stat: bool = True,
        initBalance: float = 0.0,
        interest: float = 0.02,
    ):
        Card.__init__(self, name, date, cardType, stat, initBalance)
        self._interest = interest
    
    def updateStanding(self, date: Date):
        months: float = self._date.daysGap(date) / 30
        if (months >= 0 and self._status):
            self._date = date   #updating new date
            newCredit: float = self._balance * ((1.0 + self._interest) ** months)
            self._balance = round(newCredit, 2)

class Payroll(Withdraw):
    pass
    
class Debit(Withdraw, Transfer, Deposit, Interest):
    def __init__(
        self, 
        name: str = "Null", 
        date: Date = Date(1, 1, 2020),
        stat: bool = True,
        initBalance: float = 0.0,
        reqBalance: float = 1000.0,
        interest: float = 0.02,
    ):
        Interest.__init__(self, name, date, CardType.Debit, stat, initBalance, interest)
        self._reqBalance = reqBalance
    
    def statusCheck(self):
        if self._balance < self._reqBalance:
            self.statusUpdate(False)

class Credit(Withdraw, Transfer, Deposit, Interest):
    def __init__(
        self, 
        name:str = "Null", 
        date:Date = Date(1, 1, 2020),
        stat: bool = True,
        initBalance: float = 0.0,
        limit: float = 10000.0,
        interest: float = 0.02,
    ):
        Interest.__init__(self, name, date, CardType.Credit, stat, initBalance, interest)
        self._limit = limit

    def withdraw(self, amount: float):
        if not self._status:
            print ("Your account is deactivated.")
        elif self._balance - amount < -self._limit:
            print("Reached the Limit")
        elif (amount <= 0):
            print ("Invalid Amount")
        else:  
            self._balance -= amount
            print ("Succesfully withdrawn: {} $".format(amount))
            self.checkBalance()
    
    def statusCheck(self):
        if self._balance < -self._limit:
            self.statusUpdate(False)


person1 = Credit(name="Cyrus", date=Date(1, 1, 2021), initBalance=1000, limit=1000, interest=0.10)
person2 = Payroll(name="David")
person3 = Debit(name="Naruto")
CDP = Bank()
CDP.addAccount(person1)
CDP.addAccount(person2)
CDP.addAccount(person3)
CDP.listAccounts()
person1.transfer(1000, person3)
CDP.updateDate(Date(1,1,2021))
person3.checkBalance()
person1.checkBalance()