#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#print("Welcome to the PyPassword Generator!")
nr_letters= random.randint(8,10) 
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

New_passwordL = [random.choice(letters) for l in range(nr_letters)]
New_passwordN = [random.choice(numbers) for l in range(nr_numbers)]
New_passwordS = [random.choice(symbols) for l in range(nr_symbols)]

New_password = New_passwordL+New_passwordN+New_passwordS
random.shuffle(New_password)
password1 = "".join(New_password)
#print(password1)