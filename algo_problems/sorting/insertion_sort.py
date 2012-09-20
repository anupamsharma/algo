#/usr/local/bin/python
import random

def get_random_float_array(number, min, max):
	random_array = []
	for count in range(1, number+1):
		random_array.append(random.uniform(min, max))

	return random_array


def get_random_int_array(number, min, max):
	random_array = []
	for count in range(1, number+1):
		random_array.append(int(random.uniform(min, max)))

	return random_array

class sorter(object):
	def __init__(self):
		pass

	def sort(self):
		raise NotImplementedError(" sort function ")

class insertionSorter(sorter):
	def sort(self, a):
		outer = 1
		while(outer < len(a)):
			key = a[outer]
			inner = outer - 1
			while (inner > -1 and key < a[inner]):
				a[inner+1] = a[inner]
				inner = inner - 1
				
			a[inner+1] = key
				
			outer = outer + 1
		return a

def sorting_test(sorter_obj, number=20, min=-10000, max=10000):
	random_array = get_random_int_array(number, min, max)

	##print " before sorting check is array is already sorted" 
	print sorted(random_array) == random_array
	##print random_array
	##print "\nafter sorting"

	sorter_obj.sort(random_array)

	##print random_array

	##print " sorting is working == "
	print sorted(random_array) == sorter_obj.sort(random_array)

sorter_obj = insertionSorter()
sorting_test(sorter_obj)
