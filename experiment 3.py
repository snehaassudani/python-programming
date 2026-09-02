s="hello python"
print("original string:",s)
print("length:",len(s))
print("upper case",s.upper())
print("lowercase",s.lower())
print("character index 6:",s[6])
print("position in python:",s.find("python"))
print("slice:",s[6:])
print("replace:",s.replace("python","world"))
print(s)
print("contains python:","python" in s)
print("concatenation:",s + "programming")
s2="   hello world    "
print("trim:",s2.strip())


#OUTPUT:
original string: hello python
length: 12
upper case HELLO PYTHON
lowercase hello python
character index 6: p
position in python: 6
slice: python
replace: hello world
hello python
contains python: True
concatenation: hello pythonprogramming
trim: hello world
