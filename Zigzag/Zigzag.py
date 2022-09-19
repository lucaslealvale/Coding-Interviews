class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1 ):
            return s;
        
        size = len(s)
        volta = 2*numRows - 2
        aux = []
        for i in range(numRows):
            for k in range(i, size, volta):
                aux.append(s[k])
                if i != numRows-1 and i != 0 and k+volta-2*i < size:
                    aux.append(s[k+volta-2*i])
        return ''.join(aux)