# astar.py
import heapq
from state import State, find_zero
from heuristic import heuristic

def generate_next_states(state):
    zero_i, zero_j = find_zero(state.board)
    directions = [('UP', -1,0),('DOWN',1,0),('LEFT',0,-1),('RIGHT',0,1)]
    next_states=[]
    for move, di, dj in directions:
        ni,nj = zero_i+di, zero_j+dj
        if 0<=ni<3 and 0<=nj<3:
            nb = [row[:] for row in state.board]
            nb[zero_i][zero_j], nb[ni][nj] = nb[ni][nj], nb[zero_i][zero_j]
            next_states.append(State(nb,state,move))
    return next_states

def astar(start_board, goal_board):
    start = State(start_board)
    q = [(heuristic(start_board, goal_board), 0, id(start), start)]
    visited = set()
    g_values={str(start_board):0}

    while q:
        _, g_cost, _, cur = heapq.heappop(q)
        if cur.board == goal_board:
            path=[]
            while cur.parent:
                path.append(cur.move)
                cur = cur.parent
            return path[::-1]
        visited.add(str(cur.board))
        for next_state in generate_next_states(cur):
            nb_str = str(next_state.board)
            if nb_str in visited: continue
            ng = cur.g+1
            if nb_str in g_values and ng>=g_values[nb_str]: continue
            g_values[nb_str]=ng
            f = ng + heuristic(next_state.board, goal_board)
            heapq.heappush(q,(f, ng, id(next_state), next_state))
    return None
