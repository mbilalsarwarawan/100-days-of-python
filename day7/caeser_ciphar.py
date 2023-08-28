from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


def ceaser(start_text, shift, direction):
    end_text = ""
    shift %= 26
    for letter in start_text:

        try:
            position = alphabet.index(letter)
            if direction == "encode":
                position = position+shift
            elif direction == "decode":
                position = position-shift
            end_text = end_text+alphabet[position]
        except ValueError:
            end_text += letter

    print(end_text)


print(logo)
run = "yes"
while run == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    run = input("Do you wan to run run it again!. Type yes or no\n")

# def encrypt(text, shift):
#     encrypted = ""
#     for n in text:
#         position = alphabet.index(n)
#         position = position+shift
#         encrypted = encrypted+alphabet[position]
#     print(encrypted)


# encrypt(text, shift)


# def decrypt(text, shift):
#     dencrypted = ""
#     for n in text:
#         position = alphabet.index(n)
#         position = position-shift
#         dencrypted = dencrypted+alphabet[position]
#     print(dencrypted)


# decrypt("avmv", 1)
