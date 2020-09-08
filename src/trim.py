def Trim(str, limit):
    char = (str[:limit] + '...') if limit > 2 else "Panjang karakter minimal 2"
    return char

print(Trim("Ini adalah kalimat",2))