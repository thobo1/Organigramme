import datetime


class Room:
    def __init__(self, name=None, description=None, type=1, status=1, must_be_updated=1,
                 needs_reinitialize=0,
                 has_been_synced=0, audit_code=0, lockProfilID=1, timeTableID=None, requiredAuthID=None, officeMode=None,
                 allowProgrammingCard=None,
                 isAda=None, doorOpenTime=None, guestSequenceNumerLookAhed=None, masterSequenceNumberLookAhead=None,
                 openOnWithdrawl=None, closeOnLever=None,
                 lastUpdated=None, has_been_initialized=0, defaultCardAuthsString=None, optionalCardAuthsString=None,
                 shift=None, privacy=None,
                 defaultMasterKeyCodeID=None, include_suite_key_code=0, attribute=0, customField1=None,
                 customField2=None, primaryKeyCode_KeyCodeID=0,
                 serialNumber=None):
        self.__roomId = 0
        self.__name = name
        self.__description = description
        self.__type = type
        self.__status = status
        self.__must_be_updated = must_be_updated
        self.__needs_reinitialize = needs_reinitialize
        self.__has_been_synced = has_been_synced
        self.__audit_code = audit_code
        self.__lockProfilID = lockProfilID
        self.__timeTableID = timeTableID
        self.__requiredAuthId = requiredAuthID
        self.__officeMode = officeMode
        self.__allowProgrammingCard = allowProgrammingCard
        self.__isAda = isAda
        self.__doorOpenTime = doorOpenTime
        self.__guestSequenceNumberLookAhead = guestSequenceNumerLookAhed
        self.__masterSequenceNumberLookAhead = masterSequenceNumberLookAhead
        self.__openOnWithdrawal = openOnWithdrawl
        self.__closeOnLever = closeOnLever
        self.__lastModified = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__lastUpdated = lastUpdated
        self.__has_been_initialized = has_been_initialized
        self.__defaultCardAuthsSting = defaultCardAuthsString
        self.__optionalCardAuthsString = optionalCardAuthsString
        self.__shift = shift
        self.__privacy = privacy
        self.__defaultMasterKeyCodeID = defaultMasterKeyCodeID
        self.__includeS_suite_key_code = include_suite_key_code
        self.__attribute = attribute
        self.__custom_field1 = customField1
        self.__custom_field2 = customField2
        self.__primary_key_code_key_code_id = primaryKeyCode_KeyCodeID
        self.__serial_number = serialNumber
        self.__commit = False

    def get_inset_string(self):
        query = "INSERT INTO Room(Name, Type, Status, __must_be_updated, needs_reinitialize, has_been_synced, audit_code, LockProfileID," \
                " LastModified, HasBeenInitialized, include_suite_key_code, Attribute, PrimaryKeyCode_KeyCodeID VALUES ('%s', %s, %s, %s, %s, %s," \
                " %s, %s, '%s', %s, %s, %s, %s)" % (
                    self.__name,
                    self.__type,
                    self.__status,
                    self.__must_be_updated,
                    self.__must_be_updated,
                    self.__needs_reinitialize,
                    self.__has_been_synced,
                    self.__audit_code,
                    self.__lockProfilID,
                    self.__lastModified,
                    self.__has_been_initialized,
                    self.__includeS_suite_key_code,
                    self.__attribute,
                    self.__primary_key_code_key_code_id)

    def set_commit(self, commit):
        self.__commit = commit

    def set_audit_code(self, audit_code):
        self.__audit_code = audit_code

    def set_primary_key_code_key_code_id(self, primary_key_code_key_code_id):
        self.__primary_key_code_key_code_id = primary_key_code_key_code_id
