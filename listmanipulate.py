#Input N number of commands
#Input command text and/or a number to do with list
#There are 7 types of command: insert, print, remove, append, sort, pop, reverse

if __name__ == '__main__':
    N = int(input())
    Output = [];            # make an empty list to contain numbers
    for i in range(0,N):
        command = input().split();   # Take input and split it into a list
        if command[0] == "print":    # Check position 0 for the command text
            print(Output)
            #print the Output list
        elif command[0] == "insert":
            Output.insert(int(command[1]),int(command[2]))
            #insert number in command[1] to Output at position in command[2]
        elif command[0] == "remove":
            Output.remove(int(command[1]))
            #remove number in command[1] from Output list
        elif command[0] == "pop":
            Output.pop();
            #pop the last element from current Output list
        elif command[0] == "append":
            Output.append(int(command[1]))
            #add element to Output
        elif command[0] == "sort":
            Output.sort();
            #sort the current Output list
        else:
            Output.reverse();
            #reverse the current output list
