"""
Write an efficient function that deletes characters from an ASCII string.
Use the prototype:
    string removeChars( string str, string remove )

where any character existing in remove must be deleted from str.
For example, given a str of "Battle of the Vowels: Hawaii vs. Grozny" and a remove of
"aeiou", the function should transform str to "Bttl f th Vwls: Hw vs. Grzny".
Justify any design decisions you make, and discuss the efficiency of your solution
"""

def remove_chars_loop(string, remove):
    """Solution is O(nm) - it uses a secondary string to only copy characters that are wanted"""
    str_new = ""

    for char in string:
        if char not in remove:
            str_new += char

    return str_new

if __name__ == "__main__":
    print remove_chars_loop("Battle of the Vowels: Hawaii vs. Grozny", "aeiou")
