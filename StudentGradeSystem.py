import pandas as pd

def showAllInfo():
    df = pd.read_csv("student_info.txt", sep=" ", names = ["Name","Surname","Student No","Grade"])
    print(df)

def showDataframe():
    df = pd.read_csv("grades_info.txt", sep=" ", names = ["Name","Surname","","Grade"," ","Status"])
    print(df)

def saveExcel():
    with open("grades_info.txt","r",encoding="utf-8") as file:
        data = pd.DataFrame(file)
        data.to_excel("excel_grades.xlsx")

def calcPass(fname,lname,grade):
    global gradesList
    with open("grades_info.txt","a",encoding="utf-8") as file:
        gradeS = ""
        if grade>=90 and grade<=100:
            gradeS = "AA"
            file.write(f"{fname} {lname} : {gradeS} - passed\n")
        elif grade>=85 and grade<=89:
            gradeS = "BA"
            file.write(f"{fname} {lname} : {gradeS} - passed\n")
        elif grade>=80 and grade<=84:
            gradeS = "BB"
            file.write(f"{fname} {lname} : {gradeS} - passed\n")
        elif grade>=75 and grade<=79:
            gradeS = "CB"
            file.write(f"{fname} {lname} : {gradeS} - passed\n")
        elif grade>=70 and grade<=74:
            gradeS = "CC"
            file.write(f"{fname} {lname} : {gradeS} - passed\n")
        elif grade>=65 and grade<=69:
            gradeS = "DC"
            file.write(f"{fname} {lname} : {gradeS} - passed\n")
        elif grade>=60 and grade<=64:
            gradeS = "DD"
            file.write(f"{fname} {lname} : {gradeS} - failed\n")
        elif grade>=50 and grade<=59:
            gradeS = "FD"
            file.write(f"{fname} {lname} : {gradeS} - failed\n")
        else:    
            gradeS = "FF"
            file.write(f"{fname} {lname} : {gradeS} - failed\n")

        

def calcGrade(visa,final):
    return float((visa*0.40) + (final*0.60))



def studentEntry():
    while True:
        firstName = input("Enter student's first name: ")
        if firstName.isdigit(): 
            print("Please enter only letters.") 
            continue
        lastName = input("Enter student's last name: ")
        if firstName.isdigit():
            print("Please enter only letters.")
            continue

        try:
            studentNo = int(input("Enter student's number: "))
            visaGrade = int(input("Enter student's visa grade: "))
            if not (visaGrade > -1 and visaGrade < 101):
                print("Please enter grade in range of 0-100.")
                continue
            finalGrade = int(input("Enter student's final grade: "))
            if not (finalGrade > -1 and finalGrade < 101):
                print("Please enter grade in range of 0-100.")
                continue
        except ValueError:
            print("Please enter numbers only.")
            continue
        grade = calcGrade(visaGrade,finalGrade)
        calcPass(firstName,lastName,grade)

        with open("student_info.txt","a",encoding="utf-8") as file:
            file.write(firstName + " " + lastName + " " + str(studentNo) + " " + str(grade)+"\n")
            break


while True:
    choice = input("""1 - Add new student\n2 - Show all student's info \n3 - Show dataframe of students who has passed and failed
4 - Create excel file\n5 - Exit\n""")

    if int(choice) == 1:
        studentEntry()
    if int(choice) == 2:
        showAllInfo()
    if int(choice) == 3:
        showDataframe()
    if int(choice) == 4:
        saveExcel()
    if int(choice) == 5:
        print("Closing system.")
        break