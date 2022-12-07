import Karnaugh


def main():
    Karnaugh.set_style(not_symbol='not ', and_symbol=' and ', or_symbol=' or ', paranthesize_variables=False)
    output = Karnaugh.solve([3, 7, 11, 12, 15, 27], ['V', 'W', 'X', 'Y', 'Z'])
    print(output)


if __name__ == '__main__':
    main()
