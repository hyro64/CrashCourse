def count_words(fileName):
    try:
        with open(fileName) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words
