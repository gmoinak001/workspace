t = int(input("Enter the number of test-cases:"));
for x in range(0, t):
    number = input("Enter the variable A for this test case:");
    a = []
    for i in str(number)[::-1]:
        digit = int(i)
        a.append(int(digit))
        a.reverse()
        import itertools
        for permutation in itertools.permutations(a):
            print (permutation);
