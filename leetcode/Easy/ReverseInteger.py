class Solution(object)
    def reverse(self,x)
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            strInt = str(x)
            strInt = strInt[::-1]
            result = int(strInt)
            if result >2**31:
                result = 0
        else:
            strInt = str(abs(x))
            strInt = strInt[::-1]
            result = -int(strInt)
            if result <-2**31:
                result = 0
            
