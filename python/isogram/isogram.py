def is_isogram(string):
    string = string.lower().replace(" ", "").replace("-", "")
    return len(string) == len(set(string))

    # My version

    # string = string.lower().replace(" ", "").replace("-", "")
    # ltrs = [ltr for ltr in string]

    # flag = True
    # for ltr in string:
    #     if ltrs.count(ltr) > 1:
    #         flag = False
    # return flag
