from collections import Counter
def get_book_content(link:str) -> str:
    with open(link) as f:
        file_contents = f.read()

    return file_contents
    
def count_words(words:str) -> int:
    return len(words.split())

def get_char_count(words:str) -> dict[str, int]:
    words = words.lower()
    """
    # classical solution
    letters_count_dict:dict[str, int] = {}
    for char in words:
        if char in letters_count_dict:
            letters_count_dict[char] += 1
        else:
            letters_count_dict[char] = 1

    return letters_count_dict
    """

    # we use this solution for easier sorting of the values
    char_count_dict: dict[str, int] = Counter(words) # this does the counting for us
    letter_count_dict: dict[str, int] = {}

    # return only items that are in the alphabet
    for char_item in char_count_dict:
        if ord(char_item) >= ord('a') and ord(char_item) <= ord('z'):
            letter_count_dict[char_item] = char_count_dict[char_item]

    """
    We use 'sorted' using the following arguments:
    - key=lambda x:x[1] -> to sort dict according to its values (thus using 1 as index)
    ** not sure why lambda is used tho ** 
    - reverse=True -> sort in descending order
    
    But the output of that function is a list of tuples list[tuples(key,value)]
    That's why we re-convert it to a dictionary using dict()
    """
    letter_count_dict = dict(sorted(letter_count_dict.items(), reverse=True, key=lambda x:x[1]))

    return letter_count_dict

def print_char_count(char_count_dict:dict[str, int]) -> None:
    for item in char_count_dict.items():
        print(f"The '{item[0]}' was found {item[1]} times")


def main():
    filepath: str = "books/frankenstein.txt"
    print(f'--- Begin report of {filepath} ---')
    content: str = get_book_content(filepath)
    print(f'{count_words(content)} words found in the document]\n\n')

    char_count_dict: dict[str, int] = get_char_count(content)

    print_char_count(char_count_dict)



if __name__ == "__main__":
    main()
