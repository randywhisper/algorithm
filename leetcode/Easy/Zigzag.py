class Solution(object):
    def convert(self,s,numRows):
        if len(s) == 0 or numRows == 1:
            return s
        else:
            listTotal = []
            toward = "down"
            i = 0
            for a in numRows-1:
                listTotal.append([])
            for char in s:
                listTotal[i].append(char)
                if i == numRows-1:
                    toward = "up"
                elif i == 0:
                    toward = "down"
                if toward == "down":
                    i+=1
                else:
                    i-=1


def main():
    solu  = Solution()
    m = solu.convert("PAYPALISHIRING",3)
    print m
    
if __name__ == "__main__":
    main()
         

        
