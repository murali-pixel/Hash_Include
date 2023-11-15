def build_kmp_table(pattern):
    m = len(pattern)
    alphabet_size = 256  # Assuming ASCII character set

    kmp_table = [[0] * alphabet_size for _ in range(m)]
    kmp_table[0][ord(pattern[0])] = 1
    restart_idx = 0

    for i in range(1, m):
        for c in range(alphabet_size):
            kmp_table[i][c] = kmp_table[restart_idx][c]  # Copy mismatch cases
        kmp_table[i][ord(pattern[i])] = i + 1  # Update match case
        restart_idx = kmp_table[restart_idx][ord(pattern[i])]  # Update restart index

    return kmp_table

def search_pattern(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    kmp_table = build_kmp_table(pattern)
    text_idx, pattern_idx = 0, 0

    while text_idx < text_length:
        pattern_idx = kmp_table[pattern_idx][ord(text[text_idx])]
        if pattern_idx == pattern_length:
            return text_idx - pattern_length + 1  # Pattern found
        text_idx += 1

    return -1  # Pattern not found

#TEST CASE 1
text1 = "ABABABABABABAB"
pattern1 = "ABABAA"
position1 = search_pattern(text1, pattern1)
if position1 != -1:
    print(f"Pattern found in text1 at position {position1}")
else:
    print("Pattern not found in text1.")

#TEST CASE 2
text2 = "XYZXYZXYZXYZ"
pattern2 = "XYZ"
position2 = search_pattern(text2, pattern2)
if position2 != -1:
    print(f"Pattern found in text2 at position {position2}")
else:
    print("Pattern not found in text2.")


#TEST CASE 3
text3 = "ABCDEFABCDEFABCDEF"
pattern3 = "CDE"
position3 = search_pattern(text3, pattern3)
if position3 != -1:
    print(f"Pattern found in text3 at position {position3}")
else:
    print("Pattern not found in text3.")

#TEST CASE 4
text4 = "ABCDABCDABCDABCE"
pattern4 = "ABCE"
position4 = search_pattern(text4, pattern4)
if position4 != -1:
    print(f"Pattern found in text4 at position {position4}")
else:
    print("Pattern not found in text4.")

#TEST CASE 5
text5 = "WXYZWXYZWXYZWXY"
pattern5 = "WXYZWXY"
position5 = search_pattern(text5, pattern5)
if position5 != -1:
    print(f"Pattern found in text5 at position {position5}")
else:
    print("Pattern not found in text5.")


