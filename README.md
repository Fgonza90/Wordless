# Wordless

Wordless is a Python script that helps you solving the popular game called Wordle:
https://wordle.danielfrg.com/

## Usage

The scripts works with the following steps:
1. The script sugest a word for you to write in the game. 
2. Write the word in the game.
3. Introduce the information given by the game into the script in a certain way (explained later).
4. Repeat step 1, 2 and 3 until the right word is found.

## Input

Once the word is writen in the game, it will give you information about the letters:
- If the letter is not in the final word (letter in grey), write it down in the script as a dash "-"
- If the letter is in the final word but not in the right position (letter in yellow), write it down in the script as a capital letter "A".
- If the letter is in the final word and is in the right position (letter in gree), write it down as lower case "a".

For example, the word "nubes": 
- If the 1st letter is correct and the rest is not in the word, write "n----".
- If the 1st letter is in the word but in the wrong position and and the rest is not in the word, write "N----".
- If the 1st letter is correct, the 2st letter is in the word but in the wrong position and, and the rest is not in the word, write "nU---".

## Language

This script uses a txt file that contains all the spanish words.
This script can be used with another language based in the latin alphabet if the txt file is filled with words from other language. 

## License
[MIT](https://choosealicense.com/licenses/mit/)
