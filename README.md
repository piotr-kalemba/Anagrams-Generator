# Anagrams-Generator
The project provides a relatively simple tool for generating all the anagrams of a given phrase based
on given vocabulary list. The order of the words in each anagram is inherited from the order
in the vocabulary list, which ensures that every anagram is generated only once (permutations
of the same anagram are skipped). 


The project consists of the following files:
1) corncob_lowercase.txt - an English vocabulary list
2)  load_vocab.py - module that includes a function for turning the vocabulary list
into a python list
3) generate_anagrams.py - core module of the project with the function anagrams. It is a recursive function that adds 
successively generated results to a file. After execution of the main function within the
module the file with the results is saved in the main directory. 