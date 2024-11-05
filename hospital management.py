
print("HOSPITAL MANAGEMENT:-")
class Patient:                                   #class method 1
    people = {}
    fields = ['Patient ID','Patient Name', 'Age', 'Condition']
    
    def ram(self):
        while True:                              # using option
            print("\n1. Add Patient Details\n2. Add Appointment Details\n3. View Patient Details\n4. Exit") 
            option = int(input())                 
            if option == 1:
                self.patientAdd()
            elif option == 2:
                x = ScheduleAppointment()
                x.appointment()
            elif option == 3:
                print("1. View Patient List\n2. View Appointment List\n3. View Patient Condition\n4. Delete Patient List")
                y = int(input())
                if y == 1:
                    self.get_patients()
                elif y == 2:
                    a = ScheduleAppointment()
                    a.get_appointment()
                elif y==3:
                    self.get_condition()
                elif y==4:
                    patient_name = input("Enter the Patient Name to delete: ")
                    self.delete_patients_list(patient_name)
                    
            elif option ==4:
              print("Thanks For Yours Details")
              break
                 
            else:
                print("INVALID")

    def patientAdd(self):                                 #add patient function
        patient_data = {}
        for i in self.fields:
            a = input(f'Enter {i}: ')
            patient_data[i] =a
        self.people[patient_data['Patient Name']] = patient_data
        print("Patient Details Added Successfully")

    def get_patients(self):                              #view patient list function
        if not self.people:
            print("No patients found.")
        else:
            print("Patient List:")
            for name, details in self.people.items():
                print(f"Patient ID: {details['Patient ID']},Name: {details['Patient Name']}, Age: {details['Age']}, Condition: {details['Condition']}")
                
    def get_condition(self):                            #view patient condition function & using map method
        if not self.people:
            print("Patient Details Not Found")
        else:
            print("Patient Condition List")              
            conditions = map(lambda details: f"Condition: {details['Condition']}, Name: {details['Patient Name']}, Age: {details['Age']}", self.people.values())
            for i in conditions:
                print(i)

    def delete_patients_list(self, patient_name):  # Delete patient function & filter method
        filtered_patients = list(filter( name == patient_name, self.people.keys()))
        if filtered_patients:
            deleted_patient = self.people.pop(filtered_patients[0])  # 
            print(f"Patient '{deleted_patient['Patient Name']}' has been deleted.")
        else:
            print("Patient not found.")
                
class ScheduleAppointment:          #class method 2
    appointments = {}
    fields = ['Patient ID','Patient Name', 'DutyDoctor', 'Date']

    def appointment(self):                                       # add appointment function
        appointment_data = {}
        for i in self.fields:
            b = input(f'Enter {i}: ')
            appointment_data[i] = b
        self.appointments[appointment_data['Date']] = appointment_data
        print("Appointment Added Successfully")

    def get_appointment(self):                                  # view appointment list function      
        if not self.appointments:
            print("No appointments found.")
        else:
            print("Appointment List:")
            for date, details in self.appointments.items():
                print(f"Date: {date},ID: {details['Patient ID']}, Patient Name: {details['Patient Name']}, Duty Doctor: {details['DutyDoctor']}")


      
task= Patient()
task.ram()





  
    





