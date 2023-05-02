'''For the purpose of this task, I have created a fairly simple code that partially resembles a system that could potentially be used by a small travel agency,
although limited by a series of unusual circumstances. All limitations were mainly imposed by the lack of time needed to collect all relevant information, as 
well as the complexity of such a code influenced by so many factors that need to be considered and can affect things like prices, availability of plane tickets and 
hotel stays, or even car rentals options. So much data needs to be collected, analyzed, and adapted to build a reliable system capable of updating itself, etc. 
In order to finalize this project, I had to do some online research. The first challenge was to find a reliable and always-at-hand source of data that a travel 
agency worker could rely on every time they needed it without browsing the internet or doing further research. I stumbled upon a list containing all UK airports 
while browsing the internet and I knew right away that it would represent the answer to at least my first problem. Using pandas, I tried to import the table from 
the web, but access was denied, so I had to figure out another way around it. Fortunately, the copy-paste method allowed me to collect a partially functional 
dataframe that I was able to purge using the pandas library. The uk_airports file is only a readable and printed file far from perfectly reusable, but it suits 
my needs and the task's purpose. Going down the rabbit hole from here onwards has never been easier. Jokes aside, to resolve most of my data collection problems 
I would create dictionaries which I'm afraid you will have to come across too, but please don't panic as they don't byte. Although I haven't used them extensively, 
they could be useful in other applications. For example, I could build a dictionary from each search a travel agency worker makes, and by adding every search to 
a new dictionary, it would be much easier to iterate between each dictionary to create a final result from which the client's preferences can be determined. 
However, this would only apply in extreme cases. I would then create the variables requested by the task and then the ones needed to support the functionalities of 
the system and lastly the functions which will be used in this case to only return the final results. Each block of code that follows will contain more relevant 
comments, which will help you understand the logic implemented while developing this relatively simple code.
I'm aware this code could be improved in many ways also there might be one or 2 bugs  left behind but by the end I was so overwhelmed with how much work I put into it 
and after a 1 on 1 session with a menthor I was told that I had done way too much so from now on I will instead try to limit my self to what the compulsory task is 
requesting. 
Note: the file all_uk_airports.txt and all_uk_airports.csv both need to be present in the dropbox directory along with  the "holiday.py" file or the program won't 
work as intended.
'''




from time import sleep
import random
import string
import pandas as pd

def typ_fx(line):
    for x in line:
        print(x, end="",flush=True )
        sleep(0.01)
    print()

choice_dt=None
choice_nt=None
plane_ticket=0

print(" ") 
typ_fx("Welcome!       Benvenuto!     Wilkommen!     Bienvenue!     Bienvenido!      Hoş geldin!     добре дошъл!     Mile widziany!") 

print(" ")

# First I have created a small dictionary which can be used as a reference and also to access each element individually to be reused

cities_fligths={
                1:{"Rome":"Fiumincino"},
                2:{"Kaiseri":"Erkilet"},
                3:{"Mladost":"Sofia"},
                4:{"Spata":"Athens"}
}
print(" ")

#The following block prints a line before the loop begins

line_cities="Please enter the client's destination airport! Choose one of the following options:\n"
for x in line_cities:
    print(x, end="",flush=True, )
    sleep(0.03)

#The variable city_list_n contains the list of available cities in form of numbers that correspond to the keys in the above dictionary. 
#The variable y_n_list contains the list of valid inputs to confirm or reject the destination airport.
#The loop starts with while true and a try statement and prints a message to prompt the user to enter their choice.
#The city_flight variable is set to the user's input as an integer (otherwise will need to be converted or cause an error). Each number is then assigned to the 4 keys in the dictionary
#If the input is in the list of available cities, the loop checks the value of city_flight to determine which destination airport to set and confirm.
#For each destination airport, the loop prints a message to confirm the selection and prompts the user to enter y for "Yes" or n for "No".
#Depending on the user's input, the loop either continues to the next iteration or breaks out of the loop.
#If the user enters an invalid input or the input is not in the list of available cities, the loop prints an error message and starts over.

