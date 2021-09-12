#   Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = [1, -1][x < 0]
    rst = sign * int(str(abs(x)[::-1]))
    return rst if -(2**31) -1 <rst < 2** 31 else 0