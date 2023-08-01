# https://leetcode.com/problems/decode-the-message/description/
def decodeMessage(key: str, message: str) -> str:
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        key_list = []
        for i in (list(key)):
            if i not in key_list and i != ' ':
                key_list.append(i)
        hashmap = {key_list[i]: alphabet[i] for i in range(len(key_list))}
        return ''.join([hashmap[i] if i in hashmap.values() else ' ' for i in list(message)])

# Test Cases
print(decodeMessage('the quick brown fox jumps over the lazy dog', 'vkbs bs t suepuv')) # return 'this is a secret'