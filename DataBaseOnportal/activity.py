class Activity:
    def __init__(self, activityID, auditOperation, activityTime, roomName, auditCode, auditOperationAddedNumber, auditReject,
                 masterUserName, keyCodeName, cardType, cardStartDate, cardEncodeBy, readTime, uploadTime, cardAuthorizations):
        self.__activityID = activityID
        self.__auditOperation = auditOperation
        self.__activityTime = activityTime
        self.__roomName = roomName
        self.__auditCode = auditCode
        self.__auditOperationAddedNumber = auditOperationAddedNumber
        self.__auditReject = auditReject
        self.__masterUserName = masterUserName
        self.__keyCodeName = keyCodeName
        self.__cardType = cardType
        self.__cardStartDate = cardStartDate
        self.__cardEncodeBy = cardEncodeBy
        self.__readTime = readTime
        self.__uploadTime = uploadTime
        self.__cardAuthorizations = cardAuthorizations

    def getactivityID(self):
        return self.__activityID

    def setActivityID(self, activityID):
        self.__activityID = activityID

    def getAuditOperation(self):
        return self.__auditOperation

    def setAuditOperation(self, auditOperation):
        self.__auditOperation = auditOperation

    def getInsertString(self):
        query = "INSERT INTO LockProfile(Name, Description, TimeTableID, RequiredAuthID, OfficeMode, AllowProgrammingCard, DoorOpenTime, " \
                "GuestSequenceNumberLookAhead, MasterSequenceNumberLookAhead, OpenOnWithdrawl, ShowLowBattery, CloseOnLever, IsADA, DefaultCardAuthsString, " \
                "OptionalCardAuthsString, Shift, Privacy) VALUES ('%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '%s', '%s', %s, %s)" % (
                self.__name,
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