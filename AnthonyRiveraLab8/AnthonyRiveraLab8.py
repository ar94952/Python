def main():
    print('Kilometers to Miles Converter')
    print('-----------------------------')
    kilometers = float(input('Enter number of kilometers: '))
    print(kilometers, 'km =', km_to_mi(kilometers), 'mi')


def km_to_mi(kilometers):
    return kilometers * 0.6214


main()