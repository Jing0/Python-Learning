def make_a_num_list(limit, step):
	i = 0
	numbers = []
	while i < limit:
		print "At the top i is %d" % i
		numbers.append(i)

		i += step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers:"

	for num in numbers:
		print num

def make_a_num_list_new(limit, step):
	numbers = []
	for i in range(0, limit, step):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers:"

	for num in numbers:
		print num

limit = int(raw_input("Please input a number: "))
step = int(raw_input("Please input the step: "))

print "To try the while-loop function, enter '1';"
print "To try the for-loop function, enter '2':"

choice = raw_input()

if choice == '1':
	make_a_num_list(limit, step)
else:
	make_a_num_list_new(limit, step)

