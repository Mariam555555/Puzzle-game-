# heuristic.py
def manhattan_distance(board, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            distance += abs(i-x) + abs(j-y)
                            break
    return distance

def misplaced_tiles(board, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] !=0 and board[i][j] != goal[i][j]:
                count +=1
    return count

def heuristic(board, goal, method='manhattan'):
    if method=='manhattan':
        return manhattan_distance(board, goal)
    else:
        return misplaced_tiles(board, goal)
