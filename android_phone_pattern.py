"""One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used."""

keypad = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pattern = []


def check_repeat_number(random):
    random = str(random)
    for i in random:
        if i not in pattern:
            pattern.append(i)
        else:
            print("This is a repetitive number.")
            break


check_repeat_number(1224)
