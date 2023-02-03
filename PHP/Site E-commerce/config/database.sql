-- SQLite

CREATE TABLE `user` (
    `id` int NOT NULL AUTO_INCREMENT,
    `lastname` varchar(255) NOT NULL,
    `name` varchar(255) NOT NULL,
    `birthday` date NOT NULL,
    `phone_number` int NOT NULL,
    `mail` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`),
    -- UNIQUE KEY `mail` (`mail`) / Durant le copier coller on a du retirer cette ligne car on avait une erreur avec le moteur
);
CREATE TABLE address(
    city varchar(255) NOT NULL,
    country varchar(255) NOT NULL,
    street varchar(255) NOT NULL,
    idUser int NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id)
);
CREATE TABLE product(
    id int PRIMARY KEY NOT NULL,
    name varchar(255) NOT NULL,
    image varchar(255),
    price int NOT NULL,
    description varchar(255) NOT NULL,
    stock int NOT NULL,
    category varchar(255) NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id),
);
CREATE TABLE cart(
    idUser  int NOT NULL,
    idItem int NOT NULL,
    quantity int NOT NULL,
    date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id),
    CONSTRAINT fk_item FOREIGN KEY(idItem) REFERENCES product(id)
); 
CREATE TABLE command(
    idUser  int NOT NULL,
    idItem int NOT NULL,
    date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id),
    CONSTRAINT fk_item FOREIGN KEY(idItem) REFERENCES product(id)
);

CREATE TABLE picture(
    idUser  int,
    idItem int,
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id),
    CONSTRAINT fk_item FOREIGN KEY(idItem) REFERENCES product(id)
);
CREATE TABLE rate (
    idUser  int NOT NULL,
    idItem int NOT NULL,
    rating int NOT NULL,
    comment varchar(255),
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id),
    CONSTRAINT fk_item FOREIGN KEY(idItem) REFERENCES product(id)
);
CREATE TABLE payment(
    idUser  int NOT NULL,
    card varchar(255),
    iban varchar(255),
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id)
);
CREATE TABLE invoice(
    idUser  int NOT NULL,
    date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user FOREIGN KEY(idUser) REFERENCES user(id)
);