Year 1 - Semester 2
Date: 26th April 2019

Project Specification:

Data relating to employees are kept in a file called employees.txt.
The business stores data about each employee consisting of
• A five-digit employee number
• First name
• Surname
• Email
• Salary

A snippet of the file might be:
12345
Minnie
Mouse
minnie.mouse@cit.ie
67589.54
23456
Bugs
Bunny
bugs.bunny@cit.ie
67589.54
67581
Wiley
Coyote
wiley.coyote@cit.ie
34234.56

or

12345,Minnie,Mouse,minnie.mouse@cit.ie,67589.54
23456,Bugs,Bunny,bugs.bunny@cit.ie,67589.54
67581,Wiley,Coyote,wiley.coyote@cit.ie,34234.56

Develop an application that allows the user to choose from one of the following options, until they
choose to quit.
1. View all employees
2. View a particular employee
3. Edit the salary of an employee
4. Add a new employee
5. Delete an employee
6. Give a bonus to each employee, writing the details to a file
7. Generate a report for management
8. Quit

Details:

1. Display the details of all employees.
2. Search for an employee by employee number and display the record.
3. Search for an employee by employee number and edit the associated salary.
4. Add a new employee. Ask the user for the first name, surname and salary. The application
should generate a unique email and a five digit employee number that has not already been
assigned to an employee.
5. Search for an employee by employee number and delete that employee
6. Ask the user for the (percentage) value of the end-of-year bonus and create a file into which
you write the employees' names, employee numbers and the value of the bonus each
employee receives. For example if the bonus is 1% then Minnie Mouse receives a bonus of
€675.90.
7. Generate a report that includes
a. The average salary earned
b. The largest salary earned and the name(s) of those who earn it.
8. The application finishes and all data is backed up to employees.txt
