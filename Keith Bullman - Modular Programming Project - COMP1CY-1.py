# Author: Keith Bullman
# Class: COMP1C-Y
# Project: Modular Programming 2019 (Year 1 Semester 2)

# Importing Random for Generating Random ID and Email (if required)
import random

def options():
    # Get Users Choice
    while True:
        try:
            choice = int(input("Enter Choice (1-8)\n"
                               "1: View All Employees\n"
                               "2: View Particular Employee\n"
                               "3: Edit Salary of Employee\n"
                               "4: Add New Employee\n"
                               "5: Delete an Employee\n"
                               "6: Generate Report\n"
                               "7: Give Bonuses + Generate Bonus Report\n"
                               "8: Quit\n>>> "))
            if 1 <= choice <= 8:
                break
            else:
                print("Invalid option! Try again!\n")
        except ValueError:
            print("Invalid input! Try again!\n")
    return choice

def getAllData(filename):
    # Make 5 Item Lists
    employeeId = []
    firstName = []
    surName = []
    email = []
    salary = []
    # Open File
    file = open(filename)
    # Loop to Add Each Piece of Data to its Corresponding List (i.e Employee ID added to employeeId list)
    while True:
        line = file.readline()
        if line == "":
            break
        lineData = line.split(",")
        employeeId.append(lineData[0])
        firstName.append(lineData[1])
        surName.append(lineData[2])
        email.append(lineData[3])
        salary.append(float(lineData[4]))
    # Return Every Filled List
    return employeeId, firstName, surName, email, salary

def viewEmployees(employeeID, firstName, surName, email, salary):
    # View All Employee Information
    counter = 0
    print()
    print("Current Employees: ")
    while len(firstName) > counter:
        print("ID: ", *employeeID[counter], "\t",
              "\tName: ", *firstName[counter], " ", *surName[counter],
              "\t\tEmail: ", *email[counter],
              "\t\tSalary: €", salary[counter], sep="")
        counter += 1
    print()

def particularEmployee(id, firstName, surName, email, salary):
    # View Particular Employee Information
    print()
    print("Employees to Choose From:")
    counter = 0
    nameCounter = 1
    while len(firstName) > counter:
        print(nameCounter, ": ", *firstName[counter], " ", *surName[counter], sep="")
        counter += 1
        nameCounter += 1
    print()
    # User Choice for Particular Employee
    while True:
        try:
            choice = int(input("Pick Employee to View (1-{})>>> ".format(len(firstName))))
            if choice < 1:
                print("Please choose an Employee from 1-{}!".format(len(firstName)))
                continue
            print("ID: ", *id[choice - 1], "\n"
                  "First Name: ", *firstName[choice - 1], "\n",
                  "Surname: ", *surName[choice - 1], "\n"
                  "Email: ", *email[choice - 1], "\n"
                  "Salary: ", salary[choice - 1], sep="")
            if len(id) >= choice >= 0:
                break
        except (ValueError, IndexError):
            print("Invalid input; try again!\n")
    print()

def editSalary(firstName, surName, salary, filename):
    # Edit Employee Salary
    counter = 0
    nameCounter = 1
    print()
    print("Employees to Choose From:")
    while len(salary) > counter:
        print(nameCounter, ": \t", firstName[counter], " ", surName[counter], "\n\tCurrent Salary: ", salary[counter], "\n", sep="")
        counter += 1
        nameCounter += 1
    print()
    while True:
        try:
            # User Chooses Specific Employee
            while True:
                try:
                    choice = int(input("Choose Salary to Edit (1-{}): ".format(len(firstName))))
                    if len(firstName) < choice < 1:
                        print("Invalid input! Try again!\n")
                        continue
                    if len(firstName) >= choice > 0:
                        break
                except ValueError:
                    print("Invalid input! Try again!\n")
            # User Chooses Salary Change
            while True:
                try:
                    salaryChange = float(input("Change " + firstName[choice-1] + "'s Salary to: "))
                except(ValueError):
                    print("Invalid input! Try again!\n")
                else:
                    if salaryChange < 0:
                        print("Salary cannot be changed to a negative number!")
                    if salaryChange > 0:
                        break
            # Overwrite Chosen Salary Position with New Salary
            salary[choice-1] = salaryChange
            break
        except (ValueError, TypeError):
            print("Invalid input! Try again!\n")
    print()

def newEmployee(ID, Name, lastName, eMail, Salary):
    # Add New Employee
    # Randomly Generate ID for Employee
    employeeID = random.randint(10000, 99999)
    while employeeID in ID:
        employeeID = random.randint(10000, 99999)
    # Get First Name
    while True:
        try:
            firstName = input("First Name of New Employee >>> ")
            if len(firstName) >=3:
                surName = input("Surname of New Employee >>> ")
                if len(surName) >=3:
                    break
                else:
                    print("Name not long enough! Try again!\n")
            else:
                print("Name not long enough! Try again!\n")
        except ValueError:
            print("Name not long enough!")
    # Generate Email
    email = ("{}.{}@cit.ie".format(firstName.lower(), surName.lower()))
    # If Email ALREADY in Email List, generate random number at the end of it
    while email in eMail:
        email = ("{}.{}{}@cit.ie".format(firstName.lower(), surName.lower(), random.randint(1, 99)))
    # Get Salary
    while True:
        try:
            salary = float(input("Salary of {} {} >>> ".format(firstName, surName)))
        except ValueError:
            print("Invalid input! Try again!\n")
        else:
            if salary < 0:
                print("Cannot have negative salary!")
            if salary > 0:
                break
    # Add information to corresponding lists
    ID.append(employeeID)
    Name.append(firstName)
    lastName.append(surName)
    eMail.append(email)
    Salary.append(salary)
    print()

