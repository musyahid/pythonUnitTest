def Rating(n):
    if isinstance(n, int) :
        if n >= 21:
            return 'DEWASA'
        elif n >= 13 :
            return 'REMAJA'
        elif n >= 9:
            return 'BIMBINGAN ORANG TUA'
        elif n <= 8:
            return 'SEMUA USIA'
    else :
        return False

# print(Rating(8))