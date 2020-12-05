def convert(number):
    drops = [(3, "Pling"), (5, "Plang"), (7, "Plong")] # list of tuples to use - number with respected word to return

    result = [w for f, w in drops if number % f == 0]
    return "".join(result) if result else str(number)