
'''
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approch of suming 'Equally Spaced Abscissas' 

method 2: 
"Simpson Rule"

'''
from __future__ import print_function


def method_2(boundary, steps):
# "Simpson Rule"
# int(f) = delta_x/2 * (b-a)/3*(f1 + 4f2 + 2f_3 + ... + fn)
	h = (boundary[1] - boundary[0]) / steps
	a = boundary[0]#front
	b = boundary[1]#rear
	x_i = makePoints(a,b,h)#front + increment
	y = 0.0 #define as float type
	y += (h/3.0)*f(a) #define y
	cnt = 2
	for i in x_i: #iteration
		y += (h/3)*(4-2*(cnt%2))*f(i) #update y valuable	
		cnt += 1
	y += (h/3.0)*f(b) #update y valuable
	return y

def makePoints(a,b,h):
	x = a + h
	while x < (b-h):
		yield x
		x = x + h #update x valuable by adding x

def f(x): #enter your function here
	y = (x-0)*(x-0)
	return y

def main():
	a = 0.0 #Lower bound of integration
	b = 1.0	#Upper bound of integration
	steps = 10.0		#define number of steps or resolution
	boundary = [a, b]	#define boundary of integration
	y = method_2(boundary, steps)
	print('y = {0}'.format(y)) #print format

if __name__ == '__main__':
        main()
