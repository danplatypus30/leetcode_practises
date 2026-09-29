class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        # this is just fibonacci sequence
        # basic recursion will exceed time limit
        # use DP, iterative soln, O(n)
        fib = [0,1,2,3]
        for i in range(4, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]