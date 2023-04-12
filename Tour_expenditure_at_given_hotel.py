'''Tour Expenditure at Given Hotel 

The family has spent the vacation in Goa and now they are returning home to do so they will have to check out from the hotel.

Tariff on Room: Delux Room- 7500 INR

                            Non AC Room- 4500 INR 

You  as a developer has to create a program for a hotel owner which has the following requirements,

The program should begin with taking input from the checkout counter 

Type of room booked 
Total number of days 
Total Amount on Food (Amount is expected )
There are the following cases to be considered while generating a bill.

The tax on food amount is dependent on the type of room booked.

Tax on food for the deluxe room will be billed  18% of the total food amount.

Tax on food for the Non AC room will be billed  5% of the total food amount.

You are supposed to include a tip of 10% on the food amount.

The output from your program should include;

The  Room Tariff on the number of days spend, GST on a meal(Breakdown of GST is necessary based on CGST and SGST and same has to get reflected on console ) 

The tip amount, and the grand total for the meal including both the tax and the tip.

Format the output so that all of the values are displayed using two decimal places.'''

room_type = input("Type of room booked (Deluxe/Non AC): ")
num_days = int(input("Total number of days: "))
food_amount = float(input("Total amount on food: "))


if room_type.lower() == "deluxe":
    room_tariff = 7500 * num_days
    food_tax_rate = 0.18
elif room_type.lower() == "non ac":
    room_tariff = 4500 * num_days
    food_tax_rate = 0.05
else:
    print("Invalid room type entered.")
    exit()

food_tax = food_amount * food_tax_rate
cgst = food_tax / 2
sgst = food_tax / 2
tip_amount = food_amount * 0.1
grand_total = room_tariff + food_amount + food_tax + tip_amount

print(f"Room Tariff: {room_tariff:.2f} INR")
print(f"GST on Food: CGST {cgst:.2f} INR + SGST {sgst:.2f} INR = {food_tax:.2f} INR")
print(f"Tip Amount: {tip_amount:.2f} INR")
print(f"Grand Total: {grand_total:.2f} INR")