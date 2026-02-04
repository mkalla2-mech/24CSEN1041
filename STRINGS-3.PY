text = "   python STRING methods demo   "

print("Original text:", text)

print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())

print("upper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())
print("swapcase():", text.swapcase())

print("replace 'STRING' with 'string':",
      text.replace("STRING", "string"))

words = text.strip().split()
print("split():", words)

print("join():", ",".join(words))

#OUTPUT
Original text:    python STRING methods demo   
strip(): python STRING methods demo
lstrip(): python STRING methods demo   
rstrip():    python STRING methods demo
upper():    PYTHON STRING METHODS DEMO   
lower():    python string methods demo   
title():    Python String Methods Demo   
swapcase():    PYTHON string METHODS DEMO   
replace 'STRING' with 'string':    python string methods demo   
split(): ['python', 'STRING', 'methods', 'demo']
join(): python,STRING,methods,demo

=== Code Execution Successful ===
