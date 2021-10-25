CREATE TABLE IF NOT EXISTS mainmenu (
    id integer PRIMARY KEY AUTOINCREMENT, 
    uid integer, 
    name text NOT NULL,
    tele text NOT NULL,
    email text NOT NULL,
    company text, 
    address text, 
    comment text
);

CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT, 
    login text NOT NULL,
    pasw text NOT NULL
);