"""
Usage :	Just copy paste the content of the script in the iPython interperter,
		or just call the script. The scripts written are only for
		study purpose.

Author:	Vivek Rana

Date:	14-Aug-2016

About Script:
		Write some thing about script here.
		https://www.hackerrank.com/challenges/30-loops
"""

def main():
        N = int(input("Enter an integer : "))
        print("Table of ",N," to 10 : ")
        for i in range(1,11):
                print(N,"x",i,"=",N*i) 

if __name__ == '__main__':
	main()
	input("Press any button to exit.")
