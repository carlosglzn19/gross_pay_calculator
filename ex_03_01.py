'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.

'''

#Input Hours
hrs_input = input("Enter hours: ")
hours = float(hrs_input)

#Input Rate
rate_input = input("Enter rate: ")
rate = float(rate_input)

#Gross pay variable
gross_pay = 0

#If statement to calculate groos pay depending on the hours worked
if hours <= 40:
    gross_pay = hours * rate
elif hours > 40:
    gross_pay = rate * 40 + (rate * 1.5 * (hours - 40))

#Printing the gross pay    
print(gross_pay)
    