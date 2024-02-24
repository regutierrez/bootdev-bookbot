def get_book_content(link:str) -> str:
    with open(link) as f:
        file_contents = f.read()

    return file_contents
    
def count_words(words:str) -> int:
    return len(words.split())

def count_letters(words:str) -> dict[str, int]:
    words = words.lower()
    letters_count_dict:dict[str, int] = {}

    for char in words:
        if char in letters_count_dict:
            letters_count_dict[char] += 1
        else:
            letters_count_dict[char] = 1

    return letters_count_dict

def main():
    content = get_book_content("books/frankenstein.txt")
    # print(content)
    # print(count_words(content))
    print(count_letters(content))

if __name__ == "__main__":
    main()
