DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date1 DATE NULL,
    flag int default 0,
    dept_name varchar(25),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    venue TEXT NOT NULL,
    time varchar(25),
    url varchar (1500),
    status varchar(25) default 'none',
    flag1 int default 0
);
CREATE TABLE login (
    username varchar(25) NOT NULL,
    passwords varchar(25) NOT NULL,
    department varchar(25)
);
CREATE TABLE a_login (
    username varchar(25) NOT NULL,
    passwords varchar(25) NOT NULL
);
CREATE TABLE feedback (
    id1 INTEGER PRIMARY KEY AUTOINCREMENT,
    id2 INTEGER NOT NULL,
    feedback varchar(200)
);

