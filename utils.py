def is_float(n):
    try:
        float(n) 
    except ValueError:
        return False
    return True