city_list_n=[1,2,3,4]
y_n_list= ["y","n"]
while True:
    try:
        print(" ")
        print(f"{cities_fligths}")       
        print(" ")
        city_flight=int(input())
        if city_flight in city_list_n:
            if city_flight == 1:
                base_ticket_value1= 109
                dest=dest=cities_fligths[1]["Rome"]
                typ_fx(f"Please confirm: dest. airport {dest}! Enter y for 'Yes', n for 'NO':")

                try:
                    y_n=str(input())                    
                    
                    if y_n=="y": 
                        city_flight=1
                        print("OK")
                        break

                    elif y_n=="n":
                        typ_fx("Destination hasn't been confirmed! Starting over...")
                        continue   

                    elif y_n not in y_n_list:
                        typ_fx("Input error! y for 'YES', n for 'NO'!")
                        continue
                
                except (ValueError,NameError):
                    print(" Unrequested input! Starting over...")
                    continue
            
            elif city_flight == 2:
                base_ticket_value1= 117
                dest=cities_fligths[2]["Kaiseri"]
                typ_fx(f"Please confirm: dest. airport {dest}! Enter y for 'Yes', n for 'NO':")
                try:
                    y_n=str(input())
                    
                    if y_n=="y": 
                        city_flight=2
                        print("OK")
                        break

                    elif y_n=="n":
                        typ_fx("Destination hasn't been confirmed! Starting over...")
                        continue   

                    elif y_n not in y_n_list:
                        typ_fx("Input error! y for 'YES', n for 'NO'!")
                        continue

                except (ValueError,NameError):
                    print(" Unrequested input! Starting over...")
                    continue
            
            elif city_flight == 3:
                base_ticket_value1= 120
                dest=cities_fligths[3]["Mladost"]
                typ_fx(f"Please confirm: dest. airport {dest}! Enter y for 'Yes', n for 'NO':")

                try:
                    y_n=str(input())
                    
                    if y_n=="y":
                        city_flight=3
                        print("OK")
                        break

                    elif y_n=="n":
                        typ_fx("Destination hasn't been confirmed! Starting over...")
                        continue   

                    elif y_n not in y_n_list:
                        typ_fx("Input error! y for 'YES', n for 'NO'!")
                        continue
                
                except (ValueError,NameError):
                    print(" Unrequested input! Starting over...")
                    continue
            
            elif city_flight == 4:
                base_ticket_value1= 95
                dest=cities_fligths[4]["Spata"]
                typ_fx(f"Please confirm: dest. airport {dest}! Enter y for 'Yes', n for 'NO':")

                try:
                    y_n=str(input())
                    
                    if y_n=="y":   
                        city_flight=4
                        print("OK")
                        break 

                    elif y_n=="n":
                        typ_fx("Destination hasn't been confirmed! Starting over...")
                        continue   

                    elif y_n not in y_n_list:
                        typ_fx("Input error! y for 'YES', n for 'NO'!")
                        continue

                except (ValueError,NameError):
                    print(" Unrequested input! Starting over...")
                    continue
                
        else:
            typ_fx("Invalid input! Please try again: ")
            continue

    except ValueError:
        print(" Unrequested input! Starting over...")
        continue
    break

#I've tried to import the table directly from the website but the access was denied so I left it as a comment. Feel fry to try by removing the "#"
#url="https://airmundo.com/en/countries/united-kingdom/"
#pd.read_html(url)

#The code reads a CSV file and stores it in the variable uk_airports using pandas.  
#The dropna() method is used to remove any columns that contain all missing values.
#The column names are cleaned up using the str.strip() method, and the column names "Airport" and "CODE" are swapped using the rename() method.
#A new index is created for the uk_airports DataFrame using pd.RangeIndex().
#A message is printed asking the user to select the ID number corresponding to their departure airport, and then a while loop is entered to prompt the user for input.
#The user's input is validated to ensure it falls within the valid range of IDs (1-23).
#If the input is valid, a confirmation message is printed asking the user to confirm their selected airport.
#Another while loop is entered to prompt the user to confirm their selection, with the option to retry if they select "n".
#If the input is invalid, an error message is printed and the loop continues. Once a valid input is received, the loop is broken.

uk_airports=pd.read_csv("all_uk_airports.txt", sep="\t",index_col=0)
uk_airports= uk_airports.dropna(axis=1,how="all")
uk_airports.columns = uk_airports.columns.str.strip()
uk_airports = uk_airports = uk_airports.reset_index().rename(columns={"index": "Airport", "Airport": "CODE"})
uk_airports.index = pd.RangeIndex(start=1, stop=len(uk_airports)+1, step=1)
uk_airports.index.name = 'ID'
print(" ")
print(uk_airports)
print(" ")

