def checkio(ls):
	result_list = []
	#print "start"
  	for index,value in enumerate(ls):
  		for index2,value2 in enumerate(ls):
				#print "index=",index,"value=",value
				#print "index2=",index2,"value2=",value2
				if index != index2:
				#	print "#"
					if value == value2:
				#		print "##"
						result_list.append(value)
						break

	return result_list

print checkio([1, 2, 3, 1, 3])
print checkio([1, 2, 3, 4, 5])
print checkio([5, 5, 5, 5, 5])
print checkio([10, 9, 10, 10, 9, 8])
