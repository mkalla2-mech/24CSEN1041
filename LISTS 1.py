list_1 = ["2025419670", "KALLA MOKSHITH SRIVATSA"]
print(list_1)
print("Memory location of the list_1", id(list_1))
print(type(list_1))
print(list_1[0])
print(list_1[0][0])
print(type(list_1[0]))

# Common List functions / methods

print(len(list_1))
list_1.append(5)
print(list_1)
list_1.insert(1, "mkalla2@student.gitam.edu")
print(list_1)
list_1.remove("KALLA MOKSHITH SRIVATSA")
print(list_1)
list_1.pop()
print(list_1)

#OUTPUT
['2025419670', 'KALLA MOKSHITH SRIVATSA']
Memory location of the list_1 140450860288448
<class 'list'>
2025419670
2
<class 'str'>
2
['2025419670', 'KALLA MOKSHITH SRIVATSA', 5]
['2025419670', 'mkalla2@student.gitam.edu', 'KALLA MOKSHITH SRIVATSA', 5]
['2025419670', 'mkalla2@student.gitam.edu', 5]
['2025419670', 'mkalla2@student.gitam.edu']

=== Code Execution Successful ===
