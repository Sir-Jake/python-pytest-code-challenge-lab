import pytest
from palindrome import longest_palindromic_substring


class TestBasicCases:
    def test_babad_returns_valid_palindrome(self):
        result = longest_palindromic_substring("babad")
        assert result in ("bab", "aba")

    def test_cbbd_returns_bb(self):
        assert longest_palindromic_substring("cbbd") == "bb"

    def test_racecar_is_full_string(self):
        assert longest_palindromic_substring("racecar") == "racecar"

    def test_abacaba_returns_full_string(self):
        assert longest_palindromic_substring("abacaba") == "abacaba"

    def test_noon_returns_noon(self):
        assert longest_palindromic_substring("noon") == "noon"

    def test_ac_returns_single_char(self):
        result = longest_palindromic_substring("ac")
        assert result in ("a", "c")


class TestEdgeCases:
    def test_single_character(self):
        assert longest_palindromic_substring("a") == "a"

    def test_single_digit(self):
        assert longest_palindromic_substring("7") == "7"

    def test_two_same_characters(self):
        assert longest_palindromic_substring("aa") == "aa"

    def test_two_different_characters(self):
        result = longest_palindromic_substring("ab")
        assert result in ("a", "b")

    def test_all_same_characters(self):
        assert longest_palindromic_substring("aaaa") == "aaaa"

    def test_palindrome_embedded_in_longer_string(self):
        assert longest_palindromic_substring("xyzracecarabc") == "racecar"

    def test_numeric_string(self):
        assert longest_palindromic_substring("12321") == "12321"

    def test_long_string_no_long_palindrome(self):
        result = longest_palindromic_substring("abcdefg")
        assert len(result) == 1
        assert result in list("abcdefg")

    def test_long_palindrome_at_end(self):
        assert longest_palindromic_substring("abcmadam") == "madam"

    def test_long_palindrome_at_start(self):
        assert longest_palindromic_substring("levelbcd") == "level"


class TestReturnType:
    def test_returns_string(self):
        result = longest_palindromic_substring("babad")
        assert isinstance(result, str)

    def test_result_is_palindrome(self):
        for s in ["babad", "cbbd", "racecar", "abcba", "noon", "a"]:
            result = longest_palindromic_substring(s)
            assert result == result[::-1]

    def test_result_is_substring(self):
        for s in ["babad", "cbbd", "racecar", "abcba", "noon"]:
            result = longest_palindromic_substring(s)
            assert result in s
