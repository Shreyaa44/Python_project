# vET CLINIC SYSTEM
class Pet:
    def __init__(self, name, breed, age, health_status):
        self.name = name
        self.breed = breed
        self.age = age
        self.health_status = health_status

    def introduce(self):
        print(f"Name: {self.name} | Breed: {self.breed} | Age: {self.age} | Status: {self.health_status}")


class Clinic:
    
    def __init__(self, clinic_name):
        self.clinic_name = clinic_name
        self.patients = []
        

    def admit_pet(self):
        name          = input("Enter pet name: ")
        breed         = input("Enter breed: ")
        age           = input("Enter age: ")
        health_status = input("Status (Healthy/Sick/Critical): ")
        
        new_pet = Pet(name, breed, age, health_status)
            
        self.patients.append(new_pet)
        
        print(f"{name} admitted!")

    def view_patients(self):
        if len(self.patients) == 0:
            print("No patients currently.")
            return

        for index, pet in enumerate(self.patients, start=1):
            print(f"{index}. {pet.name} | {pet.breed} | Age: {pet.age} | Status: {pet.health_status}")

    def treat_pet(self):
        pet_name = input("Enter pet name to treat: ")
        for pet in self.patients:
            if pet.name == pet_name:
                pet.health_status = "Healthy"
                print(f"{pet.name} has been treated!")
                return
        print("Pet not found.")

    def discharge_pet(self):
        pet_name = input("Enter pet name to discharge: ")
        for pet in self.patients:
            if pet.name == pet_name:
                print(f"--- Discharge Bill ---")
                print(f"Patient : {pet.name}")
                print(f"Bill    : Rs 450")
                self.patients.remove(pet)
                print("Discharged successfully!")
                return
        print("Pet not found.")

    def display(self):
        while True:
            print(f"\n--- {self.clinic_name} ---")
            print("1. Admit a pet")
            print("2. View all patients")
            print("3. Treat a pet")
            print("4. Discharge a pet")
            print("5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.admit_pet()
            elif choice == "2":
                self.view_patients()
            elif choice == "3":
                self.treat_pet()
            elif choice == "4":
                self.discharge_pet()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")


clinic = Clinic("City Vet")
clinic.display()