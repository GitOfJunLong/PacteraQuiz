class LargeSum(object):
    def large_sum(self, a, b):
        d = abs(len(a) - len(b))
        if len(a) > len(b):
            b = '0' * d + b
        if len(a) < len(b):
            a = '0' * d + a
        
        l_sum = [0] * len(a) + 1
        a = a[::-1]
        b = b[::-1]

        for i in range(len(a)):
            s = int(a[i]) + int(b[i]) + l_sum[i]
            if s >= 10:
                l_sum[i] = s - 10
                l_sum[i + 1] += 1
            else:
                l_sum[i] = s
        
        if l_sum[-1] == 0:
            del l_sum[-1]
        l_sum = ''.join(l_sum[::-1])
        return l_sum
