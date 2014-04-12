class MyClass:
	i = 12345
	def f(self):
		return "Hello World"

class Complex:
	def __init__(self, realpart, imagepart):
		self.r = realpart
		self.i = imagepart

if __name__ == '__main__':
	x = MyClass()
	print(x.f())
	y = Complex(3.0, -4.5)
	print(y.r,y.i)
