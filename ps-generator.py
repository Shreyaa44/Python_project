import random as r 

class Password_genrator:

    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    symbols = "!@#$%"

    all_chars = letters+numbers+symbols

    def genrate_password(self,length):
        password = ""
        for i in range(length):
            new_character = r.choice(Password_genrator.all_chars)
            password += new_character 

        print("\nGenerated Password:",password)

    
obj = Password_genrator()
obj.genrate_password(10)