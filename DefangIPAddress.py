# https://leetcode.com/problems/defanging-an-ip-address/description/
def defangIPaddr(address: str) -> str:
    return ''.join([f'[{i}]' if i == '.' else i for i in list(address)])

# Test Cases
print(defangIPaddr('1.1.1.1')) # return '1[.]1[.]1[.]1'
print(defangIPaddr('192.168.0.1')) # return '192[.]168[.]0[.]1'
