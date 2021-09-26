#1
user_text = input("Enter the text:\n")

if len(user_text) >= 3:
	if user_text.endswith("ing"):   
		new_text = user_text + "ly"
	else:
		new_text = user_text + "ing"
	print(new_text)
else:
	print(user_text)


#2
user_text = input("Enter the text:\n")

not_index = user_text.find("not")
poor_index = user_text.find("poor")

if 0 <= not_index < poor_index:
	new_text = user_text[:not_index] + "good" + user_text[poor_index+4:]
	print(new_text)
else:
	print(user_text)


#3	
user_text = input("Enter the text:\n")

first_char = user_text[0]
new_text = first_char + user_text.replace(first_char,"$")[1:]

print(new_text)

#4
user_text = input("Enter the text:\n")
count_even_digits = 0

for char in user_text:
	if char.isdigit() and int(char)%2 == 0:
		count_even_digits +=1

print(f"The number of the even digits in the '{user_text}' is {count_even_digits}.")

#5
user_text = input("Enter the text:\n")

print(user_text[::2])
