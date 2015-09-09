class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self,a,b):
        lenA = len(a)
        lenB = len(b)
        sum = int(a[(lenA-1):]) + int(b[(lenB-1)])
        if sum == 2
