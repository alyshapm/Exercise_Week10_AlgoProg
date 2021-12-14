# not finished! some parts doesn't work but i will edit if given the permission
# if i were to improve, i'd allow user to input in the driver (and fix the entire thing in general) and more validation
# also add more comments but it is 12:25 as i am writing this *sobs*
class Person:
    def __init__(self, name="John", address="Jl. Hang Lekir I No.6"):
        self.__name = name
        self.__address = str(address)
    
    def setName(self, name):
        self.__name = name
    def setAdd(self, address):
        self.__address = address
    
    def getName(self):
        return self.__name
    def getAdd(self):
        return self.__address

    def __str__(self):
        return ("Name: {} \nAddress: {}".format(self.getName(), self.getAdd()))

class Student(Person):
    # courses is a dict data with grades as its value so i did not include a grade parameter
    def __init__(self, numCourses=0, courses={}, name="", address=""):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses
    
    # updates the grade (or value) for the art key
    def addCourseGrade(self, courses):
        gradeArt = 70
        courses["art"] = 70
        return courses
    
    # prints the dict because it has the grades for the corresponding subjects
    def printGrades(self, courses):
        print(courses)

    # function to find average grade
    def getAverageGrade(self, courses):
        # first, i declared a starting value
        totalGrade = 0
        # using loop, for each value in the dict, it adds to the starting value for the total grade
        for grade in courses.values():
            totalGrade += grade
        # avg grade formula, dividing the total grade by the length of the dict
        avgGrade = totalGrade / len(courses)
        print(avgGrade)

class Teacher(Person):
    def __init__(self, numCourses=0, courses=[], name="", address=""):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses
        
    #adds course using validation to ensure that it does not duplicate if the course exists
    def addCourses(self, courses):
        newCourse = "IT"
        if newCourse not in courses:
           courses.append(newCourse)
        else:
            print("Cannot duplicate course")

    def removeCourses(self, courses):
        delCourse = "science"
        if delCourse not in courses:
            print("Course does not exist")
        else:
            courses.remove(delCourse)

def main():
    personalDetails = Person()
    print(personalDetails.__str__())

    coursesStud = {"maths": 67, "art": 0}
    sdetails = Student()
    sdetails.addCourseGrade(courses=coursesStud)
    sdetails.getAverageGrade(courses=coursesStud)

    coursesTeach = ["maths", "science"]
    tdetails = Teacher()
    tdetails.addCourses(courses=coursesTeach)
    tdetails.removeCourses(courses=coursesTeach)


if __name__ == '__main__':
    main()
    

