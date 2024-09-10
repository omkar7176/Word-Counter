from input_handler import get_user_input
from counter import count_words

def main():
    # Get input from the user
    text = get_user_input()

    # Count words in the input
    word_count = count_words(text)

    # Display the word count
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
