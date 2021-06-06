# List Comprehensions HackRank
# Input 3 integers x,y,z of cuboid dimensions and a integer n
# Print all possible coordinates (i,j,k) where
# 0 <= i <= x; 0 <= j <= y; 0 <= k <= z and i+j+k != n

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #Solve
    arr = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    #Output
    print(arr)