line_air_dp="Using the table above as a reference please enter the correspondent ID number for the client's departure airport:\n"
for x in line_air_dp:
    print(x, end="",flush=True)
    sleep(0.03)
print(" ")

while True:
    try:
        air_dep = int(input())
        if air_dep in range(1,24):
            typ_fx(f"Please confirm: dep. airport is {uk_airports.loc[air_dep, 'Airport']}! Enter y for 'Yes', n for 'NO':")

            try:
                y_n2=input()
                
                if y_n2 == "y":
                    air_dep = air_dep
                    print("OK")
                
                elif y_n2=="n":
                    typ_fx("Please try a diff. ID!")
                    continue
                
                else:
                    print("Invalid input!")
            
            except (ValueError,NameError):
                print(" Unrequested input! Starting over...")
                continue
        else:
            typ_fx("Invalid input! Please try again:")
            continue
        print(" ")
    
    except ValueError:
        print(" Unrequested input! Starting over...")
        continue
    break

#A variable plane ticket is initialised so that can be recalled later, the variance variable apply a random correction of -\+ 5% to the base value of the ticket. 
variance1 = random.uniform(-0.05,0.05)
plane_ticket= base_ticket_value1 + (base_ticket_value1* variance1)   

#I have created a small dictionary that contains all daytime and nightime travels options available to the client so that it can be accessed by the user to make a choice or to access each item individually, stored in va variablem then reused 
flight_times = {
                "daytime": {1: "8:30am", 2: "12:00am", 3: "3:00pm", 4: "6:00pm"},
                "nighttime":{1: "8:30pm", 2: "10:30pm", 3: "3:00am", 4: "6:00am"},
}
list=(1,2,3,4)

#This few lines of code print a statement before the loop starts, they aren'r meant to be part of the loop
line_time="Should the flight be scheduled during daytime or nighttime?  Enter 1 for 'daytime' and 2 for 'nighttime':\n" 
line_time2="Note: It's recommended to inform the client about the possible price differences between daytime and nighttime travel.\n"
for x in line_time + line_time2:
    print(x, end="",flush=True, )
    sleep(0.03)


#The following code uses a while loop with a True condition to keep prompting the user for input until valid input is provided or an error occurs.
#The first try-except block is used to get the user's choice between daytime and nighttime flights.
#If the user enters 1, the code enters another try-except block to get the user's choice of preferred time from the daytime flights list. The code uses a for loop to print out the available options one character at a time and then prints the list of daytime flight times. If the user enters a valid choice (1, 2, 3, or 4), the code confirms the chosen departure time and exits the loop. If the user enters an invalid choice, the code prompts them to try again.
#If the user enters 2, the code enters another try-except block to get the user's choice of preferred time from the nighttime flights list. The code uses a for loop to print out the available options one character at a time and then prints the list of nighttime flight times. If the user enters a valid choice (1, 2, 3, or 4), the code confirms the chosen departure time and exits the loop. If the user enters an invalid choice, the code prompts them to try again.
#If the user enters anything other than 1 or 2, the code prompts them to try again.
#If the user enters invalid input (e.g., a non-integer), the code catches the error with the except block and prompts the user to try again.
while True:
    try:
        choice_dt_nt=int(input())
        if choice_dt_nt == 1:
            try:
                typ_fx("What's the client's preferred time schedule? Choose one from the following:\n")

                print(flight_times["daytime"])
                choice_dt = int(input())
                if choice_dt ==1 or choice_dt ==2 or choice_dt ==3 or choice_dt ==4:
                    time = flight_times['daytime'][int(choice_dt)]
                    typ_fx(f"Please confirm: dep.time is{time}! Enter y for 'Yes', n for 'NO':")
                    
                    while True:
                        try:
                            y_n3 = input()
                            if y_n3 == "y":
                                print("OK")
                                break
                            elif y_n3 == "n":
                                print("Please try again!")
                                break
                            else:
                                print("Invalid input! Enter y or n:")
                                continue
                        except (ValueError,NameError,KeyError):
                            print("Unrequested input! Starting over...")
                            continue
                    break
                else:
                    typ_fx("Invalid input! Enter 1, 2, 3, or 4:")
                    continue
            except (ValueError,NameError,KeyError):
                print("Unrequested input! Starting over...")
                continue

        elif choice_dt_nt == 2:
            try:
                typ_fx("What's the client's preferred time schedule? Choose one from the following:\n")                 
                print(flight_times["nighttime"])
                choice_nt = int(input())
                if choice_nt == 1 or choice_nt == 2 or choice_nt == 3 or choice_nt == 4:
                    time = flight_times['nighttime'][int(choice_nt)]
                    typ_fx(f"Please confirm: dep.time is{time}! Enter y for 'Yes', n for 'NO':")
                    while True:
                        try:
                            y_n3 = input()
                            if y_n3 == "y":
                                print("OK")
                                break
                            elif y_n3 == "n":
                                print("Please try again!")
                                break
                            else:
                                print("Invalid input! Enter y or n:")
                                continue
                        except (ValueError,NameError):
                            print("Unrequested input! Starting over...")
                            continue
                    break
                else:
                    typ_fx("Invalid input! Enter 1, 2, 3, or 4:")
                    continue
            
            except (ValueError,NameError,KeyError):
                print("Unrequested input! Starting over...")
                continue

        else:
            typ_fx("Invalid input! Please try again:")
            continue

    except (ValueError,NameError,KeyError):
        print("Unrequested input! Starting over...")
        continue


