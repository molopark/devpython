#except.py
try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
