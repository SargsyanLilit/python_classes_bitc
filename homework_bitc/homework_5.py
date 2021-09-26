#1
for i in range(1, 5):
    print("*" * i)
for i in range(5, 0, -1):
    print("*" * i)

#2
for i in range(1, 11):
    print(f"{i} X {i+1} = {i*(i+1)}")

#3
user_number = int(input("Enter a number and I will tell you its divisors:\n"))

for i in range(1, user_number+1):
    if user_number % i == 0:
        print(i)

#4
user_number = int(input("Enter a number and I will tell you its factorial:\n"))

factorial = 1
for i in range(1, user_number+1):
    factorial *= i

print(f"The factorial of {user_number} is {factorial}")

#5
number_1 = 0
number_2 = 1
print_output = ""

while number_1 <= 50:
    print_output += str(number_1) + " "
    sum_ = number_1 + number_2
    number_1 = number_2
    number_2 = sum_

print(f"The Fibonacci Sequence between 0 to 50 is: {print_output}")

#Excercises from class_6.pdf
#1
sum_sequence = 0
for i in range(1,21):
    if i != 3 and i != 13:
        sum_sequence += i

print(f"The sum of (1,20) sequence values (3, 13 are excluded is {sum_sequence}")

#2
sum_sequence = 0
for i in range(1,21):
    if i == 15:
        break
    else:
        sum_sequence += i

print(f"The sum of (1,20) sequence is {sum_sequence} (stopped when reached 15)")
