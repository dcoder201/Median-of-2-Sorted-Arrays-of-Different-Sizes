#User function Template for python3
import numpy as np
class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            final=arr1+arr2
            ans=np.median(final)
            if '.0' in str(ans):
                return(int(ans))
            else:
                return(ans)
