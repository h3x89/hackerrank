# https://www.hackerrank.com/challenges/30-class-vs-instance/problem?isFullScreen=true

class Person:
    test_case_counter = 0
    total_test_cases = 0

    def __init__(self, initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
        
        # Sprawdzenie, czy to nie jest ostatni przypadek
        Person.test_case_counter += 1
        if Person.test_case_counter < Person.total_test_cases:
            print("")

    def yearPasses(self):
        self.age += 1
        
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")