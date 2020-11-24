from abc import ABC, abstractmethod

class Headline:
    def __init__(self, headline:str, details:str, source:str):
        self.__headline = headline
        self.__details = details
        self.__source = source

    def __str__(self) -> str:
        return "%s(%s)\n%s" % (self.__headline, self.__source, self.__source)

class Weather:
    def __init__(self, temp:float, humidity:float, outlook:str):
        self.__temp = temp
        self.__humidity = humidity
        self.__outlook = outlook

    def __str__(self) -> str:
        return "%s: %.1fC %.1f" % (self.__outlook, self.__temp, self.__humidity)


class Subscriber(ABC):
    @abstractmethod
    def update(self):
        pass

class PushNotifier:
    def __init__(self, currHeadline: Headline, weather: Weather):
        self.__currWeather = weather
        self.__currHeadline = currHeadline
        self.__subscribers = []
    
    def changeHeadline(self):
        headline: str = input("Enter New Headline: ")
        details: str = input("Enter the Details: ")
        source: str = input("Cite the Source: ")
        self.__currHeadline = Headline(headline, details, source)
        self.notifySubscribers()

    def changeWeather(self):
        temp:float = float(input("Enter the Temperature: "))
        humidity:float = float(input("Enter the Humidity: "))
        outlook:str = input("Enthr the outlook: ")
        self.__currWeather = Weather(temp, humidity, outlook)
        self.notifySubscribers()

    def subscribe(self, newSubscriber: Subscriber):
        self.__subscribers.append(newSubscriber)
        newSubscriber.update(self.__currHeadline, self.__currWeather)

    def unsubscribe(self, exSubscriber: Subscriber):
        if exSubscriber in self.__subscribers:
            self.__subscribers.remove(exSubscriber)
    
    def notifySubscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update(self.__currHeadline, self.__currWeather)

class EmailSubscriber(Subscriber):
    def __init__(self, emailAdress: str):
        self.__emailAddress = emailAdress
        self.__weather = None
        self.__headline = None

    def update(self, newHeadline: Headline, newWeather: Weather):
        self.__headline = newHeadline
        self.__weather = newWeather
        print("Headline: " + str(self.__headline) +
              "Weather: " + str(self.__weather) + "\n")


class FileLogger(Subscriber):
    def __init__(self, filename: str):
        self.__file = open(filename, "w+")
        self.__weather = None
        self.__headline = None
    
    def update(self, newHeadline: Headline, newWeather: Weather):
        self.__headline = newHeadline
        self.__weather = newWeather
        self.__file.write("Headline: " + str(self.__headline) +
                          "Weather: " + str(self.__weather) + "\n\n")

def main():
    h = Headline("Dalai Lama Triumphantly Names Successor After Discovering Woman With ‘The Purpose Of Our Lives Is To Be Happy’ Twitter Bio","Details","The Onion")
    w = Weather(25.0,0.7,"Cloudy")
    app = PushNotifier(h, w)

    person1 = EmailSubscriber("cyrusdavidp@gmail.com")
    file1 = FileLogger("log.in")

    app.subscribe(file1)
    app.subscribe(person1)
    app.changeHeadline()
    app.changeWeather()

if __name__ == "__main__":
    main()