class Solution(object):

    def groupAnagrams(self, strs):
        """ 
        :type strs: List[str]
        :rtype: List[List[str]]
        """ 

        anagram_hash = {}
        anagram_list = []

        for s in strs: 
            if "".join(sorted(s)) in anagram_hash:
                anagram_hash["".join(sorted(s))].append(s)
            else:
                anagram_hash["".join(sorted(s))] = []
                anagram_hash["".join(sorted(s))].append(s)

        for k, v in anagram_hash.items(): 
            anagram_list.append(v)

        return anagram_list

