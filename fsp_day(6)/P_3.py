def caesarCipher(s, k):
    result = ""
    k = k % 26
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        else:
            result += ch
    return result

print(caesarCipher("middle-Outz", 2)) 
