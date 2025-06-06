#You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

#User function Template for Python

class Solution:
	def pushZerosToEnd(self,arr):
    	index = 0
    	
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        arr[index] = arr[i]
    	        index += 1
    	        
    	while index < len(arr):
    	    arr[index] = 0
    	    index += 1
