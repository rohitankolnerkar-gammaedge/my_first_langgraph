vague_phrases = [
    "as an AI language model",
    "it depends",
    "some people think",
    "various factors",
]
def  check_constraint(ans):
    if len(ans)<10:
        return False
    elif any(vague in ans.lower() for vague in vague_phrases):
        return False
    else:
        return True
    