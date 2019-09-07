# Anagram Difference

We define an anagram to be a word whose characters can be rearranged to create another word. Given two strings, we want to know the minimum number of characters that we must modify to make two strings anagrams. If its not possible to make two strings anagrams, we consider this number to be -1. 

For example, 

* *tea* and *ate* are anagrams, so we would need to modify 0 characters.
* *tea* and *toe* are not anagrams, but we can modify 1 character in either string (o -> a or a-> o) to make them anagrams.
* *act* and *acts* are not anagrams and cannot be converted to anagrams because they contain different numbers of characters.

# Function description

Complete the function `getMinimumDifference` in the editor below. The function must return an array of integers which denote the minimum number of characters in either string that need to be modified to make the two strings anagrams. If its not possible, return -1.

`getMinimumDifference` has the following parameter(s):

* *a* : the first string 
* *b* : the second string 

# Constraints 

* Each string consists of lowercase characters [a-z]. 

* 1 <= n <= 100 
* 0 <= | a[i] |, |b[i]| <= 10^4
* 1 <= |a[i]| + |b[i]| <= 10^4

