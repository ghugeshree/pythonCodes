from random import shuffle
print("Good Day, Chief!\nProcessing, please wait...")

f1 = open("myFile.txt", "r")
myLine = f1.read()
f1.close()

f2 = open("myScrambledFile.txt", "w")

myList = myLine.split(" ")  #split the entire line in words

listScrambled = list()      #declare a list for the final scrambled words in list

for i in range(len(myList)): 
    myWord = myList[i]      #takes every word from the list and do the following operations

    apostrophy = ""
    
    #if length of word is 1/2/3 append to ScrambledList as it is!
    if (len(myWord) <= 3):
        listScrambled.append(myWord)
          
    else:
        character = list(myWord)    #make a list of all characters of that word
        firstChar = character[0]    
        character.remove(character[0])  #remove the first char of the word
        lastChar = character[(len(character)-1)]
        
        if(lastChar == "." or lastChar == "," or lastChar == "!" or lastChar == "?"):
            exclamation = character[(len(character)-1)]     #if the last character is an exclamation
            lastChar = character[(len(character)-2)]
            character.pop()

        else:
            if(character[(len(character)-2)] == "'"):
                apostrophy = character[(len(character)-2)]  #if there is an apostrophy
                
            lastChar = character[(len(character)-1)]
            exclamation = ""
            character.pop()
        
        character.pop() #remove the last char of the word
        shuffle(character)  #shuffle the remaining character
        
        newWord = "".join(character)    #join the scrambled char to form a word
        
        scrambledWord = (firstChar + newWord + apostrophy + lastChar + exclamation)    #concatenate them to form a word
        
        listScrambled.append(scrambledWord)     #append it to the final scrambled list
        
f2.write(" ".join(listScrambled))  #prints the final scrambled list with space as separator
f2.close()  
print("Executed Successfully!")
                
        
    
    