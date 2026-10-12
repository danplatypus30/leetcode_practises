class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        i = 3
        res = [[1],[1,1]]
        if numRows == 0:
            return [[]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res
        # 3 rows and more
        # row no. = size of row
        while i <= numRows:
            a = [1]
            j = 2
            # build 1st half of list
            mid = i // 2
            if i % 2 == 1:
                mid += 1
            while j <= mid:
                b = res[i-1-1][j-1] + res[i-1-1][j-1-1]
                a.append(b)
                j += 1
            # duplicate second half list
            k = mid + 1
            while k <= i:
                c = i - k
                a.append(a[c])
                k += 1
            res.append(a)
            i += 1
        return res