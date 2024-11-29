
# Word Filter Script

This script is a Python program that filters lines of text from standard input (`stdin`) based on a specific word provided as an argument.

## How It Works
1. **Input a word**: The word to search for is passed as a command-line argument.
2. **Process input lines**: The script reads lines from `stdin`, one by one.
3. **Check for the word**: If the given word (case-insensitive) is found in a line, the line is printed to the output.
4. **Ignore case**: Both the input word and lines are converted to lowercase to ensure case-insensitive matching.

## Usage
1. Save the script as `filter_word.py`.
2. Run the script with the word to search for as an argument and provide text input via `stdin`.
