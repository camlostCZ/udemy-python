def is_palindrome(s: str) -> bool:
    result = True
    stop = len(s) // 2
    for i in range(stop):
        result = result and (s[i] == s[-(i + 1)])
    return result

p = is_palindrome('racecar')
q = is_palindrome('jelenovipivonelej')
