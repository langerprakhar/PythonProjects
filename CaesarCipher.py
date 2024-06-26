#CAESAR CIPHER CODE

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
sum=0
new_position=0
if direction.lower()=='encode':
    def encrypt(plain_text,shift_amt):
        cipher_text=""
        for letter in plain_text:
            position=alphabet.index(letter)
            new_position=(position+shift_amt)%26
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        print(f"The encoded text is {cipher_text}")

    encrypt(plain_text=text,shift_amt=shift)
elif direction.lower()=='decode':
    def decrypt(plain_text,shift_amt):
        cipher_text=""
        for letter in plain_text:
            position=alphabet.index(letter)
            new_position=(position+(len(alphabet)-shift_amt))%26
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        print(f"The decoded text is {cipher_text}")
    decrypt(plain_text=text,shift_amt=shift)
else:
    print("enter either encode or decode!")