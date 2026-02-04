# String initialization (modified values)
s1 = "Good"
s2 = "Morning"
s3 = """Python strings are powerful"""

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print()

# Indexing
print("First character of s2:", s2[0])
print("Last character of s2:", s2[-1])
print()

# Basic operations
# Concatenation
result = s1 + " " + s2
print("Concatenated string:", result)

# Repetition
print("Repeat s2 twice:", s2 * 2)

# Length
print("Length of s3:", len(s3))

# Membership
print("'ring' in s3:", "ring" in s3)
print("'Java' not in s3:", "Java" not in s3)
print()

# String slicing (modified examples)
word = "Development"
print("word =", word)

print("word[1:6]   =", word[1:6])
print("word[:4]    =", word[:4])
print("word[5:]    =", word[5:])
print("word[-5:]   =", word[-5:])
print("word[::3]   =", word[::3])
print("word[::-1]  =", word[::-1])
print()

# String methods
sample = "   learning python strings   "
print("Original:", sample)

print("strip()        ->", sample.strip())
print("upper()        ->", sample.upper())
print("lower()        ->", sample.lower())
print("replace()      ->", sample.replace("python", "java"))
print("count('n')     ->", sample.count("n"))
print("find('python') ->", sample.find("python"))

# split and join
words = sample.strip().split()
print("split() ->", words)

joined = "_".join(words)
print("join with _ ->", joined)

# startswith / endswith
print("startswith('   le') ->", sample.startswith("   le"))
print("endswith('   ')     ->", sample.endswith("   "))

# isalpha / isdigit
alpha = "Python"
digit = "2025"
print("isalpha():", alpha.isalpha())
print("isdigit():", digit.isdigit())


#OUTPUT

# String initialization (modified values)
s1 = "Good"
s2 = "Morning"
s3 = """Python strings are powerful"""

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print()

# Indexing
print("First character of s2:", s2[0])
print("Last character of s2:", s2[-1])
print()

# Basic operations
# Concatenation
result = s1 + " " + s2
print("Concatenated string:", result)

# Repetition
print("Repeat s2 twice:", s2 * 2)

# Length
print("Length of s3:", len(s3))

# Membership
print("'ring' in s3:", "ring" in s3)
print("'Java' not in s3:", "Java" not in s3)
print()

# String slicing (modified examples)
word = "Development"
print("word =", word)

print("word[1:6]   =", word[1:6])
print("word[:4]    =", word[:4])
print("word[5:]    =", word[5:])
print("word[-5:]   =", word[-5:])
print("word[::3]   =", word[::3])
print("word[::-1]  =", word[::-1])
print()

# String methods
sample = "   learning python strings   "
print("Original:", sample)

print("strip()        ->", sample.strip())
print("upper()        ->", sample.upper())
print("lower()        ->", sample.lower())
print("replace()      ->", sample.replace("python", "java"))
print("count('n')     ->", sample.count("n"))
print("find('python') ->", sample.find("python"))

# split and join
words = sample.strip().split()
print("split() ->", words)

joined = "_".join(words)
print("join with _ ->", joined)

# startswith / endswith
print("startswith('   le') ->", sample.startswith("   le"))
print("endswith('   ')     ->", sample.endswith("   "))

# isalpha / isdigit
alpha = "Python"
digit = "2025"
print("isalpha():", alpha.isalpha())
print("isdigit():", digit.isdigit())
