import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@',"#","$","%","&","*"]

print("Password Generator:")
let_length = int(input("Enter the length of letters: ")) 
num_length = int(input("Enter the length of numbers: "))
sym_length = int(input("Enter the length of symbol: "))

password = []

for i in range(let_length):
    password += random.choice(letters)
    
for i in range(num_length):
    password += random.choice(numbers)
    
for i in range(sym_length):
    password += random.choice(symbol)

random.shuffle(password)    

password_final = ""
for i in password:
    password_final += i
    
print(password_final)
