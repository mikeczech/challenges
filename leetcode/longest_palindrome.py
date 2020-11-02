import operator

def longest_palindrom(s: str):
    cache = set(s)
    for j in range(0, len(s) - 2 + 1):
        subs = s[j:j+2]
        if subs[0] == subs[-1] and subs not in cache:
            cache.add(subs)

    for i in range(3, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            subs = s[j:j+i]
            print(subs)
            if subs[0] == subs[-1] and subs[1:-1] in cache:
                cache.add(subs)
    return max(cache, key=len)

assert longest_palindrom("babad") == "aba"
assert longest_palindrom("cbbd") == "bb"
assert longest_palindrom("aba") == "aba"
assert longest_palindrom("ccc") == "ccc"
