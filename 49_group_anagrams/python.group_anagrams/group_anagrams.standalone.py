#!/usr/bin/env python

'''
https://leetcode.com/problems/group-anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagram_hash = {}
        #anagram_hash = dict()
        anagram_list = []

        for s in strs: 
            if "".join(sorted(s)) in anagram_hash:
                anagram_hash["".join(sorted(s))].append(s)
            else:
                anagram_hash["".join(sorted(s))] = []
                anagram_hash["".join(sorted(s))].append(s)

        for k, v in anagram_hash.items(): 
            anagram_list.append(v)

        return (strs, anagram_list)

if __name__ == '__main__':
    solution = Solution()
    print "\nInput: %s \nOutput: %s" % solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
