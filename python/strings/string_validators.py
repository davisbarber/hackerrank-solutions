# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    alnum, alpha, digits, lower, upper = False, False, False, False, False

    for c in s:
        if c.isalpha():
            alpha = True
            alnum = True
            if c.islower():
                lower = True
            else:
                upper = True

        if c.isdigit():
            digits = True
            alnum = True

        if alpha and alnum and digits and lower and upper:
            break

    print(alnum)
    print(alpha)
    print(digits)
    print(lower)
    print(upper)
