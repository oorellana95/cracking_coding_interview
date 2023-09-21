"""
String Compression:
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def string_compression(s: str):
    if not s:
        return s

    compressed = []
    current_char = s[0]
    char_count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            char_count += 1
        else:
            compressed.append(current_char + str(char_count))
            current_char = s[i]
            char_count = 1

    compressed.append(current_char + str(char_count))
    compressed_str = ''.join(compressed)

    return compressed_str

