''' 
******************************************************************************
*                   Assignment: Compound-Interest                              *
*                   Lecturer: Dr.Richard Lai                                   *
*                   Student : Pun VireakRoth                                   *
*                   Student ID:18215                                           *
*                                                                              *
******************************************************************************
'''

print('''

                    ░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░
                    ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗
                    ██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║
                    ██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░██║██║░░░██║██║╚████║██║░░██║
                    ╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
                    ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░

                    ██╗███╗░░██╗████████╗███████╗██████╗░███████╗░██████╗████████╗
                    ██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝
                    ██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████╗░░╚█████╗░░░░██║░░░
                    ██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░
                    ██║██║░╚███║░░░██║░░░███████╗██║░░██║███████╗██████╔╝░░░██║░░░
                    ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░
''')

#Get user input 
A = float(input("                    How much money you have to save into account each month? "))
N = int(input("                    How many month you want to put your money? "))
W = float(input("                    How much interest you earn annually? "))
print("\n\n")
w = W / 1200 # interest for each month

# Color 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# print(f"{bcolors.OKGREEN}============================================================================================================={bcolors.ENDC}")


# print(f"{bcolors.OKBLUE}Month{bcolors.ENDC}\t {bcolors.WARNING}Deposit{bcolors.ENDC}\t {bcolors.OKGREEN}Total Deposits{bcolors.ENDC}\t {bcolors.OKCYAN}This Month's Interest{bcolors.ENDC}\t {bcolors.HEADER}Total-Interest Earned{bcolors.ENDC}\t {bcolors.FAIL}Total-Value To Date{bcolors.ENDC}")
# print(f"{bcolors.OKGREEN}============================================================================================================={bcolors.ENDC}")
#=================Calculate month=========================================== 

def cal_month():
    month_list = []
    for time in range(1,N+1):
        month = month_list.append(time)
    month_list.append(month)
    month_list.pop()
    return month_list
# print(cal_month())

#---------Print Deposit ------------------------------------------
def cal_deposit():
    deposit_list = []
    for time in range(1,N+1):
        deposit = deposit_list.append(format(A,".2f"))
    deposit_list.append(deposit)
    deposit_list.pop()
    return deposit_list
# print(cal_deposit())
#---------Total Deposit ------------------------------------------
def cal_total_deposit():
    total_deposit_list = []
    for time in range(1,N+1):
        total_deposit = total_deposit_list.append(format(A*time,".2f"))
    total_deposit_list.append(total_deposit)
    total_deposit_list.pop()
    return total_deposit_list
# print(cal_total_deposit())
#-------- Calculate This Month's interest ------------------------

def cal_month_interest():
    counter = 0 
    first_monthly_interest = [] 
    first_monthly_interest.append(A/100)
    for time in range(1,N+1):
        M = (1+w)**time
        counter += M
        total_val_to_date = A* counter
        this_month_interest = format((total_val_to_date + 100)/100,".2f")
        first_monthly_interest.append(this_month_interest)
    first_monthly_interest.append(first_monthly_interest)
    first_monthly_interest.pop()
    first_monthly_interest.pop()
    return first_monthly_interest
# print(cal_month_interest())
#-----------------------calculate total interest earned ------------------------
def cal_total_interest_earned():
    counter = 0 
    total_interest_earned_list = []
    for time in range(1,N+1):
        M = (1+w)**time
        counter += M
        total_val_to_date = A* counter
        total_interest_earned = total_interest_earned_list.append(format(total_val_to_date - (A*time),".2f"))
    total_interest_earned_list.append(total_interest_earned)
    total_interest_earned_list.pop()
    return total_interest_earned_list
    
# print(cal_total_interest_earned())
#--------------------Calculate Total value to date -----------------------
def cal_total_value_to_date():
    counter = 0
    total_value_to_date_list = []
    for time in range(1,N+1):
        M = (1+w)**time
        counter += M
        total_val_to_date =total_value_to_date_list.append(format(A * counter,".2f"))
    total_value_to_date_list.append(total_val_to_date)
    total_value_to_date_list.pop()
    return total_value_to_date_list
# print(cal_total_value_to_date())
#-----------------------------Display Result as a table------------------------------------------

import pandas as pd
import numpy as np

#Insert label
labels = []
bold_labels = []
for j in range(1,N+1):
    new_labels = labels.append("█")
    new_bold_labels = bold_labels.append("░")
labels.append(new_labels)
labels.pop()
bold_labels.append(new_bold_labels)
bold_labels.pop()

exam_data  = {
        'Month': cal_month(),
        'Deposit':cal_deposit(),
        'Total Deposits':cal_total_deposit(),
        'This Month Interest':cal_month_interest(),
        'Total-Interest Earned': cal_total_interest_earned(),
        'Total-Value To Date': cal_total_value_to_date(),
        '█': labels,
        '░': bold_labels
        }


df = pd.DataFrame(exam_data,index=labels)
print(f"███████████████████████████████████████████████████████████████████████████████████████████████████████████████")
print(df[['Month','█', 'Deposit','░', 'Total Deposits','█', 'This Month Interest','░', 'Total-Interest Earned','░', 'Total-Value To Date','█']])
print(f"███████████████████████████████████████████████████████████████████████████████████████████████████████████████")

