class Hotel:

    def __init__(self):
        self.__name = "None"
        self.__adress = "None"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAdress(self, adress):
        self.__adress=adress

    def getAdress(self):
        return self.__adress