# printing fibonacci using memoization technique
# time complexity O(n)


def allfib(n):
    memo = [0]*(n+1)
    for i in range (n):
        print (fib(i,memo), sep = "\n")

        
def fib(i,memo):
    if i <=0:
        return 0
    elif i == 1:
        return 1
    elif (memo[i] > 0):
        return memo[i]
    else:
        memo[i] = fib(i-1,memo) + fib(i-2,memo)
        return memo[i]


allfib(8) 