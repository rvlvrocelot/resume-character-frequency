import re
import collections
from operator import itemgetter


file = open('C:\\Users\\amahan\\Desktop\\resume.txt', 'r')
fileString = file.read()

#Using RE, eliminate all non alphanumeric characters, lowercase the rest. Turn into a list and take the total
characterList  = list(re.sub('[^0-9a-zA-Z]+', '', fileString).lower())
total = len(characterList)
file.close()

#create default int dict, loop through characterlist and increment for each character
CharacterDict = collections.defaultdict(int)
CharacterList = []

for char in characterList:
    CharacterDict[char] += 1

#convert dict to list so the data can be sorted alphanumerically    
for char in CharacterDict:
    CharacterDict[char] = (float(CharacterDict[char])/total)*100
    CharacterList.append([char,CharacterDict[char]])

CharacterList = sorted(CharacterList, key=itemgetter(0))    

#write the file
outfile = open('C:\\Users\\amahan\\Desktop\\table.txt', 'w')

for key in CharacterList:
    outfile.write(key[0]+','+str(key[1])+'\n') 

outfile.close()