if choice_dt:
    time = flight_times['daytime'][int(choice_dt)]
elif choice_nt:
    time = flight_times['nighttime'][int(choice_nt)]
variance2 = random.uniform(-0.05,0.05)
plane_ticket= plane_ticket + (plane_ticket* variance2)

typ_fx("What's the client's class preference? Type in 1 for '1st class' and 2 for 'economy':")
print(" ")

while True:
    try:
        class_choice=int(input())
        if class_choice== 1 or class_choice==2:
            print("OK!")
            break
        else:
            print("Wrong Input! Please try again:Enter  1 or 2!")
            continue
    
    except (ValueError,NameError,KeyError):
        print("Unrequested input! Starting over...")
        continue
    

typ_fx("Client's plane booking is now completed! Will be printed at the end along with the other bookings! Carrying on...\n")

#This block of code is responsible for getting input from the user regarding whether they want to rent a car or not and if they do, for how many days, and which range of car they prefer.
#The code uses nested try-except blocks and while loops to handle errors and keep prompting the user until valid input is entered.

typ_fx("Is the client going to rent a car? Enter y for 'Yes', n for 'No'! ")

while True:   
    try:
        answer=input()            
        if answer=="y":
            try:
                typ_fx("for how many days?")

                try:
                    rental_days=int(input())
                    if rental_days<=14:
                        typ_fx(f"Please confirm the number of days is {rental_days}! Enter y for 'Yes', n for 'NO':")

                        try:
                            y_n4 = input()
                            
                            if y_n4 == "y":
                                print("OK")
                                typ_fx(" Please choose between the following ranges:\n")
                                typ_fx("1 - economy\n")
                                typ_fx("2 - mid range\n")
                                typ_fx("3 - luxury\n")

                                try:
                                    range_choice=int(input())              
                                    
                                    if range_choice==1:
                                        price1_carxday= 50
                                        car="WolkswagenPolo 1.0 petrol"
                                        break
                                    
                                    elif range_choice==2:
                                        price2_carxday= 72
                                        car="Ford Focus 1.6 diesel"
                                        break
                                    
                                    elif range_choice==3:
                                        price3_carxday= 99
                                        car="JaguarF-Type1.0"            
                                        break
                                    
                                    else:
                                        typ_fx("Wrong Input! Enter 1,2 or 3!")
                                        continue
                                
                                except (ValueError,NameError):
                                    print("Unrequested input! Starting over...")
                                    continue
                                                                               
                            elif y_n4 == "n":
                                print("Please try again!")
                                continue
                            else:
                                print("Invalid input! Enter y or n:")
                                continue
                            
                        except (ValueError,NameError):
                            print("Unrequested input! Starting over...")
                            continue
                        
                    
                    else:
                        typ_fx("Input error: Must between 1 and 14! Try again!")
                        continue
            
                except (ValueError,NameError):
                    print("Unrequested input! Starting over...")
                    continue                
            except (ValueError,NameError):
                print("Unrequested input! Starting over...")
                continue          
        
        elif answer=="n":
            rental_days=0
            break

        elif answer!="y" or answer!="n":
            typ_fx("Input Error! please Try again!")
            continue
        
    except (ValueError,NameError):
        print("Unrequested input! 'y' or 'n'?")
        continue       

