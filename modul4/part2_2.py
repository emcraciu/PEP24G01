# Exceptions

try:
    raise NotImplemented('This is a test')
    print(result)
    result = 1/0
    print(result)
    pass
except ZeroDivisionError:
    print('Cannot divide by 0')
except NameError:
    print('Variable result does not exit')
except Exception:
    print('some unexpected error occurred')
else:
    print('Everithing executed successfully')
finally:
    print('This will always get printed')