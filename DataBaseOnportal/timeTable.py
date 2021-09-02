class TimeTable:
    def __init__(self, time_table_id=1, time_table_number=1, name="Workday"):
        self.__time_table_id = time_table_id
        self.__timeTableNumber = time_table_number
        self.__name = name

    def getTimeTableID(self):
        return self.__timeTableID

    def set_time_table_id(self, time_table_id):
        self.__time_table_id = time_table_id

    def getTimeTableNumber(self):
        return self.__timeTableNumber

    def set_time_table_number(self, time_table_number):
        self.__timeTableNumber = time_table_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

