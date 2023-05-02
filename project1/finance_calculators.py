#This code allows the user to choose between two financial calculators: investment and home loan.
#First the libraries and modules that are needed are imported
#The program uses the time.sleep() method to delay the printing of the messages for a better user experience.
#First, a menu is printed to welcome the user and explain the available options.
#Then all messages are printed using a for loop method that print each letter for each message in sequence, The Flush method allows to write each character in sequence in the same line 
#A while loop is then introduced to break or restart a certain process when the wrong input is entered
#If the user chooses investment, the program will calculate the potential return/s of their investment/s based on factors such as the initial investment amount, the expected rate of return, and the length of the investment period.
#The program will then prompt the user to enter the investment amount, interest rate, duration, and type of interest (simple or compound).
#Then, the user is prompted to choose between the two calculators by entering 1 or 2.
#If an invalid input is entered, the program will continue to prompt the user until a valid input is entered.
#The program will then calculate and print the total amount earned based on the user's inputs.
#If the user chooses home loan instead, the program will calculate the amount of the monthly repayments of the mortgage based on the loaned amount, the interest rate, and the duration of the mortgage.
#the program will then prompt the user to enter the loaned amount, interest rate, and duration of the mortgage.
#Finally the program will  calculate and print the amount of the monthly payments based on the user's inputs.

import math as mt
from time import sleep
import sys

def typ_fx(line):
    for x in line:
        print(x, end="", flush=True)
        sleep(0.01)
    print()

print("\n")
typ_fx("Dear customer please choose one of the following options: ")
typ_fx("investment - to calculate the amount of interest you'll earn on top of your initial investment. ")
typ_fx("home loan - to calculate the amount of the monthly repayment based on the interests accumulated on the price borrowed.  ")
typ_fx("Please enter 1 for investment and 2 for home loan: ")
print("\n")
while True:
    choice = int(input())
    if choice != 1 and choice != 2:
        typ_fx("Invalid choice. Please enter 1 for investment and 2 for home loan.")
        continue
    print("\n")
    if choice==1:
        typ_fx("You chose Investment: ")
        typ_fx('''This is a calculator that will help you calculate the potential return/s of your investment/s based on factors such as the initial investment amount, the expected rate of return, and the length of the investment period. ''')
        typ_fx('''Please enter below the amount you would like to entrust followed by the yearly interest, then the time that you intend it to last, finally you can choose between the following type of interests: simple(constant) and compound(accumulated). ''')
        print("\n")
        typ_fx("amount in £: ")
        amount1= int(input())

        typ_fx("rate in %: ")
        interest1= float(input())

        typ_fx("duration in yrs: ")
        duration1= int(input())

        typ_fx("what type? Enter 1 for simple or 2 for compound: ")
        while True:
            type= int(input())
            print("\n")
            if type== 1:
                simple_total= round(amount1*(1+(interest1/100)*duration1),2)
                typ_fx(f'''You chose simple interest: the total amount earned based on an investiment of {amount1}£ with an interest rate of {interest1}% for a period of {duration1}yrs is {simple_total} ''')
                print("\n")
                sys.exit(0) 
            elif type== 2:
                compound_total= round(amount1*mt.pow((1+(interest1/100)),duration1),2) 
                typ_fx(f'''You chose compound interest: the total amount earned based on an investiment of {amount1}£ with an interest rate of {interest1}% for a period of {duration1}yrs is {compound_total} ''')
                print("\n")
                sys.exit(0)
            else:
                typ_fx("Invalid choice. Please enter 1 for simple and 2 for compound to continue...")
                continue
    
    elif choice==2:
        typ_fx("You chose home loan: ")
        typ_fx('''This is a calculator that will help you calculate the amount of the monthly payments of a mortgage based on the loaned amount, the interest rate on the amount you borrowed, and the loan term. ''')
        typ_fx('''Please enter below the value of the home you are interested in followed by the yearly interest rate and finally the duration of the plan: ''')
        print("\n")
        typ_fx("amount in £: ")
        amount2= int(input())
        typ_fx("rate in %: ")
        interest2= float(input())
        typ_fx("duration in months: ")
        duration2= int(input())
        print("\n")
        repayment= round(((interest2/100)/12)*amount2/((1-(1+((interest2/100)/12))**(-duration2))), 2)
        typ_fx(f'''The amount of loan that will have to be repaid based on an initial investiment of {amount2}£ with an annual interest rate of {interest2}% for a period of {duration2}months is {repayment} ''')
        print("\n") 
        break

# Sources:
# https://www.bbc.co.uk/bitesize/topics/zn63bqt/articles/z2jfp4j
# Google search for information on using the sys module and how to use while True loop in Python  
    


