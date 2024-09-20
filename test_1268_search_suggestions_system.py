import unittest
from typing import List
from 1268_search_suggestions_system import suggestedProducts_final

class TestSearchSuggestionsSystem(unittest.TestCase):
    def setUp(self):
        self.solution = type('obj', (object,), {'suggestedProducts': suggestedProducts})

    def test_example_1(self):
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        searchWord = "mouse"
        expected = [
            ["mobile", "moneypot", "monitor"],
            ["mobile", "moneypot", "monitor"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"],
            ["mouse", "mousepad"]
        ]
        result = self.solution.suggestedProducts(self.solution, products, searchWord)
        self.assertEqual(result, expected)

    def test_example_2(self):
        products = ["havana"]
        searchWord = "havana"
        expected = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        result = self.solution.suggestedProducts(self.solution, products, searchWord)
        self.assertEqual(result, expected)

    def test_example_3(self):
        products = ["bags", "baggage", "banner", "box", "cloths"]
        searchWord = "bags"
        expected = [
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"]
        ]
        result = self.solution.suggestedProducts(self.solution, products, searchWord)
        self.assertEqual(result, expected)

    def test_example_4(self):
        products = ["havana"]
        searchWord = "tatiana"
        expected = [[], [], [], [], [], [], []]
        result = self.solution.suggestedProducts(self.solution, products, searchWord)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()