class Solution:

    def searchMatrix(self,mat, x): 
    	
    	n = len(mat)
    	m = len(mat[0])
    	
    	for i in range(n):
    	    
    	    for j in range(m):
    	        
    	        if mat[i][j] == x:
    	            
    	            return True
    	
    	return False
    	
