def find_it(seq):
    for n in seq:
        counter = seq.count(n)
        if counter % 2 == 1:
            return n

print(find_it([2,2,3,4,4]))