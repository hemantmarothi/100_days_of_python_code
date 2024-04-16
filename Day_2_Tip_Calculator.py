#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("$$$ Welcomw to the tip calculator $$$")
total_bill = float(input("What is the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))/100
split_between = int(input("How many people to split the bill? "))
per_person = (total_bill + tip_percent*total_bill)/split_between
print("Each person should pay: $",per_person)