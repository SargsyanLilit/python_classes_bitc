#1
print("-"*100)

kilometers = float(input("Enter the kilometers: \n"))
print(kilometers, "km is equal to", kilometers*1.60934, "mi.")


#2
print("-"*100)

from rates import *
currency = input("Enter the currency you want to convert to USD: 'AMD', 'RUB' or 'EUR'\n")
amount = float(input("Enter the amount you want to convert:\n"))

if currency == "AMD":
	amount_USD = rate_AMD_USD * amount
elif currency == "RUB":
	amount_USD = rate_RUB_USD * amount
else:
	amount_USD = rate_EUR_USD * amount

print(currency, amount, "=", "USD", amount_USD,)


#3
print("-"*100)

day_number = input("Enter the day number from 0 to 6:\n")

if day_number == "0":
	print("Sunday")
elif day_number == "1":
	print("Monday")
elif day_number == "2":
	print("Tuesday")
elif day_number == "3":
	print("Wednesday")
elif day_number == "4":
	print("Thursday")
elif day_number == "5":
	print("Friday")
else:
	print("Saturday")


#4
print("-"*100)

user_text = input("Enter the text: \n")

if " " in user_text:
	print("There is a space in the text.")
else:
	print("There is no space in the text.")


#5
print("-"*100)

number_1 = int(input("Enter the first number:\n"))
number_2 = int(input("Enter the second number:\n"))
number_3 = int(input("Enter the third number:\n"))

max_number = number_1

if number_2 >= number_1:
	if number_3 > number_2:
		max_number = number_3
	else:
		max_number = number_2
elif number_2 < number_1:
	if number_3>=number_1:
		max_number = number_3

print("The highest number is", max_number)

#6
print("-"*100)

check_year = int(input("Enter the year: \n"))

if check_year % 4 == 0:
	if check_year % 100 == 0:
		if check_year % 400 == 0:
			print(check_year, "is a leap year.")
		else:
			print(check_year, "is not a leap year.")

	else:
		print(check_year, "is a leap year.")
else:
	print(check_year, "is not a leap year.")







