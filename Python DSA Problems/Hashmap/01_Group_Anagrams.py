Leetcode link: https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = {}

        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            print(word)
            sorted_str = word
            string_dict[sorted_str] = string_dict.get(sorted_str, [])
            string_dict[sorted_str].append(i)
        
        #print(string_dict)
        
        string_dict_sorted = dict(sorted(string_dict.items(),key=lambda item:len(item[1])))
        #print(dict_keys)
        ans = []
        for key,values in string_dict_sorted.items():
            temp=[]
            for value in values:
                temp.append(strs[value])
            ans.append(temp)

        return ans