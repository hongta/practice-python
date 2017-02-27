
def kmp(text, pattern):
    pattern = list(pattern)

    #Partial match" table
    t = kmp_partial_match_table(pattern)

def kmp_shift_table(pattern):
    shifts = [None] * (len(pattern) + 1)
    shift = 1

    for pos in range(len(pattern) + 1):
        while shift < pos and pattern[pos - 1] != pattern[pos - shift - 1]:
            shift += shifts[pos - shift - 1]
        shifts[pos] = shift
    return shifts


def kmp_partial_match_table(pattern):
    N = len(pattern)
    l = 0 #length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    i = 1
    while i < N:
        print i,l
        if pattern[i] == pattern[l]:
            l +=1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_first_match(text, pattern):
    shifts = kmp_shift_table(pattern)

    start_pos = 0
    match_len = 0
    for c in text:
        while match_len >=0 and pattern[match_len] != c:
            start_pos += shifts[match_len]
            match_len -= shifts[match_len]
        match_len +=1

        if match_len == len(pattern):
            return start_pos
    return False

def kmp_all_matches(text, pattern):
    shfits = kmp_shift_table(pattern)
    start_pos = 0
    match_len = 0

    for c in text:
        while match_len >= 0 and pattern[match_len] != c:
            start_pos += shfits[match_len]
            match_len -= shfits[match_len]
        match_len += 1
        if match_len == len(pattern):
            yield start_pos
            start_pos += shfits[match_len]
            match_len -= shfits[match_len]


if __name__ == '__main__':
    t = "BBC ABCDAB ABCDABCDABDE"
    p = "ABCDABD"
    # p = "AABAAAB"
    # p = "AABAACAABAA"
    # kmp(t, p)
    print kmp_partial_match_table(p)
    print kmp_shift_table(p)
    print kmp_first_match(t, p)
