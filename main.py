def get_book_content(link:str) -> str:
    with open(link) as f:
        file_contents = f.read()

    return file_contents
    
def count_words(words:str) -> int:
    return len(words.split())

def main():
    content = get_book_content("books/frankenstein.txt")
    print(content)
    print(count_words(content))

if __name__ == "__main__":
    main()
