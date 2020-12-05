def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b) or strand_a is None or strand_b is None:
        raise ValueError("DNA Strands not equal in length")
    else:
        errors = [a != b for a, b in zip(strand_a, strand_b) if a != b]
        return len(errors)