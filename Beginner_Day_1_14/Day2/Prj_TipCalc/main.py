print("Welcome to the tip calculator!!")
bill_Total = input("What was the total bill? ")
percentage_Tip = input("What percentage tip would you like to give? ")
amount_Split = input("How many people are splitting this bill? ")

bill = float(bill_Total)
tip = int(percentage_Tip)
guests = int(amount_Split)

tip_per_guest = (bill / guests) * (1+(tip/100))

# rounded = round(tip_per_guest, 2)

#Print like this with formatting that adds a 0
print("Each guest must pay {:.2f}".format(tip_per_guest))
