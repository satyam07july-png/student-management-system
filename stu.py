import pyttsx3
import os
import time

#-------------------------- voice fuction -------------------------------------
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)

#------------------------------ file name -----------------------------------------
FILE_NAME = "STUDENT.TXT"

#----------------------------- add fuction -----------------------------------------
def add_student():
    name = input("enter student name: ")
    roll_no = int(input("enter roll_no"))
    course  = input("enter course")
    marks = float(input("enter marks"))# we use float beause marks are also in points 

    with open(FILE_NAME,"a") as files: # this fuction use for permantaly save student data "a" are use to add new add and save perivous one 
        files.write(f"{name},{roll_no},{course},{marks}\n")

    print("student entred succefully")
    speak("student entred succefully ")

#---------------------------------view student --------------------------------
def view_student():
    if not os.path.exists(FILE_NAME):
        print("no student record find")
        speak("no student record find")
        return
    print("student record find ")
    with open(FILE_NAME,"r") as files:# here the fuction are use open easily "r" used for read only
        for line in files:# loop are used to again again data are print which we are saved 
            name,roll_no,course,marks = line.strip().split(",")# line strip are used to remove the space and split are used to commoa witten every one input
            print(f"Name: {name} | roll_no: {roll_no} | course: {course} | marks: {marks}")
    
    speak("showing all record of student")

#------------------------------- search fuction ------------------------------
def search_student():
    search_name = input("enter student name ")
    found = False # this is a flag use if user giving input are found its ture other than its flase
    if not os.path.exists(FILE_NAME):# agra file nhi hogi to path run nhi karega 
        print("no record found")
        speak("no record found ")
        return
    with open(FILE_NAME,"r") as files:
        for line in files:# loop use to print all inputs line by line 
            name,roll_no,course,marks = line.strip().split(",")
            if name.lower == search_name: # user name are matching with the recorde name so they print all things 
                print("\n student record found")
                print(f"name {name}")
                print(f"roll_no{roll_no}")
                print(f"course{course}")
                print(f"marks{marks}")
                found = True
                break
    if not found:
        print("student not founded")
        speak("student not founded ")

#--------------------------------- delet fuction ----------------------------------------
def deleted_student():
    deleted_name = input("enter student name")
    updated_line = []
    deleted = False

    if not os.path.exists(FILE_NAME):
        print("record was not found ")
        speak("record was not found ")
        return
    
    with open(FILE_NAME,"r") as files:
        lines = files.readlines()
    
    for line in lines:
        name,_,_,_ = line.strip().split(",")
        if name != deleted_name:
            updated_line.append(line)
        else:
            deleted = True
    with open(FILE_NAME,"w") as files:
        files.writelines(updated_line)
    if deleted:
        print("student deleted succesfully")
        speak("student deleted succesfully")
    else:
        print("no student found")
        speak("no student found ")

#------------------------------ main fuction ------------------------------------------
def main():
    speak("welcome to student management system")

    while True:
        print("==========\student management system")
        print("1.add student")
        speak("1 add student")
        print("2.view student")
        speak("2.view student")
        print("3.search student")
        speak("3.search student")
        print("4.delete student")
        speak("delete student")
        print("5.exit")
        speak("5.exit")


        choice = input("enter your choice:")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            deleted_student()
        elif choice == '5':
            print("exit sucessfully")
            speak("exit sucessfully")
            break
        else:
            print("invalid choice")
            speak("invalid choice")

main()








