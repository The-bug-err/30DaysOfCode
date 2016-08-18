"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	18-Aug-2016

About Script:
		Write some thing about script here.
		https://www.hackerrank.com/challenges/30-dictionaries-and-maps
"""
import sys

def main():
        try:
                T = int(input("Enter the number of dictionary items : "))
                phoneBook = {}
                for _ in range(T):
                    key, value = input().split()
                    phoneBook[key] = value
                for _ in range(T):
                    key = input()
                    value = phoneBook.get(key,"Not found")
                    if value == "Not found":
                        print(value)
                    else:
                        print(key+"="+value)
        except:
                print("Unhandled Exception : ",sys.exc_info())
        return 

if __name__ == '__main__':
        main()
        input("Press any button to exit.")
