"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...

    def __init__(self, file_path):
        txt_file = open(file_path)
        self.words = self.parse(txt_file)
        print(f"{len(self.words)} words read")
    """The strip() method removes any leading, and trailing whitespaces. Leading 
    means at the beginning of the string, trailing means at the end. You can 
    specify which character(s) to remove, if not, any whitespaces will be removed."""

    def parse(self, txt_file):
        return [word.strip() for word in txt_file]

    def random(self):
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):

    def parse(self, txt_file):
        return[word.strip() for word in txt_file
            if word.strip() and not word.startswith("#")]



    
