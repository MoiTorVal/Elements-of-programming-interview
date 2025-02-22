# output 'fl'
strs = ['flower', 'flow', 'flight']

def longestCommonPrefix(strs: list[str]) -> str:
        min_length = min(len(word) for word in strs)
        common_prefix = ''

        for i in range(min_length):
            cur_char = strs[0][i]
            if all(cur_char == word[i] for word in strs):
                common_prefix += cur_char
            else:
                print('break')
                break

        return common_prefix

print(longestCommonPrefix(strs))

