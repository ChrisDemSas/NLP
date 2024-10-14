import numpy

class NGrams:
    """Implementation of the N-Grams algorithm using Python. Will only work on sentences.
    
    Attributes:
        n: The N_grams.
        data: The data from the N grams.
        words: The words used in the n-gram.
        vector: The vector of words.
        text: The text to be processed.
    """

    def __init__(self, n: int, text: str) -> None:
        """ Take in a number n to initialize the n-grams.

        Attributes:
            n: The N_grams.
            text: The text to be processed.
        """

        self.n = n
        self.data = {}
        self.words = []
        self.vector = []
        self.text = ""
    
    def process_sentence(self, text: str) -> str:
        """Take in a text and remove all the full stops.
        
        Attributes:
            text: Take in a text and remove all full stops.
        """

        data = text.split()
        final = []

        for word in data:
            if word[-1] == ".":
                final.append(word[:-1])
            else:
                final.append(word)
        
        self.text = " ".join(final).lower()

    def initialize(self, text: str) -> None:
        """Take in a body of text and then populate self.data with keys and empty list.

        Attributes:
            text: The text to be processed.
        """
        
    def process_text(self, text: str) -> list:
        """Initialize the word vector using words in self.words.
        """
        
    def predict(self, fragment: str) -> None:
        """Take in a text fragment and predict the next word.
        
        Attributes:
            fragment: The fragment of a text.
        """

if __name__ == "__main__":
    text = """I don’t like cats and they don’t like me. I used to be allergic to them and I would get stuffed up and have hives. That doesn’t seem to happen anymore. But I still don’t like them. I lived with 3 cats that were not good at peeing in the litter box. They seemed to find something important to me and pee on it. Most of the time they peed on photographs or papers that would be ruined. Cats also bring fleas into the house. There is nothing worse than having to flea dip cats and also flea bomb a home. That is why I don’t like cats.
    """

    n = NGrams(3)
    t = n.remove_full_stops(text)
    print(t)

