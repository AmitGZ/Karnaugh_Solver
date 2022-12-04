import karnaugh


def main():
    output = karnaugh.solve([3, 7, 11, 15, 19], ['first', 'second', 'third', 'fourth', 'fifth'])
    print(output)


if __name__ == '__main__':
    main()
