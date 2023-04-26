
def pangrams(s):
    # Write your code here
    s = s.replace(" ", "").lower()
    lst = []
    for i in s:
        if i not in lst:
            lst.append(i)

    if len(lst) == 26:
        return 'pangram'
    else:
        return 'not pangram'
