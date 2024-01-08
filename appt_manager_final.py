import appointment as ap
from os.path import exists


new_appt = ap.Appointment("",0)   #use class Appointment
appt_list=[]
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]


#create each day and time slot in this day
def create_weekly_calendar(new_day_of_week):
    if new_day_of_week.capitalize() in week:            #if input day is in week list, run this function
        existing_appt=None   
        for appt in appt_list:                                 #appt_list already have same appt as new_day_of_week, use appt
            if appt.get_day_of_week()==new_day_of_week:
                existing_appt=appt
        if existing_appt==None:                          
            for time in range(9, 18):
                appt_list.append(ap.Appointment(new_day_of_week, time))            # if not, appt_list append this new_day_of_week



    

def find_appointment_by_time(new_appt):                         #this is find_appointment_by_time(), use this code to find the match time slot when load files
    for appt in appt_list:                                       #check appt in appt_list, if time and day match, load the information and assign them in different positions of schedule function called by Appointment Class.
        if new_appt.get_day_of_week().capitalize() ==appt.get_day_of_week().capitalize():
            if new_appt.get_start_time_hour() == appt.get_start_time_hour():
                # if the start times match, replace old entry with new_appt.
                    appt.schedule(new_appt.get_client_name(),new_appt.get_client_phone(),new_appt.get_appt_type())

                

                    

#  load information from csv file
def load_scheduled_appointments():
    print("Starting the Appointment Manager System")
    print("Weekly calendar created")
    load_option = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").lower()
    if load_option == "y":
        while True: 
            load_file_name = input("Enter appointment filename: ")
            if exists(f"{load_file_name}.csv"):
                with open(f'{load_file_name}.csv', 'r') as my_file:
                    lines = my_file.readlines()
                    line_account=0
                    for line in lines:
                        values = line.strip().split(",")  # Split the line by comma to get individual values
                        load_appt = ap.Appointment(values[3], int(values[4]), values[0], values[1], int(values[2]))
                        create_weekly_calendar(values[3])    
                        find_appointment_by_time(load_appt) 
                        # print(load_appt)      #test
                        line_account+=1
                            
                             
                # print(appt_list)     #test
                # for appt in appt_list:
                #     print(appt)
                print(f"{len(lines)} previously scheduled appointments have been loaded")
                break
            else:
                print("File not found.")


#get user input and locate them into class  #part of option 1
def create_appt():
    found=True
    new_day_of_week=input("What Day: ").capitalize()
    create_weekly_calendar(new_day_of_week)                                              #use input day create a calendar put into appt_list
    new_start_time_hour=int(input("Enter start hour (24 hour clock): "))
    for appt in appt_list:
      if new_day_of_week.capitalize() ==appt.get_day_of_week().capitalize():
          if new_start_time_hour== appt.get_start_time_hour():      
                if appt.get_appt_type()==0:                                               #if time slot is avaible, keep asking
                    found=False
                    new_client_name=input("Client Name: ")                                #assign input into class
                    new_appt.client_name=new_client_name
                    new_client_phone=input("Client Phone: ")
                    new_appt.client_phone=new_client_phone 
                    print("Appointment types")
                    print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
                    new_appt_type=int(input("Type of Appointment: "))
                    if new_appt_type in [1,2,3,4]:
                        new_appt.appt_type=new_appt_type
                        appt.schedule(new_appt.get_client_name(),new_appt.get_client_phone(),new_appt.get_appt_type())
                        new_appt.get_appt_type_desc()      
                        print(f"OK, {new_appt.client_name}'s appointment is scheduled!")
                    else:
                        print("Sorry that is not a valid appointment type!")    
                else:
                    print("Sorry that time slot is booked already!")
                    found = False   
                  
    else:
       if found==True:    
            print("Sorry that time slot is not in the weekly calendar!")    
              


#system menu to choose
def print_menu():
    print(''' 
Jojo's Hair Salon Appointment Manager
=====================================
 1) Schedule an appointment
 2) Find appointment by name
 3) Print calendar for a specific day
 4) Cancel an appointment
 9) Exit the system
''')
    user_menu_input=int(input("Enter your selection: "))
    while user_menu_input not in [1,2,3,4,9]:
        print("Sorry that is not a valid appointment type!")
        user_menu_input=int(input("Enter your selection: /n"))
    return user_menu_input    
      


    

