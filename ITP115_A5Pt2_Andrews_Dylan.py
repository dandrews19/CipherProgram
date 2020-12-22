# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Assignment 5, part 2
# Description:
# This program allows a user to make a ciphered message by asking how much they want to shift the alpahbet and then
# creating a message based on that

def main():
    # ask user to input message and number to shift by
    message = input("Enter a message: ")
    while message.isdigit() == True:
        message = input("Enter a message: ")
    shift = input("Enter a number to shift by (0-25): ")
    while not shift.isdigit():
        shift = input("Enter a number to shift by (0-25): ")
    shift = int(shift)
    # initializing alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']
    # creates a new alphabet based on shift user provides
    halfCipher = alphabet[:shift]
    newAlphabet = halfCipher
    newAlphabet = (alphabet[shift:26]) + newAlphabet
    messageList = list(message)
    cipheredWord = []
    n = 0
    # encrypts message based on shifted alphabet
    while n < len(message):
        if message[n] != " ":
            r = alphabet.index(messageList[n])
            cipheredWord.append(newAlphabet[r])
            n = n + 1
        elif message[n] == " ":
            cipheredWord.append(" ")
            n = n + 1
    # prints encrypted message
    print("Encrypting message....\n\tEncrypted message: ", "".join(cipheredWord))
    k = 0
    decryptedWord = []
    # decrypts message and prints it
    while k < len(message):
        if message[k] != " ":
            c = newAlphabet.index(cipheredWord[k])
            decryptedWord.append(alphabet[c])
            k = k + 1
        elif message[k] == " ":
            decryptedWord.append(" ")
            k = k + 1

    print("Decrypting message....\n\tDecrypted message: ", "".join(decryptedWord), "\n\tOriginal message: ",
          message)

main()
