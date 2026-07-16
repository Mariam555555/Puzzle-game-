# test.py
def test():
    import time
    from astar import astar

    goal = [[1,2,3],[4,5,6],[7,8,0]]
    tests = [([[1,2,3],[4,0,6],[7,5,8]],"Easy"),
             ([[1,0,3],[4,2,5],[7,8,6]],"Medium"),
             ([[0,1,3],[4,2,5],[7,8,6]],"Hard")]

    for b,n in tests:
        t0 = time.time()
        s = astar(b, goal)
        print(f"{n}: {len(s) if s else 'No solution'} moves, {round(time.time()-t0,3)}s")

# لتشغيل test.py لوحده
if __name__=="__main__":
    test()
