''' 
******************************************************************************
*                   Assignment: Compound-Interest                              *
*                   Lecturer: Dr.Richard Lai                                   *
*                   Student : Pun VireakRoth                                   *
*                   Student ID:18215                                           *
*                                                                              *
******************************************************************************
'''

from tracemalloc import start
#class colors
class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m' 
# Start 
start_over = 'true'
while start_over == 'true':
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
    A = float(input("How much money you have to save into account each month? "))
    N = int(input("How many month you want to put your money? "))
    W = float(input("How much interest you earn annually? "))
    print("\n\n")
    w = W / 1200 # interest for each month

    # initial value function 
    def cal_compound_interest(A,N,w):
        F = A*(1+w)**N
        compound_interest = F - A
        return compound_interest
    # function that handle with add and remove item to the list 
    def add_remove_list(list_value, value):
        for j in range(1):
            assign = list_value.append(value)
        list_value.append(assign)
        list_value.pop()
        
    
    total_value_to_date = 0

    list_month = []
    list_deposit = []
    list_total_deposit = []
    list_this_month_interest = []
    list_total_interest_earned = []
    list_total_value_to_date = []

    for time in range(1,N+1):
        month = time 
        total_deposit = A * time
        this_month_interest = cal_compound_interest(A,time,w)
        total_value_to_date += A*(1+w)**time
        total_interest_earned = total_value_to_date - total_deposit

        # --------------------------append value to the list -----------------------------------
        #Month
        add_remove_list(list_month,month)
        #Deposit
        add_remove_list(list_deposit,A)
        #Total Deposit
        add_remove_list(list_total_deposit,total_deposit)
        #This month interest 
        add_remove_list(list_this_month_interest,this_month_interest)
        #Total interest Earned 
        add_remove_list(list_total_interest_earned,total_interest_earned)
        #Total value to date
        add_remove_list(list_total_value_to_date,total_value_to_date)
   
    #---------------------------Print table--------------------------------------------
    
    from beautifultable import BeautifulTable
    table = BeautifulTable()
    table.columns.append(list_month, header=color.BOLD + color.BLUE + "Month")
    table.columns.append(list_deposit, header=color.BOLD + color.BLUE +"Deposit")
    table.columns.append(list_total_deposit, header=color.BOLD + color.BLUE +"Total-Deposit")
    table.columns.append(list_this_month_interest, header=color.BOLD + color.BLUE +"This-Month-interest")
    table.columns.append(list_total_interest_earned, header=color.BOLD + color.BLUE+"Total-Interest-Earned")
    table.columns.append(list_total_value_to_date, header=color.BOLD + color.BLUE +"Total-Value-to-Date")
    table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
    print(table)

    redo_program = input(color.RED+"\n\nDo you want to calculate your Compound interest again? (Y/N) : ").upper()
    if (redo_program == 'Y'):
        start_over = 'true'
    else:
        start_over = 'false'


