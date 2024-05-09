"""
With while loop we can execute a set of statements as long as a condition is true.
With the break statement we can continue and break the loop.
In python we cannot use '++' to increment.
"""
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
