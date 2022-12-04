import karnaugh


def main():
    output = karnaugh.solve([1, 5], ['first', 'second', 'third', 'fourth', 'fifth'])
    print(output)


if __name__ == '__main__':
    main()
