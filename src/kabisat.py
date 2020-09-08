def Kabisat(n):
    if isinstance(n, int) :
        if n % 400 == 0:
            return True
        if n % 100 == 0:
            return False
        if n % 4 == 0:
            return True
        else:
            return False
    else :
        return False


# print(kabisat("2000"))