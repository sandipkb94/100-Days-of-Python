def ceaserCipher(choose, word, shift) :
    encodedWord = ""
    for char in word :
        encodedWord += chr(((ord(char) + shift - 97)%26 + 97))
    print(encodedWord)

flag = True
while  flag :
    choose = input("Want to encode or decode? : ").lower()
    word = input("Enter the word : ")
    shift = int(input("How many letters to shift? : "))
    if choose == "decode" :
        shift = -shift
    ceaserCipher(choose, word, shift)
    choice = input("Want to check again? yes/ no :").lower()
    if choice == "no" :
        flag = False