# import classes to enable user to enter input in the comand line
import sys
import time

#main method that takes the file_name as an input or in case there is no file_name it uses the .input file
def window_points(file_name = ".input") :
	initial_time = time.clock()
	final_time = 0
	with open(file_name, 'r') as f :
		T = int(f.readline()) 
		if (T > 15) :
			return "The number of test cases have been exceeded"
		elif (T >= 1 and T <= 15) :
			count = 1
			while(count <= T) :
				l1 = int(f.readline())
				count2 = 1
				new_nlst = []
				while(count2 <= l1) :
					l2 = f.readline()
					nlst = l2.split(' ')
					nlst = [int(i) for i in nlst]
					new_nlst.append(nlst)
					count2 += 1
				print(calculate_intersection(new_nlst, count))
				count += 1
		else :
			return "The number of text cases is too small"

	final_time = time.clock() - initial_time
	print "This is the initial time : " + str(initial_time)
	print "This is the final time : " + str(final_time)

def calculate_intersection(lst, n) :
	output = "" 
	intersect = 0
	A = []
	B = []
	new_lst = []
	for i in range(len(lst)) :
		new_lst += [(item) for j, item in enumerate(lst[i])]

	for i in range(len(new_lst)) :
		# check if the value of the height is greater than 10**4
		if new_lst[i] > 10 **4 :
			new_lst[i] = -1
		if i % 2 == 0 :
			A.append(new_lst[i])
		elif i % 2 != 0 :
			B.append(new_lst[i])

	intersect = solve(A,B)
	output += "Case " + str(n) + "# : " + str(intersect)
	return output

def solve(A, B) :
	intersect = 0
	count = 0
	if len(A) == len(B) :
		while (count < len(A)) :
			value_a = cal(A,B, count)
			value_b = cal(B,A, count)
			if value_a :
				intersect += 1
			elif value_b :
				intersect += 1
			else :
				intersect += 0
			count += 1
	else :
		return - 1
	return intersect

def cal(A, B, count) :
	if count == 0 and len(A) :
		return False
	elif count > 0 and len(A) : 
		value_a = 0
		value_b = 0
		for i in range(count +1) :
			value_a += A[i]
		for i in range(count) :
			value_b += B[i]
		if value_b >= value_a :
			return True
		else :
		    return False
	else :
	    return False

if __name__ == "__main__":
	if len(sys.argv) > 1 :
		window_points(sys.argv[1])
	elif len(sys.argv) == 1 :
		window_points()
	else :
		print "What you doing"
