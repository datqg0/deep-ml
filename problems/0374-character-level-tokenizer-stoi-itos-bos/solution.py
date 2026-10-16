class CharTokenizer:
    def __init__(self, text: str):
        """
        Build a character-level tokenizer from the input text.
        
        Args:
            text: A string used to build the vocabulary.
        """
        # Your code here
        pass
        clone = text
        clone = sorted(clone)
        
        self.stoi = {}
        self.itos = {}
        o =2
        self.itos[0] = '<BOS>'
        self.stoi['<BOS>'] = 0
        self.itos[1] = '<EOS>'
        self.stoi['<EOS>'] = 1
        for i in clone:
            if(i not in self.stoi):
                self.itos[o] = i
                self.stoi[i] = o
                o+=1
        self.vocab_size = o

    def encode(self, text: str) -> list:
        """
        Encode a string into a list of token indices.
        
        Args:
            text: The string to encode.
        Returns:
            List of integer indices.
        """
        # Your code here
        pass
        o = []
        o.append(0)
        for i in range (len(text)):
            o.append(self.stoi[text[i]])
        o.append(1)
        return o

    def decode(self, indices: list) -> str:
        """
        Decode a list of token indices back into a string.
        
        Args:
            indices: List of integer indices.
        Returns:
            Decoded string.
        """
        # Your code here
        pass
        o = ""
        for i in indices:
            o+=self.itos[i]
        return o
        
