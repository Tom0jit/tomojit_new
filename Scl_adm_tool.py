#Project1
import csv

def change_csv(i_list):
    with open('st_info.csv', 'a', newline='')as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])

        writer.writerow(i_list)

if __name__=='__main__':
    c= True
    st_num= 1

    while(c):
        st_info = input("Enter the student information for student #{} in the given format (Name Age Contact_no Email_ID): ".format(st_num))

        info_list= st_info.split(' ')

        print("\nThe Entered info is -\nName: {}\nAge: {}\nContact_number: {}\nE-Mail ID: {}".format(info_list[0], info_list[1], info_list[2], info_list[3]))

        choice_check = input("Is the entered information correct? (Yes/No):")

        if choice_check== "Yes":
            change_csv(info_list)

            check = input("Enter (Yes/No) to continue:")
            if check=="Yes":
                c= True
                st_num = st_num + 1
            elif check=="No":
                c= False
        elif choice_check== "No":
            print("\nPlease re-enter the values.")
            
        
        
    
        
      
    
    
