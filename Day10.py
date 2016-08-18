"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	-Aug-2016

About Script:
		Write some thing about script here.
"""
import sys

def factorial(N):
        if N == 1:
                return 1
        return N*factorial(N-1)

def main():
        try:
                num = int(input("Enter a number: "))
                print("Factorial of ",num,"is",factorial(num))
        except:
                print("Unhandled Exception : ",sys.exc_info())
        return 

if __name__ == '__main__':
        main()
        input("Press any button to exit.")
