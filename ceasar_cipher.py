alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


"""
def encrypt(plain_text, shift_amount):
    alphabet_place = []
    for t in plain_text:
        # print("1" + t)
        for letter in alphabet:
            # print("2" + letter)
            if letter == t:
                # print("t=letter")
                alphabet_place.append(alphabet.index(letter) - len(alphabet) + shift_amount)
    encoded_message = ""
    for position in alphabet_place:
        # print(position)
        encoded_message += alphabet[position]
    print(f"The encoded message is: {encoded_message}")


def decrypt(cipher_text, shift_amount):
    alphabet_place = []
    for t in cipher_text:
        # print("1" + t)
        for letter in alphabet:
            # print("2" + letter)
            if letter == t:
                # print("t=letter")
                alphabet_place.append(alphabet.index(letter) - shift_amount)
    decoded_message = ""
    for position in alphabet_place:
        # print(position)
        decoded_message += alphabet[position]
    print(f"The decoded message is: {decoded_message}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

"""