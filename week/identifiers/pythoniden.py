"""Identify	which	of	the	following	are	valid	Python	identifiers	and	explain	why	the	invalid	ones	fail:
2value ,	
value_2 ,	
_hidden ,	
class ,	
my-var ,	
MyClass ,	
total$"""
value_2 = 20
_hidden = 30

class MyClass:
    pass

print(value_2)
print(_hidden)
print(MyClass)