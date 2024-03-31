import random 

import array 

  

# maximum length of password needed 

# this can be changed to suit your password length 

MAX_LEN = 12 

  

# declare arrays of the character that we need in out password 

# Represented as chars to enable easy string concatenation 

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

  

# combines all the character arrays above to form one array 

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS 

  

# randomly select at least one character from each character set above 

rand_digit = random.choice(DIGITS) 

rand_upper = random.choice(UPCASE_CHARACTERS) 

rand_lower = 

