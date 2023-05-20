class Solution:
	def is_palindrome(self, n):
		# Code here
		n=str(n)
		left = 0
		right = len(n)-1
		output = 'Yes'
		while(left<=right):
		    if n[left] == n[right]:
		        left +=1
		        right-=1
		    else:
		        output='No'
		        return output
		    
		return output
            
