#Merge the Tools! HackerRank
#Give a string with n letters and a number k represents the length of substring
#Substring only contain each letter once
#Ex: AABCAAADA, n=3 => output: "AB" "CA "AD"

def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        sub_str = string[i:i+k]         # take a substring with the length k
        check_str = set()               # create empty sequence
        for letter in sub_str: 	
            if letter not in check_str: #check with checked string if letter isn't dubplicated 
                print(i,end="")
                check_str.add(letter)   #add accepted letter to check string
        #prints a new line
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
