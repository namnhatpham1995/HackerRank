#Given the participants' score sheet for your University Sports Day,
#you are required to find the runner-up score. You are given  scores.
#Store them in a list and find the score of the runner-up.
# in put n=5, arr= 2 3 6 6 5 => output 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
    #set() method is used to convert any of the iterable to sequence of iterable elements with "distinct elements"
    #sorted()[-2] => sorted increasing and take the runner-up position
