CREATE TABLE IF NOT EXISTS Autor (
    id_autora        INT AUTO_INCREMENT,
    imie             VARCHAR(50) NOT NULL,
    nazwisko         VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_autora)
);


CREATE TABLE IF NOT EXISTS Użytkownik (
    pesel                VARCHAR(11) NOT NULL,
    imie                 VARCHAR(50) NOT NULL,
    nazwisko             VARCHAR(50) NOT NULL,
    data_urodzenia       DATE,
    adres_miejscowosc    VARCHAR(100) NOT NULL,
    adres_powiat         VARCHAR(100) NOT NULL,
    adres_wojewodztwo    VARCHAR(100) NOT NULL,
    adres_numer          INTEGER NOT NULL,
    adres_ulica          VARCHAR(100) NOT NULL,
    adres_kod_pocztowy   VARCHAR(6) NOT NULL,
    PRIMARY KEY ( pesel )
);

CREATE TABLE IF NOT EXISTS Filia (
    numer                INTEGER NOT NULL,
    adres_miejscowosc    VARCHAR(100) NOT NULL,
    adres_powiat         VARCHAR(100) NOT NULL,
    adres_wojewodztwo    VARCHAR(100) NOT NULL,
    adres_numer          INTEGER NOT NULL,
    adres_ulica          VARCHAR(100) NOT NULL,
    adres_kod_pocztowy   VARCHAR(6) NOT NULL,
    PRIMARY KEY (numer)
);


CREATE TABLE IF NOT EXISTS Gatunek (
    nazwa   VARCHAR(200) NOT NULL,
    PRIMARY KEY (nazwa)
);

CREATE TABLE IF NOT EXISTS Dzieło (
    id_dziela      INT AUTO_INCREMENT,
    tytul          VARCHAR(100) NOT NULL,
    rok_wydania    INTEGER,
    kraj           VARCHAR(200),
    typ            VARCHAR(7) NOT NULL,
    PRIMARY KEY (id_dziela)
);

ALTER TABLE Dzieło
    ADD CONSTRAINT IF NOT EXISTS ch_inh_dzielo CHECK ( typ IN (
        'Film',
        'Ksiazka'
    ) );

CREATE UNIQUE INDEX IF NOT EXISTS filia__idx ON
    Filia (
        adres_miejscowosc
    ASC,
        adres_powiat
    ASC,
        adres_wojewodztwo
    ASC,
        adres_numer
    ASC,
        adres_ulica
    ASC,
        adres_kod_pocztowy
    ASC );


