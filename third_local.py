def spam():
    eggs = 31337

spam()
# The error happens because the eggs variable exists only in the local scope created when spam() is called
print(eggs)