"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	18-Aug-2016

About Script:
		Write some thing about script here.
		https://www.hackerrank.com/challenges/30-arrays
"""

import sys

def main():
        try:
                N = int(input("Size of Array: "))
                print("Enter",N,"space seperated numbers: ")
                arr = input().split(' ')
                print("Reversed array is : ")
                for elem in arr[::-1]:
                        print(elem, end=" ")
        except:
                print("Unhandled exception : ",sys.exc_info())
        return

if __name__ == '__main__':
        main()
        input("Press any button to exit.")
