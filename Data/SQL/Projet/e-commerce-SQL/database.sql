-- SQLite

CREATE TABLE user(
    id INTEGER PRIMARY KEY NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    phone_number INTEGER NOT NULL,
    mail VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE address(
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    id_user INTEGER NOT NULL,
    FOREIGN KEY(id_user) REFERENCES user(id)
);
CREATE TABLE product(
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    description VARCHAR(255) NOT NULL,
    stock INTEGER NOT NULL
);
CREATE TABLE cart(
    id_user  INTEGER NOT NULL,
    FOREIGN KEY(id_user) REFERENCES user(id),
    id_item INTEGER NOT NULL,
    FOREIGN KEY(id_item) REFERENCES product(id),
    quantity INTEGER NOT NULL,
    date DATE CURRENT_TIMESTAMP
); 
CREATE TABLE command(
    id_user  INTEGER NOT NULL,
    FOREIGN KEY(id_user) REFERENCES user(id),
    id_item INTEGER NOT NULL,
    FOREIGN KEY(id_item) REFERENCES product(id),
    date DATE CURRENT_TIMESTAMP
);

CREATE TABLE photo(
    id_user  INTEGER,
    FOREIGN KEY(id_user) REFERENCES user(id),
    id_item INTEGER,
    FOREIGN KEY(id_item) REFERENCES product(id),
    url VARCHAR(255)
);
CREATE TABLE rate(
    id_user  INTEGER NOT NULL,
    FOREIGN KEY(id_user) REFERENCES user(id),
    id_item INTEGER NOT NULL,
    FOREIGN KEY(id_item) REFERENCES product(id),
    rating INTEGER NOT NULL,
    comment VARCHAR(255)
);
CREATE TABLE payment(
    id_user  INTEGER NOT NULL,
    FOREIGN KEY(id_user) REFERENCES user(id),
    card VARCHAR(255),
    iban VARCHAR(255)
);
CREATE TABLE invoice(
    id_user  INTEGER NOT NULL,
    FOREIGN KEY(id_user) REFERENCES user(id),
    date DATE CURRENT_TIMESTAMP
);