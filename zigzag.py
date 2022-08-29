import time, sys
indent = 0 # space of indentation
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True:
        print(' ' * indent, end='')
        print("indent", indent)
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20: 
                # Change direction:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
