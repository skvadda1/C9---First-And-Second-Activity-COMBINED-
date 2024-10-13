class student:
    grade = 9
    name = "Sathvik"
    print("Hello my name is Sathvik, I study in grade" , grade)

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is" , self.name)
        print("I study in grade" ,self.grade)

ob = student()
ob.introduction()
ob.details()