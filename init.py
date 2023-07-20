import sqlite3

connection = sqlite3.connect('database.db')


with open('schema1.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO posts (date1,dept_name,title, content,venue,time,url) VALUES (?, ?,?,?,?,?,?)",
            ('2023-01-31','cse','Code War', 'content in first post','SSL','10AM-11AM','https://assets.telegraphindia.com/telegraph/2022/Feb/1645939091_codewars1.jpg')
            )
cur.execute("INSERT INTO posts (date1,dept_name,title, content,venue,time,url) VALUES (?, ?,?,?,?,?,?)",
            ('2023-01-31','ece','AUTOCAD', 'Content for the second post','NSL','2PM-4PM','https://cdn.educba.com/academy/wp-content/uploads/2019/01/AutoCAD-For-student.jpg')
            )
cur.execute("INSERT INTO posts (date1,dept_name,title, content,venue,time,url) VALUES (?, ?,?,?,?,?,?)",
            ('2023-01-31','eee','Circuithon', 'Content for the first post','NLHC 102','1PM-5PM','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREy4Z0pKPyIlC4sZQZ4xjuMDoHK88NFFc-1w&usqp=CAU')
            )
cur.execute("INSERT INTO posts (date1,dept_name,title, content,venue,time,url) VALUES (?, ?,?,?,?,?,?)",
            ('2023-02-31','ce','Treasure Hunt', 'Content for the second post','NIT CAMPUS','9AM-3PM','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTCTNhxs6YXCB4J85MHRKBR1RPalph4jLMSsuyKy0tbv1D-hMA85lM72f49_l0mwJ5QLs&usqp=CAU')
            )
cur.execute("INSERT INTO posts (date1,dept_name,title, content,venue,time,url) VALUES (?, ?,?,?,?,?,?)",
            ('2023-01-31','me','ASSEMBLING AND DISASSEMBLING', 'Content for the first post','ABC HALL','1PM-5PM','https://assets.skyfilabs.com/images/blog/free-mechanical-project-ideas.webp')
            )

cur.execute("INSERT INTO login (username, passwords, department) VALUES (?, ?, ?)",
            ('sudhir', '123456', 'cse')
            )
cur.execute("INSERT INTO login (username, passwords, department) VALUES (?, ?, ?)",
            ('ruthvik', '123456', 'ece')
            )
cur.execute("INSERT INTO login (username, passwords, department) VALUES (?, ?, ?)",
            ('raja', '123456', 'eee')
            )
cur.execute("INSERT INTO login (username, passwords, department) VALUES (?, ?, ?)",
            ('varsha', '123456', 'ce')
            )
cur.execute("INSERT INTO login (username, passwords, department) VALUES (?, ?, ?)",
            ('manaswi', '123456', 'me')
            )
cur.execute("INSERT INTO a_login (username, passwords) VALUES (?, ?)",
            ('joe', '123456')
            )
connection.commit()
connection.close()
