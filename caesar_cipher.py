alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(text, rotation): #Encrypt (text, rotation)
    result = ""
    for caesar in text: #text encrypting (t=text)
      if (alphabet.find(caesar) == -1): #if can't find simbol then it stays
        result += caesar
      else: # else replace a letter by a number equal to a rotation % 26
        rotated=alphabet.find(caesar) + rotation
        result += (alphabet[rotated % len(alphabet)])
    return result

def decrypt(text, rotation): #Decrypt (text, rotation)
    result = ""
    for caesar in text: #text decrypting (t=text)
      if (alphabet.find(caesar) == -1): #if can't find simbol then it stays
        result += caesar
      else: # else replace a letter by a number equal to a rotation % 26
        rotated=alphabet.find(caesar) - rotation
        result += (alphabet[rotated % len(alphabet)])
    return result

select = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(select))

if mode == 1: #if first mode is selected then encrypt text
    text = input("Enter the text: ")
    rotation = int(input("Enter the rotation: "))
    print("Encrypted: " + encrypt(text, rotation))
elif mode == 2: #if second mode is selected then decrypt text
    text = input("Enter the text: ")
    rotation = int(input("Enter the rotation: "))
    print("Decrypted: " + decrypt(text, rotation))
elif mode == 3: #if third mode is selected then bruteforce all rotations
    print("Bruteforcing...")
    print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
