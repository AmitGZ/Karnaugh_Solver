import karnaugh


def main():
    output = karnaugh.solve([3, 7, 11, 12, 15, 27], ['V', 'W', 'X', 'Y', 'Z'])
    print(output)


if __name__ == '__main__':
    main()
