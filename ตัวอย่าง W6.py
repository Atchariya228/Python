import sqlite3 #import sqlite3
'''conn = sqlite3.connect("D:\Atchariya_python\example.db")
c = conn.cursor() #create a cursor object 
c.execute (CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
   fnme varchar(30) NOT NULL,
   IName varchar(30) NOT NULL,
   email varchar(100) NOT NULL))
c.execute('''#INSERT INTO users (id,fnme,IName,email) VALUES (NULL,"Atchariya","Wiangkaew","BENZ") ''')
#c.execute('''INSERT INTO users VALUES (NULL,"B","B","B") ''')
#conn.commit() #save (commit) the change
#conn.close() #close the connecton when done'''

'''import sqlite3
def insertTousers (fnme,IName,email) :
    try :
        conn = sqlite3.connect('D:\Atchariya_python\example.db')
        c = conn.cursor()
        sql =  INSERT INTO users (fnme,IName,email) VALUES (?,?,?) 
        data = (fnme,IName,email)
        c.execute(sql,data)
        conn.commit ()
        c.close ()

    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close ()

insertTousers('Atchariya','Wiangkaew','atchariya.wi@gmail.com')
insertTousers('Ben','Ten','123')'''

'''import sqlite3
conn = sqlite3.connect ('D:\Atchariya_python\example.db')
c = conn.cursor()
try : 
    data = ('B','B','B'),('C','C','C'),('D','D','D')
    c.execute('INSERT INTO users (fnme,IName,email) VALUES (?,?,?)',data)
    conn.commit ()
except sqlite3.Error as e:
    print(e)

finally :
    if conn :
        conn.close ()'''
        


