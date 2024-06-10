# PRODIGY_CS_01
Python  program that can encrypt and decrypt text using the Caesar Cipher algorithm.



letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += 26
                    new_index -= num_letters
                plaintext += letters[new_index]
    return plaintext

print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do ypu want to encrypt or decryypt?')
user_input = input('e/d: ').lower()
print()

if user_input =='e':
    print('ENCYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):'))
    text = input('Enter the text to encypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')  
    
      
elif user_input == 'd' :
    print('DECYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):'))
    text = input('Enter the text to Decypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT" {plaintext}')
