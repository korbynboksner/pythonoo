"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, path):
        self.file = open(path, "r")
        self.w =[w.strip() for w in self.file]
    def random(self):
        print(random.choice(self.w))
wf = WordFinder(r"C:\Users\Korbeezy\OneDrive\Documents\vscode\words.txt")
wf.random()