Insurance1xday=20 
Insurance2xday=25
Insurance3xday=30
deposit=200


#creates a dataframe using pandas that can be re-used to access each item
hotel_choices = [
                ["***Yes Hotel","***Club Viva","***Sunny Beach","***Hotel Achilleas"],
                ["****The Glam Hotel","****Green Nature Resort & Spa","****Wave Resort","****Brown Acropol"]
]
hotel_choice = pd.DataFrame(hotel_choices, index=["3-Star Hotel", "4-Star Hotel"], columns=["Rome", "Marmaris", "Burgas", "Athens"])

print(hotel_choice)
print(" ")


#This loop asks the user to input their preferred hotel rating (either 3 or 4 stars).
#It then asks the user to confirm their choice and provides an option to change it.
#If the input is invalid, the loop continues and asks the user to enter a valid input.
#If the input is valid and confirmed, the loop breaks and proceeds to the next step of the program.
while True:
    line_hotel="What is the client's preferred hotel rating: Enter a number below: Enter 3 for ***stars or 4 for ****stars!\n"
    for x in line_hotel:
        print(x, end="",flush=True)
        sleep(0.03)
    try:
        hotel_rating = int(input())

        if hotel_rating==3 or hotel_rating==4:
            typ_fx(f"Please confirm below that the client's rating choice is {hotel_rating} stars! y for 'Yes', n for 'No'!\n")   

            try:
                y_n5 = input()
                if y_n5 == "y":
                    print("OK")
                    break
                elif y_n3 == "n":
                    print("Please try again!")
                    break
                else:
                    print("Invalid input! Enter y or n:")
                    continue

            except (ValueError,NameError):
                print("Unrequested input! Starting over...")
                continue
        else:
            typ_fx("Input Error. Please enter 3 or 4!")
            continue
    
    except ValueError and NameError:
        print("Unrequested input! 'y' or 'n'?")
        continue

#This loop prompts the user to enter the number of nights the client will stay at the resort, and validates the input.
#If the input is not valid, it prompts the user to try again.
#If the input is valid, it prompts the user to confirm the length of stay and validates the input.
#If the input is not valid, it prompts the user to try again.
#If the input is valid, it breaks out of the loop.

while True:   
    typ_fx("Please enter the number of nights the client will stay at the resort! Choose  3,4,7 or 14:\n")

    try:        
        num_nights=int(input())        
        if num_nights== 3 or num_nights== 4 or num_nights== 7 or num_nights== 14: 
            typ_fx(f"Please confirm that the lenght of stay is {num_nights} nights! y for 'Yes', n for 'No'!\n")   
            try:
                y_n5 = input()
                if y_n5 == "y":
                    print("OK")
                    break
                elif y_n5 == "n":
                    print("Please try again!")
                    break
                else:
                    print("Invalid input! Enter y or n:")
                    continue
            except (ValueError,NameError):
                print("Unrequested input! Starting over...")
                continue  

        else:
            typ_fx("You have entered an invalid input. Please enter 3,4,7 or 14")
            continue
    
    except (ValueError,NameError):
            print("Unrequested input! 'y' or 'n'?")
            continue


#Create a function that returns the resort choice based on destination and hotel_rating, no arguments are needed
def resort():
    if city_flight ==1 and hotel_rating==3:
        resort=hotel_choice.iloc[0,0] 
    elif city_flight ==1 and hotel_rating==4:
        resort=hotel_choice.iloc[1,0]
    if city_flight ==2 and hotel_rating==3:
        resort=hotel_choice.iloc[0,1]
    elif city_flight ==2 and hotel_rating==4:
        resort=hotel_choice.iloc[1,1]
    if city_flight ==3 and hotel_rating==3:
        resort=hotel_choice.iloc[0,2]
    elif city_flight ==3 and hotel_rating==4:
        resort=hotel_choice.iloc[1,2]
    if city_flight ==4 and hotel_rating==3:
        resort=hotel_choice.iloc[0,3]
    elif city_flight ==4 and hotel_rating==4:
        resort=hotel_choice.iloc[1,3]
    return resort

