def permutationDifference(s,t)->int:
    d = {j:i for i,j in enumerate(t)}
    return sum(abs(i - d[j]) for i,j in enumerate(s))


if __name__ == "__main__":
    print(permutationDifference("abcd", "cadb"))