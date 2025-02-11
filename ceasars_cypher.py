alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']

logo = '''
   ____                           
  / ___|__ _  ___  ___  __ _ _ __ 
 | |   / _` |/ _ \/ __|/ _` | '__|
 | |__| (_| |  __/\__ \ (_| | |   
  \____\__,_|\___||___/\__,_|_|   
'''
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encrypt text:
def encrypt(original_text, shift_amount):
    encrypted_word = ""
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        encrypted_word += alphabet[shifted_position]

    print(f"Here is the encoded result: {encrypted_word}")

# Decrypt text:
def decrypt(original_text, shift_amount):
    decrypted_word = ""
    
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decrypted_word += alphabet[shifted_position]

    print(f"Here is the encoded result: {decrypted_word}")

# combining the functions to make one function for both
def caesar(original_text, shift_amount, encode_decode):
    decrypted_word = ""
    if encode_decode == "decode":
        shift_amount *= -1


    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        decrypted_word += alphabet[shifted_position]
    print(f"Here is the {encode_decode}d result: {decrypted_word}")

caesar(original_text= text, shift_amount= shift, encode_decode= direction)