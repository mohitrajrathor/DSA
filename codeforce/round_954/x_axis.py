# codeforce round 954 problem 01: X Axis 
def f(x1, x2, x3):
    """function to get a such that |x1 - a| + |x2 - a| + |x3 - a| should be minimum."""
    ...


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        arr = [int(i) for i in input().split()]
        print(f(*arr)) 

