/*Question 1*/
CREATE TABLE Film (
	idFilm INTEGER PRIMARY KEY NOT NULL,
	titre VARCHAR(80) NOT NULL
);

/*Question 2*/
INSERT INTO Film VALUES (1,"Les évadés"), (2,"Le parrain"), (3,"La vie de Pi")

/*Question 3*/
SELECT * FROM Film

/*Question 4*/
INSERT INTO Film (titre) VALUES ("Chocolat"), ("Scarface"),("Rango")

/*Question 5*/
SELECT * FROM Film

/*Question 6*/
SELECT GROUP_CONCAT(titre, ' ') FROM Film;

/*Question 7*/
CREATE TABLE Acteur (
    idActeur INTEGER PRIMARY KEY NOT NULL,
    nom VARCHAR(80) NOT NULL,
    prenom VARCHAR(80) NOT NULL
);

/*Question 8*/
INSERT INTO Acteur VALUES (1,"Deep","Johnny"), (2,"Pacino","Al"), (3,"Sharma","Suraj")

/*Question 9*/
SELECT GROUP_CONCAT(nom, ' ') FROM Acteur;

/*Question 10*/
CREATE TABLE Filmographie (
	idActeur INTEGER,
	idFilm INTEGER,
    CONSTRAINT fk_filmographie_acteur
        FOREIGN KEY (idActeur)
        REFERENCES Acteur (idActeur),
    CONSTRAINT fk_filmographie_film 
        FOREIGN KEY (idFilm)
        REFERENCES Film (idFilm)
);

/*Question 11*/
INSERT INTO Filmographie (idActeur, idFilm) VALUES (1,4), (1,6), (2,2), (2,5),(3,3)

/*Question 12*/
SELECT * FROM Filmographie

/*Question 13*/
SELECT idFilm FROM Filmographie
WHERE idActeur = 1;

/*Question 14*/
SELECT Film.titre, Acteur.nom FROM Filmographie
JOIN Acteur ON Acteur.idActeur = Filmographie.idActeur
JOIN Film ON Film.idFilm = Filmographie.idFilm

/*Question 15*/
SELECT
    GROUP_CONCAT(
        Acteur.nom || ' a joué dans ' || Film.titre,
        ', '
    )
FROM
    Filmographie
    JOIN Acteur ON Acteur.idActeur = Filmographie.idActeur
    JOIN Film ON Film
    .idFilm = Filmographie.idFilm;
