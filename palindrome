def palin(s):
    if s=='':
        return True
    else:
        if s[0] == s[-1]:
            return palin(s[1:-1])
        else:
            return False

print palin('ab')
print palin('a')
print palin('level')


def iter_palin(s):
    for index in range(0, len(s)/2):
        if s[index] != s[-(index+1)]:
            return False
        return True

print iter_palin('ab')
print iter_palin('aaa')
print iter_palin('level')
