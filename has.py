"""from cryptography.fernet import Fernet

userInput= input("Type any thing!")
key = Fernet.generate_key()

# Instance the Fernet class with the key
fernet = Fernet(key)

#encode the input data
encMessage = fernet.encrypt(userInput.encode())

print("original string: ", userInput)
print("encrypted string: ", encMessage)

#decode the input data
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
"""
print(hash("test"))
