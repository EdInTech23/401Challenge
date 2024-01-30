import time

def offensive_mode(wordlist_path, delay):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as wordlist:
            for word in wordlist:
                print(word.strip())
                time.sleep(delay)  # Add a delay between words
    except FileNotFoundError:
        print("Word list file not found.")

def defensive_mode(search_string, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as wordlist:
            if search_string in wordlist.read():
                print(f"The string '{search_string}' appeared in the word list.")
            else:
                print(f"The string '{search_string}' did not appear in the word list.")
    except FileNotFoundError:
        print("Word list file not found.")

def main():
    mode = input("Select mode (1 for Offensive, 2 for Defensive): ")
    wordlist_path = input("Enter the path to the word list file: ")

    if mode == '1':
        delay = float(input("Enter the delay between words (in seconds): "))
        offensive_mode(wordlist_path, delay)
    elif mode == '2':
        search_string = input("Enter the string to search for: ")
        defensive_mode(search_string, wordlist_path)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
