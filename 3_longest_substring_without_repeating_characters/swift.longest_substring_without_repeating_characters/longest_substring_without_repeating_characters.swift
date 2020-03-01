class Solution(object):

    def lengthOfLongestSubstring(self, s):

        head = 0; tail = 0; foundchar = {}  # head and tail indices and list for encountered chars
        index = 0; maxm = 0;                # starting index and maximum range for substring

        for head in range(0, len(s)):
            
            if s[head] in foundchar: 
                tail = max(foundchar[s[head]] + 1, tail)

            foundchar[s[head]] = head

            if head + 1 - tail > maxm: 
                maxm = head + 1 - tail; index = tail

        return maxm

