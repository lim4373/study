def boards(board, visited, x, y, number):
	if x < 0 or x>= n or y<0 or y>= n or visited[x][y] or board[x][y] != number:
		return 0
	
	visited[x][y] = True
	
	size = 1
	size +=boards(board,visited, x+1,y, number)
	size +=boards(board,visited, x-1,y, number)
	size +=boards(board,visited, x,y+1, number)
	size +=boards(board,visited, x,y-1, number)
	
	return size

def find(n, board):
    large = [0] * 10
    
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                visited = [[False] * n for _ in range(n)]
                size = boards(board, visited, i, j, board[i][j])
                large[board[i][j] - 1] = max(large[board[i][j] - 1], size)
                
    return large

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = find(n, board)
print(*result)




