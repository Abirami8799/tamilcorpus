import os
import tamil
from tamil.utf8 import get_letters, get_letters_length, get_words
file=open("frequency+words_in_wiki.txt")
lines=file.read()
word=get_words(lines)

q=['ஃ','அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ',
       '௧','௨','௩','௪','௫','௬','௭','௮','௯','௰','௱','௲','ஶ','௦','க', 'ச','ஞ','ட','ண','த','ந','ப','ம','ய','ர','ல','வ','ழ',
'ள','ற','ன','ஹ','ஜ','ஷ','ஸ']
s=[]

for each in word:
    word1=each.split(',')[0]
    s.append(get_letters_length(word1))
a=set(s)

    
def txtfile(filename,length):
    y=[]
    for each in word:
       word1=each.split(',')[0]
       if get_letters_length(word1)==length:
          y.append(word1)
   

    file1=open(os.path.join(filename,'len_'+str(length)+'.txt'),"w")
    for words in y:
        file1.writelines("%s\n"%words)
               

for i in a:
    result="/home/abirami/Music/findfolders"
    txtfile(result,i)


