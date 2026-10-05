'''Write	a	program	that	declares	five	valid	identifiers	of	different	kinds:	a	variable,	a	constant-style	name,	a	function	name,	a
class	name,	and	a	name	using	an	underscore.	Print	all	of	them'''
age = 18
MAX_MARKS = 100
def calculate_sum():
    return 10 + 20
class Student:
    pass
student_name = "sravan"
print("Variable:", age)
print("Constant-style name:", MAX_MARKS)
print("Function name result:", calculate_sum())
print("Class name:", Student)
print("Identifier with underscore:", student_name)
"""Variable: 18
Constant-style name: 100
Function name result: 30
Class name: <class '__main__.Student'>
Identifier with underscore: sravan"""