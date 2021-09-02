class Role:
    def __init__(self, roleID = None, name = None, featureString = None, roleLevel = None, timeOut = None, authenticationType = None,
                 systemRole = None, lastModifiedBy = None, lastModified = None):
        self.__roleID = roleID
        self.__name = name
        self.__featureString = featureString
        self.__roleLevel = roleLevel
        self.__timeOut = timeOut
        self.__authenticationType = authenticationType
        self.__systemRole = systemRole
        self.__lastModifiedBy = lastModifiedBy
        self.__lastModified = lastModified

    def getRoleId(self):
        return self.__roleID

    def setRoleID(self, roleID):
        self.__roleID = roleID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getFeatureString(self):
        return self.__featureString

    def setFeatureString(self, featureString):
        self.__featureString = featureString

    def getRoleLevel(self):
        return self.__roleLevel

    def setRoleLevel(self, level):
        self.__level = level

    def getTimeOut(self):
        return self.__timeOut

    def setTimeOut(self, timeOut):
        self.__timeOut = timeOut

    def getAuthenticationType(self):
        return self.__authenticationType

    def setAuthentication(self, authenticationType):
        self.__authenticationType = authenticationType

    def getSystemRole(self):
        return self.__systemRole

    def setSystemRole(self, systemRole):
        self.__systemRole = systemRole

    def getLastModifiedBy(self):
        return self.__lastModifiedBy

    def setLastModifiedBy(self, lastModifiedBy):
        self.__lastModifiedBy = lastModifiedBy

    def getLastModified(self):
        return self.__lastModified

    def setLastModifed(self, lastModified):
        self.__lastModified = lastModified