STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with',
]
def clean_text(text):
    text = text.lower()
    all_letters = "abcdefghijklmnopqrstuvwxyz- "
    text_to_keep = ""
    for char in text:
        if char in all_letters:
            text_to_keep += char
    return text_to_keep
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    file = open("seneca_falls.txt")
    text = file.read()
    
    
    line_broke = text.replace("\n", " ")
    space_fix = line_broke.replace("  ", " ")
    nodub_dash = space_fix.replace("--", " ")
    cleaned_text = clean_text(nodub_dash)
    
    split_text = cleaned_text.split(" ")
    word_list = []
    for word in split_text:
        if not word in STOP_WORDS:
            word_list.append(word)
        
    print(word_list)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