CREATE TABLE IF NOT EXISTS Dział (
    nazwa         VARCHAR(100) NOT NULL,
    filia_numer   INTEGER NOT NULL,
    PRIMARY KEY (filia_numer, nazwa),
    FOREIGN KEY (filia_numer) REFERENCES Filia(numer) ON UPDATE CASCADE ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS Autorstwo_dzieła (
    dzielo_id_dziela   INTEGER NOT NULL,
    autor_id_autora    INTEGER NOT NULL,
    PRIMARY KEY (dzielo_id_dziela, autor_id_autora),
    FOREIGN KEY ( autor_id_autora ) REFERENCES Autor ( id_autora ) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY ( dzielo_id_dziela )
        REFERENCES Dzieło ( id_dziela )
            ON UPDATE CASCADE
            ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Egzemplarz (
    dzielo_id_dziela         INTEGER NOT NULL,
    id_egzemplarza           INT AUTO_INCREMENT,
    rok_wyd_dodruku          INTEGER,
    dzielo_typ               VARCHAR(100) NOT NULL,
    dzial_filia_numer        INTEGER NOT NULL,
    dzial_nazwa              VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_egzemplarza),
    FOREIGN KEY ( dzial_filia_numer, dzial_nazwa ) 
    REFERENCES Dział ( filia_numer, nazwa ) 
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY ( dzielo_id_dziela)
        REFERENCES Dzieło ( id_dziela )
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    FOREIGN KEY ( dzial_filia_numer, dzial_nazwa )
        REFERENCES Dział ( filia_numer, nazwa )
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    FOREIGN KEY ( dzielo_id_dziela )
        REFERENCES Dzieło ( id_dziela )
            ON UPDATE CASCADE
            ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS Przynależność_do_filii (
    filia_numer        INTEGER NOT NULL,
    uzytkownik_pesel   VARCHAR(11) NOT NULL,
    PRIMARY KEY ( filia_numer, uzytkownik_pesel ),
    FOREIGN KEY ( filia_numer ) REFERENCES Filia ( numer ) 
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY ( uzytkownik_pesel ) REFERENCES Użytkownik ( pesel ) 
        ON UPDATE CASCADE
        ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS Przynależność_do_gatunku (
    dzielo_id_dziela   INTEGER NOT NULL,
    gatunek_nazwa      VARCHAR(200) NOT NULL,
    dzielo_typ         VARCHAR(100) NOT NULL,
    PRIMARY KEY ( dzielo_id_dziela, gatunek_nazwa ),
    FOREIGN KEY ( dzielo_id_dziela )
        REFERENCES Dzieło ( id_dziela ),
    FOREIGN KEY ( gatunek_nazwa )
        REFERENCES Gatunek ( nazwa )
);


CREATE TABLE IF NOT EXISTS Rezerwacja (
    data_dokonania              DATE NOT NULL,
    data_wygasniecia            DATE NOT NULL,
    uzytkownik_pesel            VARCHAR(11) NOT NULL,
    egzemplarz_id_egzemplarza   INTEGER NOT NULL,
    status                      VARCHAR(200) NOT NULL,
    PRIMARY KEY ( uzytkownik_pesel, egzemplarz_id_egzemplarza, data_dokonania ),
    FOREIGN KEY ( egzemplarz_id_egzemplarza )
        REFERENCES Egzemplarz ( id_egzemplarza )
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    FOREIGN KEY ( uzytkownik_pesel )
        REFERENCES Użytkownik ( pesel )
            ON UPDATE CASCADE
            ON DELETE CASCADE
);



CREATE UNIQUE INDEX IF NOT EXISTS uzytkownik__idx ON
    Użytkownik (
        adres_miejscowosc
    ASC,
        adres_powiat
    ASC,
        adres_wojewodztwo
    ASC,
        adres_numer
    ASC,
        adres_ulica
    ASC,
        adres_kod_pocztowy
    ASC );


CREATE TABLE IF NOT EXISTS Wypożyczenie (
    data_wypozyczenia           DATE NOT NULL,
    termin_oddania              DATE NOT NULL,
    uzytkownik_pesel            VARCHAR(11) NOT NULL,
    rzeczywista_data_oddania    DATE,
    egzemplarz_id_egzemplarza   INTEGER NOT NULL,
    PRIMARY KEY ( data_wypozyczenia, uzytkownik_pesel, egzemplarz_id_egzemplarza ),
    FOREIGN KEY ( egzemplarz_id_egzemplarza )
        REFERENCES Egzemplarz ( id_egzemplarza )
            ON UPDATE CASCADE,
    FOREIGN KEY ( uzytkownik_pesel )
        REFERENCES Użytkownik ( pesel )
            ON UPDATE CASCADE
);


--DODANIE UZYTKOWNIKA
CREATE PROCEDURE add_user (IN pesel VARCHAR(11), 
    IN imie VARCHAR(50),
    IN nazwisko VARCHAR(50),
    IN data DATE,
    IN miasto VARCHAR(100),
    IN powiat VARCHAR(100),
    IN wojewodztwo VARCHAR(100),
    IN nr int,
    IN ul VARCHAR(100),
    IN kod VARCHAR(6)
    )
BEGIN
    INSERT INTO Użytkownik(
        pesel, 
        imie, 
        nazwisko, 
        data_urodzenia, 
        adres_miejscowosc, 
        adres_powiat, 
        adres_wojewodztwo, 
        adres_numer, 
        adres_ulica, 
        adres_kod_pocztowy)
    VALUES (pesel, imie, nazwisko, data,
    miasto, powiat, wojewodztwo, nr, ul, kod);
END;

DELIMITER $$
--CZY EGZEMPLARZ JEST WYPOZYCZONY CZY ZAREZERWOWANY
CREATE FUNCTION czy_wypozyczony(id INT) RETURNS VARCHAR(50)
BEGIN
    DECLARE licznik INT DEFAULT 0;
    DECLARE flag VARCHAR(50);
    DECLARE czy_zarezerwowane INT DEFAULT 0;
    SELECT count(*) INTO licznik
        FROM Wypożyczenie
        WHERE 
            rzeczywista_data_oddania IS NULL 
            AND 
            egzemplarz_id_egzemplarza = id;

    SET flag = IF(licznik > 0, "WYPOŻYCZONY", NULL);
    IF (flag = "WYPOŻYCZONY") THEN
        RETURN flag;
    END IF;
    SELECT count(*) INTO czy_zarezerwowane
        FROM Rezerwacja
        WHERE
            status like "AKTYWNA"
            AND
            egzemplarz_id_egzemplarza = id;
    SET flag = IF(czy_zarezerwowane > 0, "ZAREZERWOWANY", "NA PÓŁCE");
    RETURN flag;
END$$
DELIMITER ;

--WYPOZYCZENIE
CREATE PROCEDURE borrow_book (IN pesel VARCHAR(11),
				IN egzemp INT,
				IN czas INT)
BEGIN

    IF(czy_wypozyczony(egzemp) = "WYPOŻYCZONY") THEN 
        SIGNAL SQLSTATE '45000';
    END IF;
	INSERT INTO Wypożyczenie
	VALUES (CURDATE(), DATE_ADD(CURDATE(), INTERVAL czas DAY), pesel, NULL, egzemp);
END;


-----------------------------------------------
--Autorzy i ich dzieła
CREATE VIEW Autorzy_i_dzieła AS
SELECT a.imie AS "Imię autora", a.nazwisko AS "Nazwisko autora",  d.tytul AS "Tytuł"
FROM Autor a, Autorstwo_dzieła b, Dzieło d
WHERE a.id_autora = b.autor_id_autora AND d.id_dziela = b.dzielo_id_dziela;

--Dzieła i ich egzemplarze
CREATE VIEW Egzemplarze_i_dzieła AS
SELECT DISTINCT e.id_egzemplarza AS "Numer egzemplarza",
d.tytul AS "Tytuł", 
e.rok_wyd_dodruku AS "Wydanie", 
e.dzial_nazwa AS "Dział", 
e.dzial_filia_numer AS "Filia",
czy_wypozyczony(e.id_egzemplarza) AS "Status"
FROM Egzemplarz e, Dzieło d, Autor a, 
Autorstwo_dzieła b
WHERE d.id_dziela = e.dzielo_id_dziela 
and a.id_autora = b.autor_id_autora 
and d.id_dziela = b.dzielo_id_dziela;

--UZYTKOWNICY W FILIACH
CREATE VIEW Użytkownicy_w_filiach
AS
    SELECT p.filia_numer AS "Filia", p.uzytkownik_pesel AS "Pesel", u.imie AS "Imię", u.nazwisko AS "Nazwisko"
    FROM Przynależność_do_filii p, Użytkownik u 
    WHERE u.pesel = p.uzytkownik_pesel;

CREATE VIEW helper_wypożyczenia
AS 
    SELECT e.id_egzemplarza as id, czy_wypozyczony(e.id_egzemplarza) AS status
    FROM Egzemplarz e;


--WYPOZYCZENIA UZYTKOWNIKoW
CREATE VIEW Wypożyczenia_użytkowników
AS
    SELECT u.pesel as "PESEL", 
    u.imie AS "Imię", 
    u.nazwisko AS "Nazwisko", 
    d.tytul AS "Tytuł", 
    e.id_egzemplarza AS "Numer egzemplarza", 
    w.data_wypozyczenia AS "Data wypozyczenia", 
    w.termin_oddania AS "Termin oddania",
    e.dzial_filia_numer AS "Filia"
    FROM Wypożyczenie w, Egzemplarz e, Dzieło d, Użytkownik u
        WHERE w.egzemplarz_id_egzemplarza = e.id_egzemplarza 
        and u.pesel = w.uzytkownik_pesel 
        and d.id_dziela = e.dzielo_id_dziela;
        -- TODO
        -- and czy_wypozyczony(e.id_egzemplarza) = "WYPOŻYCZONY";




--SPOZNIENI Z ODDANIEM KSIAZKI
CREATE VIEW Spóźnialscy
AS
	SELECT u.pesel AS "PESEL", 
    u.imie AS "Imię", 
    u.nazwisko AS "Nazwisko",
    d.tytul AS "Tytuł",
    datediff(CURDATE(),w.termin_oddania) AS "Opóźnienie",
    datediff(CURDATE(), w.termin_oddania)*0.05 AS "Kara w złotówkach"
	FROM Użytkownik u, Wypożyczenie w, Egzemplarz e, Dzieło d
	WHERE w.termin_oddania < CURDATE()
    and w.rzeczywista_data_oddania IS NULL 
    and u.pesel = w.uzytkownik_pesel
    and d.id_dziela = e.dzielo_id_dziela
    and w.egzemplarz_id_egzemplarza = e.id_egzemplarza;
