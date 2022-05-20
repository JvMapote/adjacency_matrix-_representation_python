def manual():
 # here created adjacency matrix manually
 arr = [[0 for i in range(5)] for j in range(5)]
 arr[0][1] = arr[1][0] = 2
 arr[0][2] = arr[2][0] = 3
 arr[1][2] = arr[1][2] = 15
 arr[1][3] = arr[1][3] = 2
 arr[2][4] = arr[4][2] = 13
 arr[3][4] = arr[4][2] = 9
 return arr
def userInput():
 # get user input to create adjacency matrxi
 arr = [[0 for i in range(5)] for j in range(5)]
 edges = int(input("Enter no. of edges: "))
 for i in range(edges):
  a,b,w = map(int,input().split())
  arr[a][b] = arr[b][a] = w
 return arr

userInput()