#!/usr/bin/env node

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

    
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {

    // anagram dictionary: key - sorted letters, value - list of matching letters
    var anagramDictionary = {}
    var anagramGroups = [] // values from anagram dictionary

    for (str of strs) {
        var key = str.toLowerCase().split('').sort().join('')
        anagramDictionary[key] == undefined ? anagramDictionary[key] = [str] : anagramDictionary[key].push(str)
    }

    for (key in anagramDictionary) { anagramGroups.push(anagramDictionary[key]) }
    
    return anagramGroups
};


console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
