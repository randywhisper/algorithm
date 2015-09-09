class listNode:
	def __init__(self,x):
		self.val  = x
		self.next = None
class Solution:
    def addTwoNumbers(self,l1,l2):
        sum  = l1.val+l2.val
        if sum <10:
            tem = listNode(sum)
        else:
            sum = sum%10
            tem = listNode(sum)
            if l1.next :
                l1.next.val+= 1
            elif l2.next:
                l2.next.val+=1
            else:
                l1.next = listNode(1)
        if not(l1.next is None and l2.next is None):
            if l1.next is None:
                l1.next = listNode(0)
            elif l2.next is None:
                l2.next = listNode(0)
            tem.next = self.addTwoNumbers(l1.next,l2.next)
        return tem

def main():
    solu = Solution()
    a = listNode(1)
    b = listNode(9)
    b.next = listNode(9)
    b.next.next  = listNode(9)
    m = solu.addTwoNumbers(a,b)
    print(m.val)
    print(m.next.val)
    print(m.next.next.val)
    print(m.next.next.next.val)


if __name__ == "__main__":
    main()

