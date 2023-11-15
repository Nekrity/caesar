a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def e(t, o): #Encrypt (text, rotation)
  r = ""
  for c in t: #text encrypting (t=text)
    if (a.find(c) == -1): #if can't find simbol then won't replace it
      r += c
    else: # else replace a letter by a number equal to a rotation % 26
      r += (a[(a.find(c) + o) % len(a)])
  return r

def d(t, o): #Decrypt (text, rotation)
  r = ""
  for c in t: #text decrypting (t=text)
    if (a.find(c) == -1): #if can't find simbol then won't replace it
      r += c
    else: # else replace a letter by a number equal to a rotation % 26
      r += (a[(a.find(c) - o) % len(a)])
  return r

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1: #if first mode is selected then encrypt text
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + e(text, rotation))
elif mode == 2: #if second mode is selected then decrypt text
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + d(text, rotation))
elif mode == 3: #if third mode is selected then try to bruteforce all rotations
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
