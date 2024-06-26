DEBUG = True

def find_brute(T, P):
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        if DEBUG:
            print(f"Trying at index: {i}")
        k = 0
        while (k < m) and (T[i+k] == P[k]):
            k += 1
        if k == m:
            return i
    return -1

def find_bm(T, P):
    n, m = len(T), len(P)
    
    if m == 0:
        return 0
    
    # Create the dictionary with letters and index
    last = {}
    for k in range(m):
        last[P[k]] = k
        
    i = m - 1
    k = m - 1

    while i < n:
        if T[i] == P[k]: # Match
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else: # mismatch
            j = last.get(T[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1 # Pattern not found

def compute_kmp_fail(P):
    m = len(P)

    fail = [0] * m

    j = 1
    k = 0

    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1

            j += 1
            k += 1 

        elif k > 0:
            k = fail[k-1]

        else:
            j += 1

    return fail

def find_kmp(T, P):
    n, m = len(T), len(P)

    if m == 0:
        return 0
    
    fail = compute_kmp_fail(P)

    j = 0
    k = 0

    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k +=1 
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1

    return -1 # Pattern not found

def main():
    T = "abacaabaccabacabaabb"
    P = "abacab"

    idx = find_brute(T, P)
    print(f"Pattern \"{P}\" starts in text: \"{T}\" at index: {idx}")
    print()

    idx = find_bm(T, P)
    print(f"Pattern \"{P}\" starts in text: \"{T}\" at index: {idx}")
    print()

main()