def main():
    with open('books/frankenstein.md') as f:

        file_contents = f.read()
        words = file_contents.split(' ')
        file_contents = file_contents.lower()
        dictionary = {}
        for letter in file_contents:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] += 1
        
        print(f"There are {len(words)} in the book")
        
        for letter in range(ord('a'),ord('z') + 1,1):
            if chr(letter) in dictionary:
                print(f"The letter '{chr(letter)}' appears {dictionary[chr(letter)]} in the book")
        


main()