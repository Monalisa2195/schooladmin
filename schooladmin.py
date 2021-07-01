import csv
def write_in_csv(list):
    with open ('student_info.csv', 'a', newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
         writer.writerow(["NAME","AGE","CONTACT NO","EMAIL-ID"])
        writer.writerow(info_list)

#if _name_ == '_main_':
condition = True
student_num=1
while (condition):
   student_info=input("Enter student details in following format (NAME , AGE , CONTACT_NO , EMAIL-ID) separated by comma:")
   check=input("You want to edit details 'YES/NO':")
   if check=="YES":
     student_info=input("Enter student details in following format (NAME , AGE , CONTACT_NO , EMAIL-ID):")
   info_list = student_info.split(',')
   print(info_list)
   write_in_csv(info_list)
   condition_check=input("Enter 'YES' if you want to add another student's details otherwise 'NO':")
   if condition_check=="YES":
    condition=True
    student_num+=1
   elif condition_check=="NO":
    condition=False
