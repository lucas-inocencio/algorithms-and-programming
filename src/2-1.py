# 1. We’ve seen that n = 42 is legal. What about 42 = n?
n = 42
# SyntaxError

# 2. How about x = y = 1?
x = y = 1
# is legal

# 3. In some languages every statement ends with a semicolon, ;. What happens if you put a semicolon at the end of a Python statement?
n = 42 ;
# Python interpreter ignores

# 4. What if you put a period at the end of a statement?
# SyntaxError

# 5. In math notation you can multiply x and y like this: xy. What happens if you try that in Python?
print(x*y)
# SyntaxError