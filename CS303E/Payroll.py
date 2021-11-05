# File: Payroll.py
# Student: Maxwell T Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 2/4/20
# Date Last Modified: 2/8/20
# Description of Program: Takes in user input for weekly hours and hourly pay and calculates net pay including 
# state and federal tax rate/withholding and gross pay. This information is then formatted and outputted.
#

#User Input
employeeName = input("Enter employee's name: ")
employeeWeeklyHrs = float(input("Enter number of hours worked in a week: "))
employeeHrlyRate = float(input("Enter hourly pay rate: "))
federalTaxRate = float(input("Enter federal tax withholding rate: "))
stateTaxRate = float(input("Enter state tax withholding rate: "))
print("")

#Maths
employeeGrossPay = employeeWeeklyHrs * employeeHrlyRate
federalWithholding = employeeGrossPay * 0.20
stateWithholding = employeeGrossPay * 0.09
totalDeduction = federalWithholding + stateWithholding
netPay = employeeGrossPay - totalDeduction

#Output Formatting
employeeWeeklyHrs = format(employeeWeeklyHrs, ".1f")
employeeHrlyRate = format(employeeHrlyRate, ".2f")
employeeGrossPay = format(employeeGrossPay, ".2f")
federalTaxRate = format(federalTaxRate, ".1%" )
stateTaxRate = format(stateTaxRate, ".1%" )
federalWithholding = format(federalWithholding, ".2f")
stateWithholding = format(stateWithholding, ".2f")
totalDeduction = format(totalDeduction, ".2f")
netPay = format(netPay, ".2f")

#Output
print("Employee Name: "+employeeName)
print("Hours Worked: "+employeeWeeklyHrs)
print("Pay Rate: $"+employeeHrlyRate)
print("Gross Pay: $"+employeeGrossPay)
print("Deductions:")
print("  Federal Withholding ("+federalTaxRate+"): $"+federalWithholding)
print("  State Withholding ("+stateTaxRate+"): $"+stateWithholding)
print("  Total Deduction: $"+totalDeduction)
print("Net Pay: $"+netPay) 