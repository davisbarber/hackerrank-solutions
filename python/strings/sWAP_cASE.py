def swap_case(s):
    swapped = ''
    for c in s:
        swapped += c.upper() if c.islower() else c.lower()

    return swapped


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
