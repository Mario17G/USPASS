import random


def create_user(name,birthdate,hobby):

    one = birthdate[-1]
    noSpacesN = name.split()
    two = noSpacesN[0]
    noSpacesH = hobby.split()
    union = ''.join(noSpacesH)
    three = union[0:2] 
    four = birthdate[6]
    five = birthdate[3]

    return one + two + three + four + five 



def create_password(length, capitalLetters=False, specialCharacters=False, numbers=False):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sC = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    chars = abc  
    if capitalLetters:
        chars += upper
    if specialCharacters:
        chars += sC
    if numbers:
        chars += num

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
