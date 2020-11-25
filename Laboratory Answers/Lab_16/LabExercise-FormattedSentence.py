from abc import ABC,abstractmethod

class Sentence:
    def __init__(self,words:[str]):
        self.__words = words

    def __str__(self) -> str:
        sentenceString = ""
        for word in self.__words:
            sentenceString += word + " "
        return sentenceString[:-1]

class FormattedSentence(ABC):
    def __init__(self, wrappedSentence: Sentence):
        self._wrappedSentence = str(wrappedSentence)

    @abstractmethod
    def __str__(self) -> str:
        pass

class BorderedSentence(FormattedSentence):
    def __str__(self) -> str:
        ceiling: str = "-" * (len(self._wrappedSentence) + 2)
        return ceiling + "\n|" + self._wrappedSentence + "|\n" + ceiling

class FancySentence(FormattedSentence):
    def __str__(self) -> str:
        return "-+" + self._wrappedSentence + "+-"

class UpperSentence(FormattedSentence):
    def __str__(self) -> str:
        return self._wrappedSentence.upper()

def main():
    A = Sentence(["You", "Are", "Destined", "To", "Die"])
    print(A)
    print()
    
    B = BorderedSentence(A)
    print(B)
    print()

    B = UpperSentence(A)
    print(B)
    print()

    B = FancySentence(A)
    print(B)
    print()

    B = BorderedSentence(FancySentence(UpperSentence(A)))
    print(B)
    print()
    
        
if __name__ == "__main__":
    main()