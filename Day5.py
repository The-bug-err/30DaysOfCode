"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	13-Aug-2016

About Script:
		Write some thing about script here.
		https://www.hackerrank.com/challenges/30-class-vs-instance
"""

class Person:
        def __init__(self, initialAge):
                if initialAge >= 0:
                        self.age = initialAge
                else:
                        print("Age is not valid, setting age to 0.")
                        self.age = 0

        def amIOld(self):
                if self.age < 13:
                        print("You are young.")
                elif self.age >= 13 and self.age < 18:
                        print("You are a teenager.")
                else:
                        print("You are old.")

        def yearPasses(self):
                self.age += 1

                
def main():
        for T in range(int(input("Test cases : "))):
                age = int(input("Enter age for case "+ str(T+1)+" : "))
                p = Person(age)
                p.amIOld()
                for j in range(3):
                        p.yearPasses()
                p.amIOld()

if __name__ == '__main__':
	main()
	input("Press any button to exit.")
