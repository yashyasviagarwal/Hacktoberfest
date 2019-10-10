# This is my favorite code snippet because it has a real word example and involves critical thinking, and it has a tricky solution.

"""
Question:
Given a keypad with following configuration (0-empty,1-empty,2-('a','b','c'),3-('d','e','f'),4-('g','h','i'),5-('j','k','l'),6-('m','n','o'),7-('p','q','r','s'),8-('t','u','v'),9-('w','x','y','z'),
and an N digit number. List all words which are possible by pressing these numbers.
Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line of each test case is N, N is the number of digits. The second line of each test case contains D[i], N number of digits.

Output:
Print all possible words from phone digits with single space in lower case.

Constraints:
1 <= T <= 10
1 <= N <= 10
2 <=  D[i] <= 9

Example:
Input:
1
3
2 3 4

Output:
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi

Source: https://www.geeksforgeeks.org/find-possible-words-phone-digits/
Companies that have asked these:Accolite, Amazon, Flipkart, Samsung, Snapdeal, Zoho.

Solution:The solution that I have implemented is using recursion, and the time complexity of the same is O(4^n). 
"""
#keypad list with tuples of existing letters
phone_pad=[(),(),('a','b','c'),('d','e','f'),('g','h','i'),('j','k','l'),('m','n','o'),('p','q','r','s'),('t','u','v'),('w','x','y','z')]
#recursive function to generate all possible combinations.
def word_generator(a,s):
    #if array a is empty print the combination s and return
    if(len(a)==0):
        print(s,end=" ")
        return
    #loop through all options available for a specific digit.
    for i in digit_pad[a[0]]:
        #select one and recursively call the function with reduced array size.
        word_generator(a[1:],s+i)
           
#code to loop through all testcases and call the word_generator function
for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    #call the function with the initial array and empty string
    word_generator(a,"")
    print()
