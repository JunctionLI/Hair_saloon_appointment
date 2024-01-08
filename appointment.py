class Appointment:
    def __init__(self,day_of_week,start_time_hour,client_name="",client_phone="",appt_type=0) :
        self.__client_name=client_name
        self.__client_phone=client_phone
        self.__appt_type=appt_type
        self.__day_of_week=day_of_week
        self.__start_time_hour=start_time_hour


    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):    
        return self.__client_phone 
    
    def get_appt_type(self):
        return self.__appt_type

    def get_appt_type_desc(self):
        types = ["Available", "Mens Cut", "Ladies Cut", "Mens Colouring", "Ladies Colouring"]
        return types[self.__appt_type]          
    
    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour

    def get_end_time_hour(self):
        self.end_time_hour=int(self.__start_time_hour)+1
        return self.end_time_hour
    
#set information from clients
    def set_day_of_week(self,update_day_of_week):
        self.day_of_week=update_day_of_week
    
    def set_start_time_hour(self,update_start_time_hour):
        self.start_time_hour=update_start_time_hour
    
    def set_client_name(self,update_client_name):
        self.client_name=update_client_name

    def set_client_phone(self,update_client_phone):
        self.client_phone=update_client_phone

    def set_appt_type(self,update_appt_type):
        self.appt_type=update_appt_type

    def schedule(self,update_client_name,update_client_phone,update_appt_type):
        self.client_name=update_client_name
        self.client_phone=update_client_phone
        self.appt_type=update_appt_type

    def cancel(self):
        self.__client_name=""
        self.__client_phone=""
        self.__appt_type=0

    def format_record(self):
        return f"{self.__client_name},{self.__client_phone},{self.__appt_type},{self.__day_of_week},{self.__start_time_hour}"   
    
    def __str__(self):
        return f"{self.__client_name:20}{self.__client_phone:15}{self.__day_of_week:10}{self.__start_time_hour:2}:00  -  {self.get_end_time_hour()}:00     {self.get_appt_type_desc():20}"
        


# Junction=Appointment("Saturday",9)
# Junction.schedule("Junction","234234",2)
# print(Junction.get_client_name())
# print(Junction.get_appt_type())
# print(Junction.get_appt_type_desc())
# print(Junction.get_day_of_week())
# print(Junction.get_start_time_hour())
# print(Junction.get_end_time_hour())
# print(Junction.format_record())
# print(Junction.__str__())

