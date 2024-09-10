def count_words(text):
    """
    Count the number of words in the input text.
    
    Parameters:
    text (str): The input string from the user.

    Returns:
    int: The total number of words in the input string.
    """
    words = text.split()
    return len(words)
