class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores=scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum=0
        for i in scores:
            sum=sum+int(i)
        a=sum/len(scores)
        if a < 40:
            grade = 'T'
        elif a < 55:
            grade = 'D'
        elif a < 70:
            grade = 'P'
        elif a < 80:
            grade = 'A'
        elif a < 90:
            grade = 'E'
        elif a <= 100:
            grade = 'O'
        return(grade)
    
line = input().split()