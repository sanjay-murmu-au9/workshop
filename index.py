class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = 0
        reversed_x = self.helping(abs(x), reversed_x)
        if x <0:
            # placing neg(-) sign if input value is less than 0.
            reversed_x = - reversed_x
        if reversed_x > 2**31 or reversed_x < -(2**31):
            # returning if codition of integer storing fails.
            return 0
        return reversed_x
    
    def helping(self, x, reversed_x):
        # returning reversed integer
        while x != 0:
            li = x%10 # last_index
            x = x//10 # integer get after removing last integer
            reversed_x = reversed_x * 10 + li # storing last integer to in reversed format
        return reversed_x