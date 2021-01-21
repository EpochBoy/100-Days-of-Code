#added alphabet twice to list to avoid index out of bounds
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")




#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


def decrypt(enc_text, rev_shift):
    dec_text = ""
    for letter in enc_text:
        position = alphabet.index(letter)
        new_position = position-rev_shift
        new_letter = alphabet[new_position]
        dec_text += new_letter
    print(f"The decoded text is {dec_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(enc_text=text, rev_shift=shift)
else:
    print("Incorrect input")

















#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# textlist = []

# def convert_string(text):
#     for i in text:
#         textlist.append(i)


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#Fails on Z and doubling alphabet list breaks logic
# def encrypt(text, shift):
#     convert_string(text)
#     for i in textlist:
#         for j in alphabet:
#             if i == j:
#                 temp1 = alphabet.index(j)+shift
#                 templetter1 = alphabet[temp1]
#                 temp2 = textlist.index(i)
#                 textlist[temp2] = templetter1
#     final_string = "".join(textlist)
#     print(f"The encrypted message is: {final_string}")


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# encrypt(text, shift)



#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit#facit

# facit part 1
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# encrypt(plain_text=text, shift_amount=shift)