#Create a function that returns the total price of the stay based on the lenght of stay and hotel rating
def hotel_cost(num_nights):
    if city_flight ==1 and hotel_rating==3:
        price=157 * num_nights
    elif city_flight ==1 and hotel_rating==4:
        price=168 * num_nights
    if city_flight ==2 and hotel_rating==3:
        price=149 * num_nights
    elif city_flight ==2 and hotel_rating==4:
        price=160 * num_nights
    if city_flight ==3 and hotel_rating==3:
        price=140 * num_nights
    elif city_flight ==3 and hotel_rating==4:
        price=173 * num_nights
    if city_flight ==4 and hotel_rating==3:
        price=125 * num_nights
    elif city_flight ==4 and hotel_rating==4:
        price=147 * num_nights
    return price

#Create a function that returns the total price of the ticket based on destinationand and class choice
def plane_cost(city_flight):
    if city_flight ==1 and class_choice==1:
        final_cost= plane_ticket * 1.2
    elif city_flight ==1 and class_choice==2:
        final_cost= plane_ticket
    if city_flight ==2 and class_choice==1:
        final_cost= plane_ticket * 1.2 
    elif city_flight ==2 and class_choice==2:
        final_cost= plane_ticket 
    if city_flight ==3 and class_choice==1:
        final_cost= plane_ticket * 1.2 
    elif city_flight ==3 and class_choice==2:
        final_cost= plane_ticket
    if city_flight ==4 and class_choice==1:
        final_cost= plane_ticket * 1.2
    elif city_flight ==4 and class_choice==2:
        final_cost= plane_ticket
    return final_cost   

#Create a function that returns the total price of the car rental based lenght of days of rental, range choice etc. 
def  car_rental(rental_days):
    total_car_rent=0
    if rental_days and range_choice==1:
        total_car_rent = (rental_days*(price1_carxday+Insurance1xday)) + deposit
    elif rental_days and range_choice==2:
        total_car_rent = (rental_days*(price2_carxday+Insurance2xday)) + deposit
    elif rental_days and range_choice==3:
        total_car_rent = (rental_days*(price3_carxday+Insurance3xday)) + deposit
    elif rental_days==0:
        total_car_rent = None
    return total_car_rent

#The following code creates a random code that will be used when printing the plane ticket.This is done for the sole purpose to simulate a real life situation 
valid = string.ascii_letters + " " + "1234567890"
code = ''.join(random.sample(valid, 4))

# The following lines were made to recal the time variable
if choice_dt:
    time = flight_times['daytime'][int(choice_dt)]
elif choice_nt:
    time = flight_times['nighttime'][int(choice_nt)]

#Defines the function that returns the total value of all functions together
def holiday_cost(hotel_cost,plane_cost, car_rental):
    total_holiday_cost= hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_holiday_cost

#Print all results   
typ_fx(f'''Your client's booking has now been finalised: Departure will be from {(uk_airports.loc[int(air_dep), 'Airport'])}, code flight{code} at: {time} with destination airport:{dest}. Total plane cost travel pp: {plane_cost(city_flight)}£\n''')
typ_fx(f'''The client will be staying at the {resort()} for a total of {num_nights} nights. The total cost of the hotel pp is: {hotel_cost(num_nights)}£\n''')
if answer == "y":
    typ_fx(f'''The client is also renting a {car} for a total number of {rental_days} days. The total amount is {car_rental(rental_days)}£\n''') 
else:
    typ_fx(f'''The client is not renting a car\n''')
typ_fx(f"The total value of the holiday selected by the client is {holiday_cost(hotel_cost,plane_cost, car_rental)}£pp\n ")


#Program ends, print a message 
typ_fx("To do another search.... Please Restart the program! Goodbye! ")



#Sources
#https://airmundo.com/en/countries/united-kingdom/
#https://www.udemy.com/course/the-pandas-bootcamp/learn/lecture/, The Complete Pandas Bootcamp 2022: Data Science with Python

