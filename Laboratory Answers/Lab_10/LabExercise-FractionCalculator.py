from abc import ABC, abstractmethod

class Fraction:
    def __init__(self, num:int,denom:int):
        self.__num = num
        self.__denom = denom

    def num(self):
        return self.__num

    def denom(self):
        return self.__denom

    def __str__(self) -> str:
        return str(self.__num) + "/" + str(self.__denom)
    
    def simplify(self):
        if self.denom() == 0:
            raise "Denominator cannot be Zero"
        if self.num() == 0:
            return 0
        else:
            divisor: int = min(abs(self.num()), abs(self.denom()))
            while divisor > 2:
                if (self.num() % divisor == 0 and self.denom() % divisor == 0):
                    if (self.denom()/divisor == 1):
                        return int(self.num()/divisor)
                    else:
                        return Fraction(int(self.num()/divisor), int(self.denom()/divisor))
                divisor -= 1
            return self

class Operation(ABC):
    @abstractmethod
    def execute(self, left: Fraction, right: Fraction):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Addition(Operation):
    def __str__(self) -> str:
        return "+" 
    def execute(self, left: Fraction, right: Fraction) -> Fraction:
        newDenom = right.denom() * left.denom()
        newNum = right.denom() * left.num() + left.denom() * right.num()
        return Fraction(newNum, newDenom).simplify()

class Subtraction(Operation):
    def __str__(self) -> str:
        return "-"

    def execute(self, left: Fraction, right: Fraction) -> Fraction:
        newDenom = right.denom() * left.denom()
        newNum = right.denom() * left.num() - left.denom() * right.num()
        return Fraction(newNum, newDenom).simplify()

class Multiplication(Operation):
    def __str__(self) -> str:
        return "*" 

    def execute(self, left: Fraction, right: Fraction) -> Fraction:
        newDenom = right.denom() * left.denom()
        newNum = right.num() * left.num()
        return Fraction(newNum, newDenom).simplify()

class Division(Operation):
    def __str__(self) -> str:
        return "/" 

    def execute(self, left: Fraction, right: Fraction) -> Fraction:
        newDenom = left.denom() * right.num()
        newNum = left.num() * right.denom()
        return Fraction(newNum, newDenom).simplify()

class Calculation:
    def __init__(self, left: Fraction, right: Fraction, operation: Operation): #will cause an error when ran since Operation does not exist yet
        self.__left = left
        self.__right = right
        self.__operation = operation #the parameter that represents the operation
        self.__answer = operation.execute(left, right)

    def __str__(self):
        return str(self.__left) + " " + str(self.__operation) + " " + str(self.__right) + " = " + str(self.__answer)


def main():
    f1: Fraction = Fraction(0,4)
    f2: Fraction = Fraction(2,5)
    f3: Fraction = Fraction(0,1)
    f4: Fraction = Fraction(15,5)
    f5: Fraction = Fraction(30,6)

    print(Calculation(f1,f3,Addition()))
    print(Calculation(f2,f1,Subtraction()))
    print(Calculation(f2,f1,Multiplication()))
    print(Calculation(f3,f2,Multiplication()))

    print(Calculation(f4,f5,Addition()))
    print(Calculation(f4,f5,Subtraction()))
    print(Calculation(f4,f5,Division()))
    print(Calculation(f4,f5,Multiplication()))
    # print(Calculation(f3,f1,Division())) // undefined

if __name__ == "__main__":
    main()