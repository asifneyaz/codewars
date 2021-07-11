def to_jaden_case(string):

    return string.join(w[0].upper() + w[1:] for w in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))