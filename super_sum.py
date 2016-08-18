def super_sum(numbers_to_sum):
	'''
	Function to return the sum of numbers in a list including numbers contained in a list withi a list
	'''
	sum_counter= 0
	#checks if the list passed is an empty list
	if numbers_to_sum == []:
		return None
	
	#iterating through the elements of the list. Includes action to be done if the loop encounters a list element which is also a list
	for numbers in numbers_to_sum:
		if type(numbers)== str:
			return 0
		elif type(numbers)== list:
			for nums in numbers:
				sum_counter+=nums
				

		#adding the elements to the variable sum_counter where list elements are numbers only. 
		else:
			sum_counter+=numbers
	
	return sum_counter		
		
print (super_sum([]))