#option 2 show appointment by name
def show_appointments_by_name():
    print("** Find appointment by name **")
    new_client_abbr=input("Enter Client Name: ").capitalize()
    print(f"Appointments for {new_client_abbr}")
    print(f"{'Client Name':20}{'Phone':15}{'Day':10}{'Start':10}{'End':10}{'Type':20}")
    print("--------------------------------------------------------------------------------------------")

    found = False
    for appt in appt_list:
        if new_client_abbr == appt.get_client_name():  
            print(appt.__str__())
            found = True
        elif new_client_abbr in appt.get_client_name():
            print(appt.__str__())
            found= True    
    if not found:
        print(f"No appointments found for {new_client_abbr}")




#option 3 show appointments by day
def show_appointments_by_day(new_day_of_week):
    create_weekly_calendar(new_day_of_week)
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    print("--------------------------------------------------------------------------------------------")
    for appt in appt_list:
        if appt.get_day_of_week().lower() == new_day_of_week.lower():  # renew the specified day from input
            print(appt)


#option 4 cancel appointment
def cancel(new_day_of_week,new_start_time_hour):
    search=True 
    for appt in appt_list:   
        if new_day_of_week==appt.get_day_of_week():
            if new_start_time_hour == appt.get_start_time_hour():
                search=False
                if appt.get_appt_type()!=0:
                # if the start times match, replace old entry with new_appt.if not avaible, replace as avaible
                    print(f"Appoinment:{new_day_of_week.capitalize()} { new_start_time_hour}:00- {new_start_time_hour+1}:00 for {appt.get_client_name()} has been cancelled!")
                    appt.schedule("","",0)
                else:
                    print("That time slot isn't booked and doesn't need to be cancelled ")    
    else:         
        if search==True:
            print("Sorry that time slot is not in the weekly calendar! ")


#option 9 to exit and save content in the csv file.
def save_scheduled_appointments():
    print("**Exit the system**")
    save_option=input("Would you like to save all scheduled appointments to a file (Y/N)? ").lower()
    if save_option=="y":
       while True:
        save_file_name=input("Enter appointment filename: ")
        if exists(f"{save_file_name}.csv"):
            save_overwrite=input("File already exists. Do you want to overwrite it (Y/N)?").lower()
            if save_overwrite=="y":
                my_file= open('appointments1.csv', 'w')
                count=0
                for appt in appt_list:
                    if appt.get_appt_type()!=0:
                        my_file.write(f"{appt.format_record()}\n")
                        count +=1
                my_file.close()
                print(f"{count} scheduled appointments have been successfully saved")
                print("Good Bye!")
                break
        elif save_file_name!="appointments1" or save_overwrite=="n":
                my_file= open(f'{save_file_name}.csv', 'w')
                count=0
                for appt in appt_list:
                    if appt.get_appt_type()!=0:
                        my_file.write(f"{appt.format_record()}\n")
                        count +=1
                my_file.close()
                print(f"{count} scheduled appointments have been successfully saved")
                print("Good Bye!")
                break
                
                 


def main():

    load_scheduled_appointments()
    while True:
        selected_option = print_menu()
        if selected_option==1:              #make a schedule option 1     
            print("** Schedule an appointment **")
            create_appt()
            # print(appt_list)      #test if input already in appt_list
        elif selected_option==2:
            show_appointments_by_name()
        elif selected_option==3:
            print("** Print calendar for a specific day **")
            new_day_of_week=input("Enter day of week:").capitalize()
            print(f"Appointments for {new_day_of_week.capitalize()}")
            show_appointments_by_day(new_day_of_week)
        elif selected_option==4:
            print("** Cancel an appointment **")
            new_day_of_week=input("What Day: ").capitalize()
            new_start_time_hour=int(input("Enter start hour (24 hour clock): "))
            cancel(new_day_of_week,new_start_time_hour)          
        elif selected_option==9:
            save_scheduled_appointments()
            break



if __name__ == "__main__":
    main()        