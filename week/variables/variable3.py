"""Write	a	program	that	swaps	the	values	of	two	variables:	(a)	using	a	temporary	third	variable,	and	(b)	using	Python's	tuple unpacking"""
a = 10
b = 20

temp = a
a = b
b = temp

print("After swapping using temporary variable:")
print("a =", a)
print("b =", b)

x = 10
y = 20

x, y = y, x

print("After swapping using tuple unpacking:")
print("x =", x)
print("y =", y)