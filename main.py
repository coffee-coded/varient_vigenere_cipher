def encryption(ch, n):
    # xor is applies on the ascii of the characters
    return chr((ord(ch)^ord(n)))


x = input("Enter text to be encrypted : ")
n = input("Enter the key to be used : ")
enc = ""
dec = ""
print("Encrypted")
inc = 0
for i in x:
    enc = enc + encryption(i, n[inc % len(n)])
    inc = inc + 1
print("Encrypted message : ", enc)
print("Decrypted")
inc = 0
for i in enc:
    dec = dec + encryption(i, n[inc % len(n)])
    inc = inc + 1
print("Decrypted message : ", dec)
