class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name

    def setAdd(self, updateAdd):
        self.__address = updateAdd
    def getAdd(self):
        return self.__address

    def __str__(self):
        return ("Name: {} \nAddress: {}".format(self.getName(), self.getAdd()))

# subclass for student and personal detail
class Student(Person):
    # courses is a dict datatype with grades as its values and subjects as the keys.
    # i didn't assign an empty dict to self.__courses because i wanted the dict to already have
    # existing data.
    # accepts name, address, and courses as parameter. 
    def __init__(self, courses, name, address):
        super().__init__(name, address)
        self.__numCourses = len(courses) # not 0 because there is already data in the dict. if there is no data, then len = 0.
        self.__courses = courses
    
    # adds the grade of the subject (new or prexisting).
    def addCourseGrade(self, course, grade):
        self.__courses[course] = int(grade)
        self.__numCourses +=1 
    
    # prints the dict containing the grades and subjects.
    def printGrades(self):
        print(self.__courses)

    # function to find average grade
    def getAverageGrade(self):
        # i declared a starting value
        totalGrade = 0
        # using loop, for each value in the dict, it adds to the starting value for the total grade
        for grade in self.__courses.values():
            totalGrade += grade
        # average grade formula, dividing the total grade by the length of the dict
        avgGrade = totalGrade / len(self.__courses)
        print(f"The average grade is {avgGrade}")

# subclass for teacher and personal data
class Teacher(Person):
    # takes name (as list in this case), address, and courses as parameter
    def __init__(self, courses, name, address):
        super().__init__(name, address)
        self.__numCourses = len(courses) # not 0 because there is already data in the dict
        self.__courses = courses
        
    #adds course using validation to ensure that it does not duplicate if the course exists
    # accepts self and newCourse as the desired course name to be added
    def addCourses(self, newCourse):
        if newCourse not in self.__courses:
            self.__courses.append(newCourse)
            # adds 1 to the number of courses
            self.__numCourses += 1
            return 1
        else:
            print("Cannot duplicate course")
            # boolean
            return False

    # same logic as the function above, removes desired course using validation to check if course exists
    # delCourse here is the course that needs to be removed
    def removeCourses(self, delCourse):
        if delCourse in self.__courses:
            self.__courses.remove(delCourse)
            # subtracts one from the number of courses
            self.__numCourses -=1
            return 1
        else:
            print("Course does not exist")
            # boolean
            return False
     
    def printCourses(self):
        print(self.__courses)

def main():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    typeOfPerson = int(input("To continue, enter 0 for student and 1 for teacher: "))
    if typeOfPerson == 0:
        coursesStud = {"maths": 67, "art": 0} # adding preexisting data to show how function can modify them. otherwise, i'd set an empty dict.
        studDetails = Student(coursesStud, name, address)
        while True:
            numNewCourse = int(input("Enter number of courses to add: "))
            if numNewCourse < 1:
                print("Number of must be greater than 0.")
                numNewCourse = int(input("Re-enter number of courses to add: "))
            else:
                break
        for eachNewCourse in range(numNewCourse):
            course = input("Enter new course, or course you'd like to update: ")
            grade = float(input("Enter current course grade: "))
            coursesStud.update(dict(course=grade))
            studDetails.addCourseGrade(course, grade)
        studDetails.printGrades()
        studDetails.getAverageGrade()
    else:
        coursesTeach = ["maths", "science"] # same logic as comment before, i'd declare an empty list.
        teachDetails = Teacher(coursesTeach, name, address)
        while True:
            numNewCourse = int(input("Enter number of courses to add, 0 to skip: "))
            if numNewCourse < 0:
                print("Number of must be greater than or equal to 0.")
                numNewCourse = int(input("Re-enter number of courses to add: "))
            elif numNewCourse == 0:
                break
            else:
                break
        for eachNewCourse in range(numNewCourse):
            newCourse = input("Enter new course: ")
            # coursesTeach.append(newCourse)
            teachDetails.addCourses(newCourse)
        while True:
            numNewCourse = int(input("Enter number of courses to remove, 0 to skip: "))
            if numNewCourse < 0:
                print("Number of must be greater than or equal to 0.")
                numNewCourse = int(input("Re-enter number of courses to remove: "))
            elif numNewCourse == 0:
                break
            else:
                break
        for eachNewCourse in range(numNewCourse):
            delCourse = input("Enter course to remove: ")
            teachDetails.removeCourses(delCourse)
        teachDetails.printCourses()      

if __name__ == '__main__':
    main()