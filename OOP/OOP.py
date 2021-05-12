from abc import ABC,abstractclassmethod

class Course():
    def __init__(self,courseName,courseCode,instructor,offeringSchool,capacity):
        self.__courseName=courseName
        self.__courseCode=courseCode
        self.__offeringSchool=offeringSchool
        self.__capacity=capacity
        self.__instructor=instructor
        self.__students={}
        self.__resources=[]
        self.__assignments=[]
        self.__roster=[student for student in self.__students].append(self.__instructor)
    
    def addResource(self,resource_title,resource_content):
        self.__resources.append({
            "title": resource_title,
            "content": resource_content,
        })
    
    def addAssignment(self,assignment_title,assignment_content,assignment_deadline):
        self.__assignments.append({
            "title": assignment_title,
            "content": assignment_content,
            "deadline": assignment_deadline
        })
    
    def addMarks(self,assignment_title,student,marks):
        self.__students[student][assignment_title]=marks

    def viewAllMarks(self):
        for student in self.__students:
            print(self.__students[student])
    
    def viewStudentMarks(self,student):
        print(self.__students[student])

    def viewAllResources(self):
        for resource in self.__resources:
            print(resource)

    def viewAllAssignments(self):
        for assignment in self.__assignments:
            print(assignment)

    def viewRoster(self):
        for person in self.__roster:
            print(person)

    def printDetail(self):
        print(f"The course {self.__courseName} ({self.__courseCode}) is taught in {self.__offeringSchool} and is offered by {self.__instructor}. The course has currently the capacity of {self.__capacity}")
    
class User(ABC):
    @abstractclassmethod
    def getProfile(self):
        print("This is just a basic user!")
        # print(f"First Name : {self.first_name}")
        # print(f"Last Name : {self.last_name}")
        # print(f"User Name : {self.user_name}")

class Student(User):
    
    def __init__(self,first_name,last_name,user_name,password,roll_no,status):
        # super().__init__(first_name,last_name,user_name,password)
        self.__first_name=first_name
        self.__last_name=last_name
        self.__user_name=user_name
        self.__password=password
        self.__roll_no=roll_no
        self.__status=status
        self.__courses={}
    
    def signIn(self,user_name,password):
        if(self.__user_name == user_name and password==self.__password):
            print(f"Signed in as {self.__user_name}, Welcome {self.__first_name} {self.__last_name}")

    def signOut(self):
        print(f"Gracefully signed out !")

    def getProfile(self):
        print(f"{self.__first_name} {self.__first_name}, roll number {self.__roll_no},  is a {self.__status} at LUMS")

    def viewAssignments(self,course):
        self.__courses[course].viewAllAssignments()

    def viewResources(self,course):
        self.__courses[course].viewAllResources()

    def viewRoster(self,course):
        self.__courses[course].viewRoster()

    def viewMarks(self,course):
        self.__courses[course].viewStudentMarks(f"{self.__first_name} {self.__last_name}")

class Instructor(User):
    def __init__(self,first_name,last_name,user_name,password,designation,qualification):
        # super().__init__(first_name,last_name,user_name,password)
        self.__first_name=first_name
        self.__last_name=last_name
        self.__user_name=user_name
        self.__password=password
        self.__designation=designation
        self.__qualification=qualification
        self.__courses={}
    
    def signIn(self,user_name,password):
        if(self.__user_name == user_name and password==self.__password):
            print(f"Signed in as {self.__user_name}, Welcome {self.__first_name} {self.__last_name}")

    def signOut(self):
        print(f"Gracefully signed out !")

    def getProfile(self):
        print(f"{self.__first_name} {self.__last_name} is a {self.__designation} at LUMS and has {self.__qualification}")

    def addResource(self,course,resource_title,resource_content):
        self.__courses[course].addResource(resource_title,resource_content)

    def addAssignment(self,course,assignment_title,assignment_content,assignment_deadline):
        self.__courses[course].addAssignment(assignment_title,assignment_content,assignment_deadline)

    def addMarks(self,course,assignment_title,student,marks):
        self.__courses[course].addMarks(assignment_title,student,marks)

    def viewResources(self,course):
        self.__courses[course].viewAllResources()

    def viewAssignment(self,course):
        self.__courses[course].viewAllAssignments()

    def viewMarks(self,course):
        self.__course[course].viewAllMarks()
    
    def viewRoster(self,course):
        self.__courses[course].viewRoster()
