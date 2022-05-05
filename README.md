# Compound-Interest
a) to read in the amount of deposit, interest rate, and duration of the deposit in months; and

b) to print a table
A = given sum of money each month
N = months
W = interest at the rate percent annually
F = amount of money that will have accumulated after N months

F = A[(1+W/1200) + (1+W/1200)**2 + (1+W/1200)**3 + … + (1+W/1200)**N)]

![image](https://user-images.githubusercontent.com/63106297/166883835-9ef97bab-63fb-4419-ab2a-d5357133f918.png)

c) to ask the user if he wants to repeat (a) and (b) for new inputs after printing the table.

# pseudocode
Define colors class 
Start program
initialize start_over to string 'true'

while start_over is equal to string 'true' do the following statement until start_over is not equal to the string 'true'
print welcome message
ask the user for ( deposit, month length, interest ) input and assign them to variables

if a deposit is a negative number
  print error message and break out from the program
if month bigger than 36 or month is a negative number
  print error message and break out from the program
if interest rate bigger than 12 or interest rate is a negative number
  print the error message and break out from the program
  
print 2 new lines to make output look nicer
initial a lowercase w that take our interest and divided by 1200
define a function that calculates this month's interest
define a function that can automate the add and remove items in a list
initial a totalvaluetodate variable to 0 in order to add its value every time the loop run
initial all the lists we need starting from month to total value to date

FOR time in range 1 to the month that the user has input
  Set the month variable to the month loop variable which iterates each time the loop run.
  Call a function that we have defined to calculate the interest each month and set its value to this month's interest variable
  Take a totalvaluetodate variable that we have to declare earlier and add its old value to a new one each time the loop run
  Take the total value to date variable and subtract it from the total deposit
  Call function that we have defined in order to add and remove items to list so we call it to run with our value staring from month to total value to date
  
import a library that can easily draw a table
initial a table variable to BeaitifilTable( ) function
Add all the columns starting from month to total value to date and add BLUE color to the first list item
Manipulate table style by calling set_sytle function
Print out the table
initial redo program variable and take the Y and N input from the user then use upper case function to convert those two alphabets

if the redo program variable equal to Y
  set start_over variable to true which means the program still keeps on running
Else
  break out from the program

  




