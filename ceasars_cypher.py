alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
             'u', 'v', 'w', 'x', 'y', 'z']
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
encrypt(original_text= text, shift_amount= shift)

# Decrypt text:
