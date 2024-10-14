import numpy

class NGrams:
    """Implementation of the N-Grams algorithm using Python.
    
    Attributes:
        n: The N_grams.
        data: The data from the N grams.
    """

    def __init__(self, n: int) -> None:
        """ Take in a number n to initialize the n-grams.

        Attributes:
            n: The N_grams.
    
        """

        self.n = n
        self.data = {}
    
    def process_text(self, text: str) -> None:
        """Take in a body of text and then populate self.data.

        Attributes:
            text: The text to be processed.
        
        """
    
    def predict(self, fragment: str) -> None:
        """Take in a text fragment and predict the next word.
        
        Attributes:
            fragment: The fragment of a text.
        """