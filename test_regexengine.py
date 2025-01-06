import unittest
from main import RegexEngine

class TestRegexEngine(unittest.TestCase):
    def test_exact_match(self):
        engine = RegexEngine("abc")
        self.assertTrue(engine.match("abc"))
        self.assertFalse(engine.match("abcd"))
        self.assertFalse(engine.match("ab"))

    def test_wildcard_dot(self):
        engine = RegexEngine("a.c")
        self.assertTrue(engine.match("abc"))
        self.assertTrue(engine.match("aoc"))
        self.assertFalse(engine.match("ac"))

    def test_star_quantifier(self):
        engine = RegexEngine("a*b")
        self.assertTrue(engine.match("b"))
        self.assertTrue(engine.match("ab"))
        self.assertTrue(engine.match("aaab"))
        self.assertFalse(engine.match("ac"))

    def test_plus_quantifier(self):
        engine = RegexEngine("a+b")
        self.assertFalse(engine.match("b"))
        self.assertTrue(engine.match("ab"))
        self.assertTrue(engine.match("aaab"))

    def test_question_mark_quantifier(self):
        engine = RegexEngine("a?b")
        self.assertTrue(engine.match("b"))
        self.assertTrue(engine.match("ab"))
        self.assertFalse(engine.match("aab"))

    def test_start_anchor(self):
        engine = RegexEngine("^abc")
        self.assertTrue(engine.match("abc"))
        self.assertTrue(engine.match("abcd"))
        self.assertFalse(engine.match("ababc"))

    def test_end_anchor(self):
        engine = RegexEngine("abc$")
        self.assertTrue(engine.match("abc"))
        self.assertTrue(engine.match("aabc"))
        self.assertFalse(engine.match("abcd"))

    def test_both_anchors(self):
        engine = RegexEngine("^abc$")
        self.assertTrue(engine.match("abc"))
        self.assertFalse(engine.match("abcd"))
        self.assertFalse(engine.match("ababc"))

    def test_mixed_quantifiers_and_anchors(self):
        engine = RegexEngine("^a*b?c$")
        self.assertTrue(engine.match("ac"))
        self.assertTrue(engine.match("abc"))
        self.assertTrue(engine.match("aaac"))
        self.assertTrue(engine.match("aaabc"))
        self.assertFalse(engine.match("aabbc"))
        self.assertFalse(engine.match("bc"))

if __name__ == '__main__':
    unittest.main()
