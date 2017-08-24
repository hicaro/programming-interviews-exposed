"""
Problem: Write an efficient function to find the first nonrepeated character in a string.
For instance, the first nonrepeated character in "total" is 'o' and the first nonrepeated
character in "teeter" is 'r'. Discuss the efficiency of your algorithm.
"""

def first_non_repeated_loop(word):
    """Solution is O(n^2) - not optimal,
    uses search for each character across the remaing characters in the string"""
    length = len(word)
    for i in range(length):
        repeated = False
        # checks the first half
        for j in range(i-1):
            if word[i] == word[j]:
                repeated = True
                break

        # if a repeating character was not found, continue on the other half
        if not repeated:
            for j in range(i+1, length):
                if word[i] == word[j]:
                    repeated = True
                    break

        if not repeated:
            return word[i]

    return None

def first_non_repeated_dict(word):
    """Solution is O(n) - best solution possible"""
    counter = dict()

    for _, c in enumerate(word):
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    for c in word:
        if counter[c] == 1:
            return c

    return None

if __name__ == "__main__":
    print first_non_repeated_loop("total")
    print first_non_repeated_loop("teeter")

    print first_non_repeated_dict("total")
    print first_non_repeated_dict("teeter")
