
// https://leetcode.com/problems/group-anagrams/

/*
 49. Group Anagrams

 Medium

 Given an array of strings, group anagrams together.

 Example:

 Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
 Output:
 [
   ["ate","eat","tea"],
   ["nat","tan"],
   ["bat"]
 ]
 Note:

 All inputs will be in lowercase.
 The order of your output does not matter.
 */

class Solution49 {

    // solution - hash sorted letters as key to list of entries then output the values of the dictionary
    
    func groupAnagrams(_ strs: [String]) -> (input: [String], output: [[String]]) {
     
        var anagramDictionary = [String : [String]]() 
        var anagramGroups = [[String]]()
        
        for str in strs {
            let key = String(str.sorted())
            anagramDictionary[key] == nil ? anagramDictionary[key] = [str] : anagramDictionary[key]!.append(str)
        }
        
        for (key, _) in anagramDictionary { anagramGroups.append(anagramDictionary[key]!) }
        
        return (strs, anagramGroups)
    }
}

let solution49 = Solution49()
let ex01 = solution49.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print("\nInput: ", ex01.input, "\nOutput: ", ex01.output)
