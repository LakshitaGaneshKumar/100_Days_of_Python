# greet the user
print("Welcome to the Tip Calculator")

# generate user input for the total bill amount, tip %, and number of people spliting the bill
total = input("What was the total bill? $")
tip_amt = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_ppl = input("How many people to split the bill? ")

# convert each inputed value into the correct data type
total_float = float(total)
tip_amt_int = int(tip_amt)
num_ppl_int = int(num_ppl)

# calculate and add tip to the total amt
tip = total_float * (tip_amt_int / 100)
total_with_tip = total_float + tip

# split the total bill between the number of people and format the amt to two decimal places
split_amt = total_with_tip / num_ppl_int
split_formated = "{: .2f}".format(split_amt)

# print result
print(f"Each person should pay: ${split_formated}")
