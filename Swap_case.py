def swap_case(s):
    string = ""

    for i in s:

        if i.isupper() == True:

            string+=(i.lower())

        else:

            string+=(i.upper())

    return string


if _name_ == '_main_':
    s = input()
    result = swap_case(s)
    print(result)
