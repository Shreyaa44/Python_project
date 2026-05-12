#"DigiLocker Basic Login System
print("--------------Sign-up State-------------")
a = input("Create a username: ")
while True:
        b = input("Create a 4-Digit Pin: ")
        if len(b) == 4:
                print("--------LOGIN-------" \
                "-------------")
                break
        else:
                print("Invalid pin. Enter 4 numbers only")


       
while True:     
        c = input("Enter your username: ")
        if c == a:
               print("Correct")
               break
        else:
               print("Re-try :(")
attempts = 0 
while attempts<=3:
    entered_pin = input("Enter Your pin: ")
    if entered_pin == b:
        print("Access Granted")
        break
    else:
        attempts+=1
        print("Wrong Pin,Try again")
else:
    print("Account Blocked")

print("-------------Menu State-------------")
def menu_page():
        money = 1000
        while True:
        
                choice = (input("Enter any number from the Menu as per your choice: \n"
                           "1. View Locker balance \n"
                           "2. Add Money \n"
                           "3. Remove Money \n"
                           "4. Exit\n"))
        
                if choice == "1":
                        print("Locker balance: ",money)
                elif choice == "2":
                        x= int(input("Add money:"))
                        money+=x
                        print("Updated balance:",money)
                elif choice == "3":
                        y= int(input("Remove money: "))
                        if money<0:
                                print("Insuffient balance")
                        else:
                               print("updated amount: ",money)
                        money-=y
                                
                elif choice =="4":
                        break  
menu_page()           

             
           
                    
                

    

      

             