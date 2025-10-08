import pytest
from src.anagrams import group_anagrams

def normalize_output(groups):
    return sorted([sorted(group) for group in groups])

def test_example_1():
    '''strs = ["eat","tea","tan","ate","nat","bat"]'''
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result = group_anagrams(strs)
    assert normalize_output(result) == normalize_output(expected)

def test_empty_list():
    '''пустой спискок'''
    strs = []
    expected = []
    assert group_anagrams(strs) == expected

def test_single_word():
    '''с одним словом'''
    strs = ["abc"]
    expected = [["abc"]]
    assert group_anagrams(strs) == expected

def test_no_anagrams():
    '''без анаграмм'''
    strs = ["cat", "dog", "bird"]
    expected = [["cat"], ["dog"], ["bird"]]
    result = group_anagrams(strs)
    assert normalize_output(result) == normalize_output(expected)

def test_all_anagrams():
    '''все слова анаграммы'''
    strs = ["act", "cat", "tac"]
    expected = [["act", "cat", "tac"]]
    result = group_anagrams(strs)
    assert normalize_output(result) == normalize_output(expected)

def test_empty_strings():
    '''с пустыми строками'''
    strs = ["", "", "a"]
    expected = [["", ""], ["a"]]
    result = group_anagrams(strs)
    assert normalize_output(result) == normalize_output(expected)