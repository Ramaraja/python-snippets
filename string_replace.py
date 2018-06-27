
def replace(test_string, replace_string):
	start_index = test_string.find(replace_string)
	end_index = len(replace_string) + start_index
	result = []
	replace_flag = False
	for idx, char in enumerate(test_string):
		if idx >= start_index and idx < end_index:
			if replace_flag:
				continue
			else:
				result.append("%s")
				replace_flag = True
		else:
			result.append(char)

	print "".join(result)%("Bonga")
	# print test_string[start_index:end_index]

# tests
replace("Hi how are you?", "you")
replace("Hi how pranesh you pranesh?", "pranesh")
