def all_variants(s):
    for i in range(len(s)):
        for k in range(len(s) - i):
            yield s[k:k + 1 + i]


a = all_variants("abc")
for i in a:
    print(i)
