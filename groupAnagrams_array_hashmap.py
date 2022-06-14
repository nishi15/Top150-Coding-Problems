'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''


from collections import Counter,defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c) - ord("a")] +=1

            result[tuple(count)].append(s)
            

        print(result.values())

    def groupAnagrams2(self, strs):
        result = []
        
        groups = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in groups:
                groups[sorted_word].append(word)
            else:
                groups[sorted_word] = [word]
        
        for key, value in groups.items():
            result.append(value)
            
        return result



if __name__ == "__main__":
    sol = Solution()
    sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    sol.groupAnagrams2(["eat","tea","tan","ate","nat","bat"])