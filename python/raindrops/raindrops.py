def convert(number: int):
    word = []
    
    for x in [(3, "Pling"), (5, "Plang"), (7, "Plong")]: # list of tuples to use - number with respected word to return
        if number % x[0] == 0: # checking if rem is 0
            word.append(x[1])

    # if the word list is empty, then no factors of [3,5,7], so return inputted number.
    # else, join list and return the formed word
    if not word:
        return str(number)
    else:
        return "".join(word)