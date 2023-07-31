# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/submissions/
def cellsInRange(s: str) -> list[str]:
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    start, end = s.split(':')
    result = []
    
    for i in range(alphabet.index(start[0]), alphabet.index(end[0])+1):
        for j in range(int(start[1]), int(end[1])+1):
            result.append(f"{alphabet[i]}{j}")
    return result

# Test Cases
print(cellsInRange('A1:B2')) # return ['A1','A2','B1','B2']
print(cellsInRange('A1:G7')) # return ['A1','A2','A3','A4','A5','A6','A7','B1','B2','B3','B4','B5','B6','B7','C1','C2','C3','C4','C5','C6','C7','D1','D2','D3','D4','D5','D6','D7','E1','E2','E3','E4','E5','E6','E7','F1','F2','F3','F4','F5','F6','F7','G1','G2','G3','G4','G5','G6','G7']