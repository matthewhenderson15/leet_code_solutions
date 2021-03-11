class Solution:
    def climbStairs(self, n: int) -> int:
        # I noticed the number of distinct ways to climb to the top was a Fibonacci sequence.
        # My solution is a bottom-up solution.
        
        # Base case: if n = 1, then there is only one step to take
        if n == 1:
            return 1
        
        # Otherwise initialize variables for n >= 2
        a = 1
        b = 1
        
        # Loop through values up till number given 
        # Use temp to store new Fib number
        # Increment variables each time for next iteration of loop
        for i in range(1,n):
            temp = a + b
            a = b
            b = temp
        
        # Return last temp variable, or Fibonacci number at n
        return b
        
        # Since each computation at each iteration is done one time and has a time complexity of O(n), 
        # the overall time complexity is O(n)