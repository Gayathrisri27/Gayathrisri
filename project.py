import re
import random
import array
print("\t\t\tWelcome to West Pharmaceutical Services\t\t\n")
print(""" 
 Employee Password Bank-Keep your password strong!!	
 """ )
name=str(input("enter your name:"))
id=int((input("enter your employee id number:")))
password = input("enter your password:")
flag = 0
while True:
    if (len(password)<=8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]" , password):
        flag = -1
        break
    elif re.search("\s" , password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        print("Thank you for visiting the bank,see you soon even more stronger")
        break
 
if flag == -1:
    print("Not a Valid Password ")
    pwd=str(input("do you want a strong password(y/n):"))
    if pwd=="y":
        MAX_LEN = 8
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 

        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
 
# randomly select at least one character from each character set above
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
 
# combine the character randomly selected above
# at this stage, the password contains only 4 characters but
# we want a 12-character password
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 
# now that we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
 
# traverse the temporary password array and append the chars
# to form the password
            password = ""
        for x in temp_pass_list:
            password = password + x
         
# print out password
        print("The password suggested for you is:",password)
        print("Thank you ")
else:
       print("Thank you for visiting ,see you soon even more stronger")
