This Python script reads the content of a book from a given file path, generates a report with the total number of words, counts the occurrences of each character, and displays a sorted report of character frequencies.

Features
Reads a book's text from a specified file.
Counts the total number of words in the document.
Counts the frequency of each alphabetical character.
Displays a sorted report of character counts in descending order.
How It Works
The main() function orchestrates the reading of the book's text, counts the words, counts the characters, and generates a report.
get_book_text(path) reads the content of the file specified by path.
get_num_words(text) returns the total number of words in the text.
count_char(text) counts the occurrences of each alphabetical character, ignoring case.
chars_dict_to_sorted_list(num_chars_dict) converts the character frequency dictionary to a list of dictionaries and sorts it in descending order by frequency.
