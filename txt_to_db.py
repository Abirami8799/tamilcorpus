from psycopg2 import connect
import tamil
from tamil.utf8 import get_letters, get_letters_length, get_words

# Connect to the database
connection = connect(host='localhost',
                             user='XXX',
                             password='XXX',
                             database='XXX')

cursor = connection.cursor() 
file=open("unique_sorted_words_in_all_words_20200604-133955.txt")  
lines=file.read()
word=get_words(lines) 

for item in word:
    try:
        m=get_letters(item)
        s=get_letters_length(item)
        sql = "INSERT INTO demo(start_letter,words,end_letter,length) VALUES('{0}','{1}','{2}',{3})".format(m[0],item, m[-1],s)
        cursor.execute(sql)
    except Exception as e:
        connection.rollback()
        print(e)
    connection.commit()



connection.close()



