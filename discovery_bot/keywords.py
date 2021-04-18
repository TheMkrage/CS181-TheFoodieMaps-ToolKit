class Keyword:
    def __init__(self, w, can_be_contained_in_other_words):
        self.word = w
        self.can_be_contained_in_other_words = can_be_contained_in_other_words

    def is_present_in(self, text):
        search_term = self.word
        if not self.can_be_contained_in_other_words:
            search_term = ' ' + self.word + ' '
        return search_term in text


categories_to_keywords = {
    'drinks': [
        Keyword('bar', False),
        Keyword('martini', False),
        Keyword('alcohol', False),
        Keyword('drinks', False),

    ],
    'cheese': [Keyword('cheese', True)],
    'fruity': [
        Keyword('strawberry', True),
        Keyword('banana', True),
        Keyword('fruit', True),
        Keyword('grape', True),
        Keyword('apple', True)
    ],
    'dessert': [
        Keyword('chocolate', True),
        Keyword('sweet', True),
        Keyword('sugar', True),
        Keyword('cream', True),
        Keyword('cake', True)
    ]
}
