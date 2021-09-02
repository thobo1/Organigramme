class LockProfile_KeyCode:

    def __init__(self, lockProfileID = None, keyCodeID = None):
        self.__lockProfileID = lockProfileID
        self.__keyCodeID = keyCodeID

    def getInsertString(self):
        query = "INSERT INTO LockProfile_KeyCode(LockProfileID, KeyCodeID) VALUES (%s, %s)" % (
            self.__lockProfileID,
            self.__keyCodeID)
        return query