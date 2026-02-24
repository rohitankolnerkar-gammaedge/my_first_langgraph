class StreamBuffer:
    def __init__(self):
        self.tokens = []

    def __call__(self, token):
        self.tokens.append(token)
        print(token, end='', flush=True)

    def get_buffered_answer(self):
        return "".join(self.tokens)

    def clear(self):
        self.tokens = []