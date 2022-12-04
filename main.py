import karnaugh


def main():
    output = karnaugh.solve([1, 5, 7, 9, 19], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    print(output)


if __name__ == '__main__':
    main()
