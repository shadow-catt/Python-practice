steps = 0
def hanoi(a, b, c, n):
    global steps
    if n == 1:
        steps+=1
        print("[STEP{:>4}] {}->{}".format(steps, a, c))
    else:
        hanoi(a, c, b, n-1)
        hanoi(a, b, c, 1)
        hanoi(b, a, c, n-1)
N = eval(input())
hanoi("A", "B", "C", N)
