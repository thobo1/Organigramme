import datetime

class KeyCode:

    def __init__(self, keyCodeId = None, name = None, codeType = None, description = None, sequenceNumber = None ):
        self.__keyCodeId = keyCodeId
        self.__name = name
        self.__codeType = codeType
        self.__description = description
        self.__sequenceNumber = sequenceNumber
        self.__modifiedDate = datetime.datetime.now()

    def setKeyCodeId(self, keyCodeId):
        self.__keyCodeId = keyCodeId

    def getKeyCodeId(self):
        return self.__keyCodeId

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setcodeType(self, codeType):
        self.__codeType = codeType

    def getCodeType(self):
        return self.__codeType

    def setDescription(self, description):
        self.__description = description

    def getDescription(self):
        return self.__description

    def getSequenceNumber(self):
        return self.__sequenceNumber

    def setSequenceNumber(self, sequenceNumber):
        self.__sequenceNumber = sequenceNumber

    def getModifiedDate(self):
        return self.__modifiedDate

    def setModifiedDate(self,modifiedDate):
        self.__modifiedDate = modifiedDate


    def getInsertString(self):
            query = "INSERT INTO LockProfile(Name, CodeType, Description, SequenceNumber, ModifiedDate) VALUES ('%s', %s, '%s', %s, '%s')" % (
                self.__name,
                self.__codeType,
                self.__description,
                self.__sequenceNumber,
                self.__modifiedDate,
            )
            return query

