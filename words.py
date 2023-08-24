def print_upper_words(words, must_start_with=None):
    """
    Print words from the given list in uppercase if they meet the conditions.
    
    Args:
        words (list): A list of words.
        must_start_with (set): A set of letters. If provided, only words that start with one of these letters will be printed.
    """
    for word in words:
        if must_start_with is None or any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())

# Tests
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
