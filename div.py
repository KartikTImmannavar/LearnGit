def div(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return -1