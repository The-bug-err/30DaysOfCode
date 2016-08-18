"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	16-Aug-2016

About Script:
		Write some thing about script here.
		https://www.hackerrank.com/challenges/30-review-loop
"""
import sys

def main():
        for T in range(int(input("Test cases: "))):
                text = input("String "+str(T+1)+":")
                even = []
                odd = []
                size = len(text)
                for i in range(size):
                        if i%2 == 0:
                                even.append(text[i])
                        else:
                                odd.append(text[i])
                evenText = "".join(even)
                oddText = "".join(odd)
                print(evenText+" "+oddText)
        return 

if __name__ == '__main__':
        try:
                main()
        except:
                print("Unhandled exception :",sys.exc_info())
        input("Press any button to exit.")
