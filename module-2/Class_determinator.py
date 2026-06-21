# Student class
class Student:
    #create class with first and last name and total grade points
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_credits = 0
        self.total_grade_points = 0
        
    #add course credits & grade points
    def add_course(self, credits, grade):
        self.total_credits += credits
        self.total_grade_points += credits * grade
        
    #calculate GPA, prevent division by 0
    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0
        return self.total_grade_points / self.total_credits

    #determine student year
    def determine_year(self):
        if self.total_credits <= 33:
            return "First Year"
        elif self.total_credits <= 66:
            return "Second Year"
        elif self.total_credits <= 96:
            return "Third Year"
        elif self.total_credits < 130:
            return "Fourth Year"
        else:
            return "Multi-year"

#inheritance from student class
class DeclaredStudent (Student):
    def __init__(self, first_name, last_name, concentration):
        super().__init__(first_name, last_name)

        if concentration == "":
            self.concentration = "NA"
        else:
            self.concentration = concentration

def main():
    #prompt user for information
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    concentration = input("Enter student's concentration, press enter in undeclared: ")

    student = DeclaredStudent(first_name, last_name, concentration)

    #create loop
    keep_going = "Yes"
    while keep_going.lower() == "yes":
        credits = float(input("Enter course credits: "))
        grade = float(input("Enter grade points for the course: "))

        student.add_course(credits, grade)

        keep_going = input("Do you want to enter another course? Yes/No: ")

    #display student info
    print()
    print("Student Information")
    print("-------------------")
    print("Name: ", student.first_name, student.last_name)
    print("Concetration: ", student.concentration)
    print("Total Credits: ", student.total_credits)
    print("Cumulative GPA: ", round(student.calculate_gpa(), 2))
    print("Student Year: ", student.determine_year())

main()
