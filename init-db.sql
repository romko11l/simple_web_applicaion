create table users (
    id INTEGER NOT NULL PRIMARY KEY,
    login char(20),
    money_amount integer,
    card_number char(16),
    status char(10)
);

create table psw (
    id INTEGER NOT NULL PRIMARY KEY,
    pass char(20)
);

INSERT INTO users (login, money_amount, card_number, status) VALUES
    ('admin', 99999, '000000', 'active'),
    ('Roman', 10000, '123456', 'active'),
    ('Anton', -10, '567878', 'active'),
    ('Alice', 1000, '007236', 'not active'),
    ('Elizabeth', 8000, '433867', 'not active');
    
INSERT INTO psw (pass) VALUES
    ('aDm1N'),
    ('SefkjRYXQWfgh903'),
    ('passw0rd'),
    ('ljyvdiy214FD'),
    ('1234567890');
       
