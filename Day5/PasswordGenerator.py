import string, random

# Create a list of lowercase letters
alphabet_list_Lower = list(string.ascii_lowercase)
# Output: ['a', 'b', 'c', ..., 'z']
alphabet_list_Upper = list(string.ascii_uppercase)
alphabet_list = alphabet_list_Lower + alphabet_list_Upper
#print(alphabet_list)
digit = list(string.digits)
#print(digit)
special_char = list(string.punctuation)
#print(special_char)
letterCount = int(input("How many letters you want in your password\n"))
symbolCount = int(input("How many symbols you want in your password\n"))
numberCount = int(input("How many numbers you want in your password\n"))
#print(letterCount,symbolCount,numberCount)
password = random.choices(alphabet_list, k=letterCount)
password += random.choices(special_char, k=symbolCount)
password += random.choices(digit, k=numberCount)
print(password)
unshuffeled_password =  "".join(password)
print(unshuffeled_password)
random.shuffle(password)
shuffled_password = "".join(password)
print(shuffled_password)

