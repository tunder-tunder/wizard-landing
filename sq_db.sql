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