def checkio(data):

		#replace this for solution
		if data <= 0 and data >= 4000:
			return ""

		roman = {3000:"MMM", 2000:"MM", 1000:"M",
							900:"CM", 800:"DCCC", 700:"DCC", 600:"DC", 500:"D", 400:"CD", 300:"CCC", 200:"CC", 100:"C",
							 90:"XC", 80:"LXXX", 70:"LXX", 60:"LX", 50:"L", 40:"XL", 30:"XXX", 20:"XX", 10:"X",
							  9:"IX", 8:"VIII", 7:"VII", 6:"VI", 5:"V", 4:"IV", 3:"III", 2:"II", 1:"I"
						}

		str = ""
		for k in reversed(sorted((roman.keys()))):
			if data // k == 1:
				str = str + roman[k]
				data = data - k
		return str

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(6) == 'VI', '6'
	assert checkio(76) == 'LXXVI', '76'
	assert checkio(499) == 'CDXCIX', '499'
	assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
	assert checkio(2999) == 'MMCMXCIX', '2999'

