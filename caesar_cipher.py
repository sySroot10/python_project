alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
print("""            
                                        _       _               
                                       (_)     | |              
    ___ __ _  ___ ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __ 
   / __/ _` |/ _ / __|/ _` | '__|  / __| | '_ \| '_ \ / _ | '__|
  | (_| (_| |  __\__ | (_| | |    | (__| | |_) | | | |  __| |   
   \___\__,_|\___|___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                         | |                    
                                         |_|      sySroot                                      
""")
direction = input("Type 'e' to encrypt, type 'd', to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))


# encrypted function
def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)

        new_position = position + shift_amount
        if new_position >= len(alphabet):
            cipher_text += alphabet[new_position-len(alphabet)]
        else:
            cipher_text += alphabet[new_position]
    print("Here your encrypted text: ", cipher_text, end='')


# decrypted function
def decrypt(encrypted_text, shift_amount):
    decrypted_text = ''
    for letter in encrypted_text:
        position = alphabet.index(letter)
        new_position = position - shift
        decrypted_text += alphabet[new_position]
    print("Here your decrypted text: ", decrypted_text, end='')


if direction == "e":
    encrypt(text, shift)
elif direction == "d":
    decrypt(text, shift)
else:
    print("Invalid!!")

i = True
while i:
    new_input = input("\nDo you want to go again? (yes/no): ")
    if new_input == "yes":
        direction = input("Type 'e' to encrypt, type 'd', to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number: \n"))
        if direction == "e":
            encrypt(text, shift)
        elif direction == "d":
            decrypt(text, shift)
        else:
            print("Invalid!!")
    elif new_input == "no":
        i = False
    else:
        print("Invalid!!!")
