alphastr='abcdefghijklmnopqrstuvwxyz'
encryptedmsg=""
curpos=0
msg=input("Enter your message that is to be encrypted :")
key=int(input("Enter the key "))
key+=1
for char in msg:
    if char in msg:
        curpos=alphastr.find(char)
        addingele=(curpos+key)%len(alphastr)
        encryptedmsg+=alphastr[addingele]
    else:
        encryptedmsg+=char
print(encryptedmsg)
