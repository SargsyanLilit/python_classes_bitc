#1-a
print("-"*100)
temp_celsius = float(input("Enter the temperature in °C:\n"))
temp_fahrenheit = temp_celsius*1.8 + 32
print(temp_celsius, "°C = ", temp_fahrenheit, "°F", sep = "")


#1-b
print("-"*100)
a=5
b=6
c=7
#i
print("The average of a, b, c is", (a+b+c)/3)
#ii
print("a^c + b^c is equal to ", a**c + b**c)
#iii
print("(a + b)^c is equal to ", (a + b)**c)
#iiii
print("abc + a*b*c is equal to ",a*100+b*10+c + a*b*c)


#1-c
print("-"*100)
height = float(input("Enter your height in cm:\n"))
BMI_normal_min = 18.5 * (height/100)**2
BMI_normal_max = 24.9 * (height/100)**2
print("The optimal weight for you is from",BMI_normal_min, '-', BMI_normal_max)


#Extra task
print("-" * 100)
price_pizza = 1000
price_kebab = 1500
price_ketchup = 100
price_mayonez = 500

main_choice = input("Enter 'Pizza' or 'Kebab'\n")
addition_choice = input("Enter 'Mayonez' or 'Ketchup'\n")
user_order = (main_choice+addition_choice)

print("You have ordered Pizza with Mayonez and your price is ", price_pizza + price_mayonez, "PizzaMayonez" == user_order)
print("You have ordered Pizza with Ketchup and your price is ", price_pizza + price_ketchup, "PizzaKetchup" == user_order)
print("You have ordered Kebab with Mayonez and your price is ", price_kebab + price_mayonez, "KebabMayonez" == user_order)
print("You have ordered Kebab with Ketchup and your price is ", price_kebab + price_ketchup, "KebabKetchup" == user_order)

