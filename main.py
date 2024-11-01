def main():
    book_path = "/home/yoel/workspace/github.com/yoelleghesse/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_chars = count_char(text)
    print(num_chars)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_char(text):
    new_txt = text.lower()
    dict_ = {}
    for i in new_txt:
        if i.isalpha():
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
    return dict_

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sorted)
    return sorted_list
    

main()
