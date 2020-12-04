from abc import ABC, abstractmethod

class Headline:
    def __init__(self, headline:str, details:str, source:str):
        self.__headline = headline
        self.__details = details
        self.__source = source

    def __str__(self) -> str:
        return "%s(%s)\n%s" % (self.__headline, self.__source, self.__details)


class Weather:
    def __init__(self, temp:float, humidity:float, outlook:str):
        self.__temp = temp
        self.__humidity = humidity
        self.__outlook = outlook

    def __str__(self) -> str:
        return "%s: %.1fC %.1f" % (self.__outlook, self.__temp, self.__humidity)


class Subscriber(ABC):
    @abstractmethod
    def update(self, newHeadline: Headline, newWeather: Weather):
        pass


class PushNotifier:
    def __init__(self, currHeadline: Headline, weather: Weather):
        self.__currWeather = weather
        self.__currHeadline = currHeadline
        self.__subscribers = []
    
    def changeHeadline(self, newHeadline: Headline):
        self.__currHeadline = newHeadline
        self.notifySubscribers()
        
    def changeWeather(self, newWeather: Weather):
        self.__currWeather = newWeather
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
    h1 = Headline("Dalai Lama Triumphantly Names Successor After Discovering Woman With ‘The Purpose Of Our Lives Is To Be Happy’ Twitter Bio","Details","The Onion")
    w1 = Weather(25.0,0.7,"Cloudy")

    app = PushNotifier(h1, w1)
    
    person1 = EmailSubscriber("cyrusdavidp@gmail.com")
    file1 = FileLogger("log.in")

    app.subscribe(file1)
    app.subscribe(person1)

    h2 = Headline("We Can Do This Together!’ Nice Bio","Details are Stonks","The Garlic")
    w2 = Weather(40.0,1.9,"Sunny")

    app.changeHeadline(h2)
    app.changeWeather(w2)

if __name__ == "__main__":
    main()