def deleteEmployee(employeeID, firstName, surName, email, salary):
    # Delete Employee
    counter = 0
    nameCounter = 1
    print()
    print("Choose Employee to Delete (1-{}):".format(len(firstName)))
    print()
    while len(firstName) > counter:
        print(nameCounter, ": \t", firstName[counter], " ", surName[counter], "\n", sep="")
        counter += 1
        nameCounter += 1
    # Get Users Delete Choice
    while True:
        try:
            choice = int(input("Delete Choice >>> "))
            if len(employeeID) >= choice >= 0:
                break
            else:
                print("Invalid input! Try again!\n")
        except (ValueError, TypeError):
            print("Invalid input! Try again!\n")
    # Remove (.pop) chosen information from corresponding lists
    employeeID.pop(choice-1)
    firstName.pop(choice-1)
    surName.pop(choice-1)
    email.pop(choice-1)
    salary.pop(choice-1)

def generateReport(firstName, surName, salary):
    # Generate Report
    # Get Overall Salary Sum
    totalSalary = sum(salary)
    # Get Amount of Salaries
    amountSalary = len(salary)
    # Calculate Average Salary
    avgSalary = totalSalary / amountSalary
    # Get Largest Salary
    highestSalary = max(salary)
    print()
    print("Average Salary: €{:.2f}".format(avgSalary))
    print("Highest Salary: €{:.2f}".format(highestSalary))
    # Get Name Associated with Largest Salary
    counter = 0
    highestNameList = []
    for counter in range(len(firstName)):
        if salary[counter] >= highestSalary:
            highestNameList.append(firstName[counter])
        counter += 1
    print("Highest Salary Name(s): ", end=""), print(*highestNameList, sep=", ", end=""), print("; with the largest salary of {:.2f}".format(highestSalary))
    print()

# Get Bonus Percentages for Each Employee From User + Write to Bonus File
def bonusInfo(id, firstName, surName, salary, filename):
    # Open Bonus File
    with open(filename, "w") as bonusInfo:
        counter = 0
        # Get Bonus for Each Employee, Format, and Write To Bonus File
        while len(id) > counter:
            try:
                bonus = float(input("Bonus (%) for {} {}: ".format(firstName[counter], surName[counter])))
                while bonus < 0:
                    print("You cannot give negative bonuses!")
                    bonus = float(input("Bonus (%) for {} {}: ".format(firstName[counter], surName[counter])))
                bonusPercentage = bonus / 100
                bonusTotal = salary[counter] * bonusPercentage
                print("ID: {}\t"
                      "Name: {} {}\t"
                      "Bonus: {:.2f}\t"
                      "Total Earnings: {:.2f}".format(id[counter], firstName[counter], surName[counter], bonusTotal, salary[counter] + bonusTotal), file=bonusInfo)
                counter += 1
            except ValueError:
                print("Invalid input! Try again!")
    print()

def goodbye(overwritten, concluded, farewell):
    # Print Termination
    print()
    print("/", "=" * 18, "\\")
    print("||", overwritten, "||")
    print("||", concluded, "||")
    print("||", " " * 3, farewell, " " * 3, "||")
    print("\\", "=" * 18, "/")

def main():
    while True:
        employeeID, firstName, surName, email, salary = getAllData("data.txt")
        choice = options()
        # View All Employees
        if choice == 1:
            viewEmployees(employeeID, firstName, surName, email, salary)
        # View Particular Employee
        elif choice == 2:
            particularEmployee(employeeID, firstName, surName, email, salary)
        # Edit Salary
        elif choice == 3:
            editSalary(firstName, surName, salary, "data.txt")
        # Add New Employee
        elif choice == 4:
            newEmployee(employeeID, firstName, surName, email, salary)
        # Delete Employee
        elif choice == 5:
            deleteEmployee(employeeID, firstName, surName, email, salary)
        # Generate Report
        elif choice == 6:
            generateReport(firstName, surName, salary)
        # Get Bonuses + Write to Bonus File
        elif choice == 7:
            bonusInfo(employeeID, firstName, surName, salary, "bonusInfo.txt")
        # Terminate Program
        elif choice == 8:
            goodbye("File Overwritten ", "Program Concluded", "Farewell!")
            break
        # Add code to write the 5 lists back to data.txt with commas between the data
        with open("data.txt", "w") as output:
            counter = 0
            while len(employeeID) > counter:
                print(employeeID[counter], firstName[counter], surName[counter], email[counter], salary[counter], sep=",", file=output)
                counter += 1

main()
