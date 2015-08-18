class Solution:
	def twoSum(self,num,target):
		mid = target / 2.0
		hashTable = {}
		tuple = ()
		for index,item in enumerate(num):
			if hashTable.has_key(abs(mid-item)) == False:
				hashTable[abs(mid-item)] = [item,index]
			else:
				if item == hashTable[abs(mid-item)][0]:
					if item+hashTable[abs(mid-item)][0] == target:
						tuple = (hashTable[abs(mid-item)],index)
				else:
					tuple = (hashTable[abs(mid-item)],index)
		print(tuple)
		return tuple



def main():

	solut = Solution()
	solut.twoSum({2,3,4,8,9},10)

if __name__ == "__main__":
	main()



