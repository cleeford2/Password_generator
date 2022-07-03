#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#Amount of letters and picked randomly
for char in range(1, nr_letters + 1):
  password.append(random.choice(letters))

#Amount of symbols and picked randomly
for char in range(1, nr_symbols + 1):
  password.append(random.choice(symbols))

#Amount of numbers and picked randomly
for char in range(1, nr_numbers + 1):
  password.append(random.choice(numbers))

random.shuffle(password)

print("\n")
#Check for characters requirements
total_chars = nr_letters + nr_numbers + nr_symbols

if total_chars >= 10:
  print("Your new password is:",''.join(password))
else:
  print("Error generating password:")
  print("At least 12 characters (and up to 100 characters)")