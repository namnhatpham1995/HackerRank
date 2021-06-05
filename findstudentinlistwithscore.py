#Nested Lists HackerRank
#The first line contains an integer, N, the number of students.
#The 2N subsequent lines describe each student over 2 lines;
#the first line contains a student's name, and the second line contains their grade.

if __name__ == '__main__':
    score_list = []; # do not forget to declare a list
    for _ in range(int(input())):
            name = input()
            score = float(input()) 
            score_list.append([name, score])
    #Use set() to remove duplicate scores
    #sort scores increasing and take the second lowest position with sorted()[1]        
    second_highest = sorted(set([score for name, score in score_list]))[1]
    #Print the list if score match 
    print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
