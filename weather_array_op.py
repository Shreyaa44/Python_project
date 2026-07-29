import numpy as np
from tabulate import tabulate

print("WEATHER ARRAY ANALYZER")

temp_gen = np.random.randint(15,55,size=(7,3))

def temp_table(): # DISPLAYS ARRAY IN TABULAR FORMAT USING TABULATE LIB  
    headers = ["MUMABI","DELHI","BANGLORE"]
    #row_names = ["Temp 1","Temp 2", "Temp 3","Temp 4","Temp 5","Temp 6","Temp 7"]
    print(tabulate(temp_gen,headers=headers,tablefmt="fancy_grid",numalign="center"))

    #print("Temperature table: \n",temp_gen)

def array_info(): #Displays type
    print("Type of array:",type(temp_gen))


def show_temp(): #Displaying Single column total
    a = temp_gen[:,0].sum()
    
    print("Sum of One Day's Temp is:",a)

def mornin_temp():
    b = temp_gen[:,1].sum()

    print("Sum of Morning's Tempeature is: ",b)

def avg_temp():
    c = temp_gen.mean(axis=0)
    d = temp_gen.mean(axis=1)
    print("Avg Temperature is for column is: ",c)
    print("Avg Temperature for row is: ",d)

def highest_temp():
    e = temp_gen.max()
    print("Average temperature experienced is:",e)

def lowest_temp():
    f = temp_gen.min()
    print("Lowest Temperature experienced is:",f)

def increament_reading():
    increment = temp_gen + 2
    print(tabulate(temp_gen,headers=["MUMBAI","DELHI","BANGLORE"],tablefmt="grid",rowalign="center"),"\nIncremented Weather Data")


def comparison():
    print("Temperature above 35'C:",temp_gen[temp_gen>35])

def sort():
    sort_ = np.sort(temp_gen,axis=1)
    print("Sorting of Mumbai's Weather: ",sort_)



def menu():
     
    while True:
    
        choice = int(input(
                           "1.Display Temperature Table\n" 
                            "2.Array Information\n"
                            "3.Show One Day's Temperature\n"
                            "4.Show Morining Temperature\n"
                            "5.Average Temperature\n"
                            "6.Highest Temperature\n"
                            "7.Lowest Temperature\n"
                            "8.Increase Every Reading by 2°C\n"
                            "9.Show Temperatures Above 35°C\n"
                            "10.Sort One Day's Readings\n"
                            "11.Exit\n"
                            "Enter Num according to your Choice: "))

        if choice == 1:
            temp_table()
            input("\nPress Enter To Continue...") 
        elif choice == 2:
            array_info()
            input("\nPress Enter To Continue...")
            
        elif choice == 3:
            show_temp()
            input("\nPress Enter To Continue...")

        elif choice == 4:
            mornin_temp()
            input("\nPress Enter To Continue...")

        elif choice == 5:
            avg_temp()
            input("\nPress Enter To Continue...")

        elif choice == 6:
            highest_temp()
            input("\nPress Enter To Continue...")

        elif choice == 7:
            lowest_temp()
            input("\nPress Enter To Continue...")

        elif choice == 8:
            increament_reading()
            input("\nPress Enter To Continue...")

        elif choice == 9:
            comparison()
            input("\nPress Enter To Continue...")

        elif choice == 10:
            sort()
            input("\nPress Enter To Continue...")

        elif choice == 11:
            print("Exiting...")
            break

menu()