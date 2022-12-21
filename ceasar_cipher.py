alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    alphabet_place = []
    for t in text:
        # print("1" + t)
        for letter in alphabet:
            # print("2" + letter)
            if letter == t:
                # print("t=letter")
                alphabet_place.append(alphabet.index(letter) - len(alphabet) + shift)
    encoded_message =""
    for position in alphabet_place:
        # print(position)
        encoded_message += alphabet[position]
    print(encoded_message)
        
        
encrypt(text, shift)