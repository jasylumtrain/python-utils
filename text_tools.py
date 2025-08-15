"""
text_tools.py
A small collection of text utilities for developers.
"""

def word_count(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())

def char_count(text: str) -> int:
    """Return the number of characters (excluding spaces)."""
    return len(text.replace(" ", ""))
def reverse_text(text: str) -> str:
    """Return the text reversed."""
    return text[::-1]

if __name__ == "__main__":
    sample = "Hello world from GitHub!"
    print(f"Sample text: {sample}")
    print(f"Word count: {word_count(sample)}")
    print(f"Character count: {char_count(sample)}")
        print(f"Reversed text: {reverse_text(sample)}")

