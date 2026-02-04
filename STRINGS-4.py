data1 = "Python123"
data2 = "45678"
data3 = "HelloWorld"

print("data1:", data1)
print("data2:", data2)
print("data3:", data3)

print("isalnum():", data1.isalnum())
print("isdigit():", data2.isdigit())
print("isalpha():", data3.isalpha())

print("find('on') in data1:", data1.find("on"))
print("count('o') in data3:", data3.count("o"))

print("startswith('Py'):", data1.startswith("Py"))
print("endswith('123'):", data1.endswith("123"))

#OUTPUT
data1: Python123
data2: 45678
data3: HelloWorld
isalnum(): True
isdigit(): True
isalpha(): True
find('on') in data1: 4
count('o') in data3: 2
startswith('Py'): True
endswith('123'): True

=== Code Execution Successful ===
