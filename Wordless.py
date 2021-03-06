"""This code helps you to solve the game Wordle. You can play the game here: https://wordle.danielfrg.com/
The code has 3 main bodies:
- Read a file that contains all the spanish words and place them in a list. This start at line 15
- Choose the word from the list that will give more information once written in the game. This start at line 21
    First, it count who many times each letter is used in the list of words and asign this number to the letter.
    Second, it add the 5 numbers asigned to each letter of a word and asign this new number to the word.
    Lastly, it choose the word with the highest number asigned for the user to put it on the game.
- Delete words from the list of words that don't fit with the instructions given by the game. This start at line 44.
    - If the script receive a dash "-" as an input, it will delete all the words from the list that has the letter that replace the dash.
        if the games stays that the letter "B" is grey, we have to write it as a dash and the script will delete all the words that contains a "B".
    - If the script receive a capital letter as an input, it will delete all the words that don't contains that letter or words that cointains that letter in that place.
    - If the script receive a lower case as an input, it will delete all the words that doesn't contain that letter in that exact place.
Once the list of words is check with this information or input and many words are deleted, the script will sugest the word from the list with more points."""

fileSpanish = open('RAE.txt', 'r',encoding="utf-8") #Open a file, read it and place the words in a list 
raeList=[]
for line in fileSpanish: 
    line = line.replace('\n', '')
    if len(line)==5:
        raeList.append(line)
def chooseWord(listAux): #choose the word from a list that will show more information once written in the game
    abecedary={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'ñ':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    dictValues = dict.fromkeys(listAux) #create a dictionary from the list of words
    for word in listAux: #count how many times a letter is used in the dictionary without repeating
        notRepeatedLetter=set(word)
        notRepeatedLetter="".join(notRepeatedLetter)
        for letter in notRepeatedLetter:
            if letter in abecedary:
                abecedary[letter]+=1
    for word in listAux: #calculate how many points a word has.
        notRepeatedLetter=set(word)
        notRepeatedLetter="".join(notRepeatedLetter)
        wordValue=0
        for letter in notRepeatedLetter:
            if letter in abecedary:
                wordValue=wordValue+abecedary[letter]
        dictValues[word]=wordValue
    highestScoreWord=max(dictValues, key=dictValues.get) #find the word with highest score
    return(highestScoreWord);
chosenWord=chooseWord(raeList)#pick the first word you must use in the game
print("Empieza escribiendo la palabra "+ chosenWord + " y ya vamos viendo.")
raeList.remove(chosenWord)
raeListAux=raeList.copy()
while 1==1: #Main body of script. Remove wrong words from list.
    gameResult=input("¿Qué tal ha ido? Escribe los fallos con (-), los aciertos en minusculas y las letras correctas en lugar incorrecto en mayusculas: ")
    if gameResult==chosenWord:#finish loop if word is correct
        break
    letterCount=0
    if gameResult!="0": #write "0" to delete sugested word from list
        for letterResult in gameResult: #modify the list of words with the tips given by the game
            raeList=raeListAux.copy()
            for word in raeList:
                if (letterResult=="-") and (chosenWord[letterCount] in word):
                    raeListAux.remove(word)
                if letterResult.isupper() and (chosenWord[letterCount] == word[letterCount] or not(chosenWord[letterCount] in word)):
                    raeListAux.remove(word)
                if letterResult.islower() and not(chosenWord[letterCount] == word[letterCount]):
                    raeListAux.remove(word)
            letterCount=letterCount+1
    else: #this is what happen if I write "0"
        raeListAux.remove(chosenWord)
    chosenWord=chooseWord(raeListAux) #pick the word you must use in the next step of the game
    print("De acuerdo, ahora prueba con "+ chosenWord)
print("Eso significa que hemos acertado,¡Enhorabuena!")