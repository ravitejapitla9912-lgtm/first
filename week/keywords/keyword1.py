"""	Write	a	program	that	imports	the	
keyword	module	and	prints:	the	total	number	of	keywords	in	the	current	Python	version,
and	the	full	list	of	keywords"""
import keyword

print("Total number of keywords:", len(keyword.kwlist))
print("List of keywords:")
print(keyword.kwlist)