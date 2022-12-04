import karnaugh


def main():
    output = karnaugh.solve([19, 25, 30], ['first', 'second', 'third', 'fourth', 'fifth'])
    print(output)


if __name__ == '__main__':
    main()
