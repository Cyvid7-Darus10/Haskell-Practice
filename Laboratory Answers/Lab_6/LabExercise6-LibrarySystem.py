from abc import ABC, abstractmethod

'''
  --------Lab Exercise 6 (Library System)-------
  Name: Cyrus David G. Pastelero
  Subject: Programming Paradigms
  Section: A
  Date: Nov 8, 2020
  ----------------------------------------------
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

    def daysGap(self, today: Date) -> int:
        months:[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days:[int] = (today.__year - self.__year)* 365

        for month in range(self.__month - 1, today.__month - 1):
            days += months[month]

        days += today.__day - self.__day
        return days


class Page:
    def __init__(self, sectionHeader: str, body: str):
        self.__sectionHeader = sectionHeader
        self.__body = body


class BorrowableItem(ABC):
    @abstractmethod
    def uniqueItemId(self) -> int:
        pass
    
    @abstractmethod
    def commonName(self) -> str:
        pass


class Book(BorrowableItem):
    def __init__(self, bookId:int, title:str, 
                author:str, publishDate:Date, pages:[Page]):
        self.__bookId = bookId
        self.__title = title
        self.__publishDate = publishDate
        self.__author = author
        self.__pages = pages
    
    def coverInfo(self) -> str:
        return "Title: " + self.__title + "\nAuthor: " + self.__author
    
    def uniqueItemId(self) -> int:
        return self.__bookId
    
    def commonName(self) -> str:
        return "Borrowed Item:" + self.__title + " by " + self.__author


class Periodical(BorrowableItem):
    def __init__(self, periodicalID:int, title:str, issue:Date, pages:[Page]):
        self.__periodicalID = periodicalID
        self.__title = title
        self.__issue = issue
        self.__pages = pages
    
    def uniqueItemId(self) -> int:
        return self.__periodicalID
    
    def commonName(self) -> str:
        return self.__title + " issue: " + str(self.__periodicalID)


class PC(BorrowableItem):
    def __init__(self, pcID:int):
        self.__pcID = pcID
    
    def uniqueItemId(self) -> int:
        return self.__pcID
    
    def commonName(self) -> str:
        return "PC" + str(self.__pcID)


class LibraryCard:
    def __init__(self, idNumber: int, name: str, 
                borrowedItems: {BorrowableItem:Date}):
        self.__idNumber = idNumber
        self.__name = name
        self.__borrowedItems = borrowedItems
    
    def borrowItem(self, item:BorrowableItem, date:Date):
        self.__borrowedItems[item] = date
    
    def borrowerReport(self) -> str:
        r:str = self.__name + "\n"
        
        for borrowedItem in self.__borrowedItems:
            r += (borrowedItem.commonName() 
                + ", borrow date:" 
                + self.__borrowedItems[borrowedItem].mdyFormat() 
                + "\n")

        return r
    
    def returnItem(self, b:BorrowableItem):
        if b in self.__borrowedItems:
            self.__borrowedItems.pop(b)
    
    def penalty(self, b:BorrowableItem, today:Date) -> float:
        if b in self.__borrowedItems:
            days:float = float(self.__borrowedItems[b].daysGap(today))
            if isinstance(b, PC):
                return days * 3.5
            elif isinstance (b, Book):
                return (days - 7.0) * 3.5 if days - 7.0 > 0 else 0
            return (days - 1.0) * 3.5 if days - 1.0 > 0 else 0      #Periodical
    
    def itemDue(self, today:Date) -> [BorrowableItem]:
        dueItems:[BorrowableItem] = []

        for item in self.__borrowedItems:
            if (self.penalty(item, today) > 0):
                dueItems.append(item)

        return dueItems
    
    def totalPenalty(self, today:Date) -> float:
        total:float = 0.0

        for item in self.__borrowedItems:
            total += self.penalty(item, today)

        return total


b:BorrowableItem = Book(10991,"Corpus Hermeticum", "Hermes Trismegistus", Date(9,1,1991), [])
print(b.commonName()) #commonName() returns the string representation of a borrowable item
l:LibraryCard = LibraryCard(9982,"Rubelito Abella",{})
l.borrowItem(b,Date(1,22,2019))

Asus:BorrowableItem = PC(1234)

magazine:BorrowableItem = Periodical(12, "Geographic", Date(9,27,2019), [])
l.borrowItem(magazine, Date(1,2,2019))

print(l.borrowerReport())
print(l.penalty(b, Date(10,22,2019)))
print(l.itemDue(Date(9,26,2020)))
print(l.penalty(Asus, Date(10,22,2019)))
l.returnItem(b)
print(l.borrowerReport())
