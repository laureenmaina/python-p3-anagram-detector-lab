class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)
    
    def match(self, words):
        matches = []
        for examples in words:
            if sorted(examples) == self.sorted_word:
                matches.append(examples)
        return matches
