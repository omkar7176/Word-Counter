def get_user_input():
    """
    Prompts the user to input a sentence or paragraph.
    Handles empty input error.

    Returns:
    str: The input text from the user.
    """
    text = input("Enter a sentence or paragraph: ")
    
    if not text.strip():
        raise ValueError("Error: No text entered. Please try again.")
    
    return text
