import art
def caesar(text,shift,direction):
    new_string = ""
    shift = shift % 26
    for i in text:
        if direction == "encode":
            if i.isalpha():
                new_pos = alphabet.index(i) + shift
                new_letter = alphabet[new_pos]
                new_string += new_letter
            else:
                new_string += i
        
        elif direction == "decode":
            if i.isalpha():
                new_pos = alphabet.index(i) - shift 
                new_letter = alphabet[new_pos]
                new_string += new_letter
            
            else:
                new_string += i

        else:
            return "we do not recognize the direction"
    print(f"The beginning of the string is {text}, and the end result is {new_string}")
    return new_string 



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(text=text,shift=shift,direction=direction)
agian = input("Would you want to go again?(Y/N)")

while agian == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text,shift=shift,direction=direction)
    agian = input("Would you want to go again?(Y/N)")

print("Thanks for using our program. Goodbye")




   



