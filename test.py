# encoding: utf-8

# to work on both Python2 and Python3, I use u"..." but that means Python3
# must be 3.3 or later.

from unittest import TestCase, main


class SmokeTest(TestCase):

    def test_cafe(self):
        from pyuca import Collator
        c = Collator()

        self.assertEqual(sorted(["cafe", "caff", u"café"]), ["cafe", "caff", u"café"])
        self.assertEqual(sorted([u"cafe", u"caff", u"café"], key=c.sort_key), ["cafe", u"café", "caff"])


class TrieTest(TestCase):

    def setUp(self):
        from pyuca.trie import Trie
        self.t = Trie()

    def test_1(self):
        self.t.add("foo", "bar")
        self.assertEqual(self.t.find_prefix("fo"), ("", None, "fo"))
        self.assertEqual(self.t.find_prefix("foo"), ("foo", "bar", ""))
        self.assertEqual(self.t.find_prefix("food"), ("foo", "bar", "d"))

    def test_2(self):
        self.t.add("a", "yes")
        self.t.add("abc", "yes")
        self.assertEqual(self.t.find_prefix("abdc"), ("a", "yes", "bdc"))
class FromFullTest(TestCase):

    def test_1(self):
        from pyuca import Collator
        c = Collator()

        self.assertEqual(c.sort_key(u"\u0332\u0334"), (0x0000, 0x004A, 0x0021, 0x0000, 0x0002, 0x0002, 0x0000))

    def test_2(self):
        from pyuca import Collator
        c = Collator()

        self.assertEqual(c.sort_key(u"\u0430\u0306\u0334"), (0x1991, 0x0000, 0x0020, 0x004A, 0x0000, 0x0002, 0x0002, 0x0000))


if __name__ == "__main__":
    main()
