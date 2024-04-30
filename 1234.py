alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text1,shift1):
    cipher_text = ""
    if direction == "encode":
        for letter in text1:
            if letter == " ":
                cipher_text += str(" ")
            else:   
                position = alphabet.index(letter)
                new_position = position + shift1
                new_letter = alphabet[new_position]
                cipher_text += str(new_letter)
        print(cipher_text)
    elif direction == "decode":
        for letter in text1:    
            if letter == " ":
                cipher_text += str(" ")
            else:
                position = alphabet.index(letter)
                new_position = position - shift1
                new_letter = alphabet[new_position]
                cipher_text += str(new_letter)
        print(cipher_text)
    else:
        raise ValueError("You have to type 'encode' or 'decode'")        
        


encrypt(text,shift)



