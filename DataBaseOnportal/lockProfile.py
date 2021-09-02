class LockProfile:

    def __init__(self, lockProfileID = None, name = None, description = "", timeTableID = 1, requiredAuthID = 0, officeMode = 0, allowProgrammingCard = 1,
                 doorOpenTime = 3, guestSequenceNumberLookAhead = 100, masterSequenceNumberLookAhead = 25, openOnWithdrawl = 0, showLowBattery = 0,
                 closeOnLever = 1, isADA = 0, defaultCardAuthsString = "", optionalCardAuthsString = "", shift = 0, privacy = 1):
        self.__lockProfileID = lockProfileID
        self.__name = name
        self.__description = description
        self.__timeTableID = timeTableID
        self.__requiredAuthID = requiredAuthID
        self.__officeMode = officeMode
        self.__allowProgrammingCard = allowProgrammingCard
        self.__doorOpenTime = doorOpenTime
        self.__guestSequenceNumberLookAhead = guestSequenceNumberLookAhead
        self.__masterSequenceNumberLookAhead = masterSequenceNumberLookAhead
        self.__openOnWithdrawl = openOnWithdrawl
        self.__showLowBattery = showLowBattery
        self.__closeOnLever = closeOnLever
        self.__isADA = isADA
        self.__defaultCardAuthsString = defaultCardAuthsString
        self.__optionalCardAuthsString = optionalCardAuthsString
        self.__shift = shift
        self.__privacy = privacy

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getInsertString(self):
        query = "INSERT INTO LockProfile(Name, Description, TimeTableID, RequiredAuthID, OfficeMode, AllowProgrammingCard, DoorOpenTime, " \
                "GuestSequenceNumberLookAhead, MasterSequenceNumberLookAhead, OpenOnWithdrawl, ShowLowBattery, CloseOnLever, IsADA, DefaultCardAuthsString, " \
                "OptionalCardAuthsString, Shift, Privacy) VALUES ('%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%s', '%s', %s, %s)"%(self.__name,
                                                                                                                                                self.__description,
                                                                                                                                                self.__timeTableID,
                                                                                                                                                self.__requiredAuthID,
                                                                                                                                                self.__officeMode,
                                                                                                                                                self.__allowProgrammingCard,
                                                                                                                                                self.__doorOpenTime,
                                                                                                                                                self.__guestSequenceNumberLookAhead,
                                                                                                                                                self.__masterSequenceNumberLookAhead,
                                                                                                                                                self.__openOnWithdrawl,
                                                                                                                                                self.__showLowBattery,
                                                                                                                                                self.__closeOnLever,
                                                                                                                                                self.__isADA,
                                                                                                                                                self.__defaultCardAuthsString,
                                                                                                                                                self.__optionalCardAuthsString,
                                                                                                                                                self.__shift,
                                                                                                                                                self.__privacy)
        return query




