def validate_topic(topic: str) -> bool:
    if not topic.strip():
        return False
    if len(topic) > 500:  
        return False
    return True
class output_guardrails:
    @staticmethod
    def validate_length(text: str, min_tokens: int = 50, max_tokens: int = 2000) :
        """Ensure the text is not too short or too long."""
        token_count = len(text.split())
        return min_tokens <= token_count <= max_tokens

    @staticmethod
    def validate_structure(text: str) :
        """Check that the text has headings or basic report structure."""
        headings = ["Introduction", "Key Points", "Conclusion"]
        return any(h.lower() in text.lower() for h in headings)
    