import karnaugh


def main():
    karnaugh.set_style(not_symbol='not ', and_symbol=' and ', or_symbol=' or ', paranthesize_variables=False)
    output = karnaugh.solve([3, 7, 11, 12, 15])
    print(output)


if __name__ == '__main__':
    main()
