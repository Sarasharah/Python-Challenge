import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

Total = 0
Months_Counter = 0
Greatest_Increase = 0
Greatest_Decrease = 0
This_Amount = 0
Best_Month = "xxx"
Worst_Month = "yyy"
First_Month = True

# Open and read csv
with open (budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header
    csv_header = next (csv_file)

    
    # Read through each row of data after the header row
    # The amountof P/L for each month is stored as This_Amount
    # After the first month, the previous month's This Amount
    # becomes the current month's Last Amount and we then find This_Amount
    # for the current month. After the first month, the monthly change is
    # This_amount - Last_amount.  We then check if this change is 
    # more positive than the greatest increase so far, or more negative
    # than the greatest decrease so far.
    # First_Month is a variable that is initially True.  When we do 
    # process the first month row , (i) we don't have a Last_Month value   
    # to change, but (ii) we want to  store the first month's This_Amount 
    # as Begin_Amount (so we can use it for the Average Change formula),
    # and (iii) we want to change Begin_Month to False.
    
    
    for row in csv_reader:
        Months_Counter += 1

        if First_Month == False: 
            Last_Amount = This_Amount
        
        This_Month = row[0] 
        This_Amt = row[1]
        This_Amount = int(This_Amt)
        Total += This_Amount
            
        if First_Month == True: 
            Begin_Amount = This_Amount
            First_Month = False
        else:
            This_Change = This_Amount - Last_Amount
        
            if This_Change > Greatest_Increase:
                Greatest_Increase = This_Change
                Best_Month = This_Month
        
            if This_Change < Greatest_Decrease:
                Greatest_Decrease = This_Change
                Worst_Month = This_Month

 
print ("Total Months: ", Months_Counter)
print ("Total: $", Total)
print ("Average Change: ", (This_Amount - Begin_Amount) / (Months_Counter - 1 ))
print ("Greatest Increase in Profits: ", Best_Month, " $", Greatest_Increase)
print ("Greatest Decrease in Profits: ", Worst_Month, " $", Greatest_Decrease)

#output path for writing to text file.
analysis_file = os.path.join("Analysis", "analysis.txt")

#Write to text file
with open(analysis_file, "w") as txt:
    txt.write("Financial Analysis\n")
    txt.write("-------------------------------\n")
    txt.write(f"Total Months:  {Months_Counter}\n")
    txt.write(f"Total: $ {Total}\n")
    txt.write(f"Average Change: $ {(This_Amount - Begin_Amount) / (Months_Counter - 1) }\n")
    txt.write(f"Greatest Increase in Profits:  {Best_Month} $ {Greatest_Increase}\n")
    txt.write(f"Greatest Decrease in Profits:  {Worst_Month} $ {Greatest_Decrease}")
