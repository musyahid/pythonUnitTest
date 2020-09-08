def Convert(i):
    angka = ['','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh','sebelas']
    i = int(i)
    result = ''
    if i >= 0 and i <=11:
        result += f'{angka[i]}'
    elif i<20:
        result += f'{Convert(i % 10)} belas'
    elif i <100:
        result += f'{Convert(i / 10)} puluh {Convert(i % 10)}'
    elif i<200:
        result += f'seratus {Convert(i - 100)}'
    elif i < 1000:
        result += f'{Convert( i / 100)} ratus {Convert(i %100)}'
    elif i < 2000:
        result += f'seribu {Convert(i - 1000)}'
    elif i<1000000:
        result += f'{Convert(i / 1000)} ribu {Convert(i % 1000)}'
    elif i<1000000000:
        result += f'{Convert(i / 1000000)} juta {Convert(i % 1000000)}'
    else:
        result += f'{Convert(i / 1000000000)} milyar {Convert(i % 1000000000)}'
    return result

# print(Convert(12))