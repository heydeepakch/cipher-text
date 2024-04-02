import random
import string

characters =  list(" "+string.ascii_letters+ string.digits + string.punctuation)
# print(f"characters are : {characters}")

keys = characters.copy()
random.shuffle(keys)
# print(f"Keys are : {keys}")
hashed_pw= ""
password = input("Enter Password: ")

for ch in password:
    ch_ind=characters.index(ch)
    hashed_pw+=keys[ch_ind]
print(f"Encrypted Password: {hashed_pw}")

encryptedpw = input("Enter Encrypted Password: ")
normaltxt = ""
for ch in encryptedpw:
    ch_ind=keys.index(ch)
    normaltxt+=characters[ch_ind]

print(normaltxt)




