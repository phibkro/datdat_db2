--------------------Stykke section--------------------
CREATE TABLE SesongType (
    ID INT PRIMARY KEY,
    Navn VARCHAR(255) NOT NULL 
);

CREATE TABLE Stykke (
    ID INT PRIMARY KEY,
    Navn VARCHAR(255) NOT NULL
);

CREATE TABLE SesongStykke (
    SesongTypeID INT NOT NULL,
    År INT NOT NULL,
    StykkeID INT NOT NULL,
    SalID INT NOT NULL,
    FOREIGN KEY (SesongTypeID) REFERENCES SesongType(ID),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(ID),
    FOREIGN KEY (SalID) REFERENCES Sal(ID)
    PRIMARY KEY (SesongTypeID, År)
);

-------------Akt og Rolle----------------
CREATE TABLE Akt (
    StykkeID INT NOT NULL,
    AktNR INT NOT NULL,
    Navn VARCHAR(255),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(ID)
    PRIMARY KEY (StykkeID, AktNR)
);

CREATE TABLE Rolle (
    ID INT PRIMARY KEY,
    Navn VARCHAR(255) NOT NULL
);

CREATE TABLE AktRolle (
    StykkeID INT NOT NULl,
    AktNR INT NOT NULL,
    RolleNavn VARCHAR(255) NOT NULL,
    AnsattID INT NOT NULl,
    FOREIGN KEY (StykkeID, AktNR) REFERENCES Akt(StykkeID, AktNR),
    FOREIGN KEY (RolleNavn) REFERENCES Rolle(RolleNavn),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(ID)
    PRIMARY KEY (StykkeID, AktNR, RolleNavn, AnsattID)
);

-------------------------Forestilling section--------------------------
CREATE TABLE Sal (
    ID INT PRIMARY KEY,
    Navn VARCHAR(255) NOT NULL
);

CREATE TABLE Forestilling (
    SalID INT NOT NULL,
    StartTid DATETIME NOT NULL,
    FOREIGN KEY (SalID) REFERENCES Sal(ID)
    PRIMARY KEY (SalID, StartTid)
);

CREATE TABLE Område (
    SalID INT NOT NULL,
    Navn VARCHAR(255),
    FOREIGN KEY (SalID) REFERENCES Sal(ID)
    PRIMARY KEY (SalID, Navn)
);

CREATE TABLE Stol (
    SalID INT NOT NULL,
    OmrådeNavn VARCHAR(255),
    StolNR INT NOT NULL,
    RadNR INT,
    FOREIGN KEY (SalID, OmrådeNavn) REFERENCES Område(SalID, Navn)
    PRIMARY KEY (SalID, OmrådeNavn, RadNR, StolNR)
);

------------------------------Billett section---------------------------
CREATE TABLE BillettType (
    ID INT PRIMARY KEY,
    Navn VARCHAR(255),
    StykkeID INT NOT NULL,
    SalID INT NOT NULL,
    ForestillingStartTid DATETIME NOT NULL,
    Pris INT NOT NULL,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(ID),
    FOREIGN KEY (SalID, ForestillingStartTid) REFERENCES Forestilling(SalID, StartTid)
);

CREATE TABLE Billett (
    BillettTypeNavn VARCHAR(255),
    SalID INT,
    OmrådeNavn VARCHAR(255),
    RadNr INT,
    StolNr INT,
    PRIMARY KEY (BillettTypeNavn, SalID, RadNr, StolNr),
    FOREIGN KEY (BillettTypeNavn) REFERENCES BillettType(Navn),
    FOREIGN KEY (SalID, OmrådeNavn, RadNr, StolNr) REFERENCES Stol(SalID, OmrådeNavn, RadNr, StolNr)
);

CREATE TABLE Kunde (
    ID INT PRIMARY KEY,
    Adresse VARCHAR(255),
    Navn VARCHAR(255),
    TlfNr VARCHAR(255),
    UNIQUE (TlfNr)
);

CREATE TABLE BillettKjøp (
    BillettTypeID INT NOT NULL,
    SalID INT,
    OmrådeNavn VARCHAR(255),
    RadNr INT,
    StolNr INT,
    KundeID INT,
    KjøpsTid DATETIME,
    PRIMARY KEY (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr),
    FOREIGN KEY (BillettTypeID) REFERENCES BillettType(ID),
    FOREIGN KEY (SalID, OmrådeNavn, RadNr, StolNr) REFERENCES Stol(SalID, OmrådeNavn, RadNr, StolNr),
    FOREIGN KEY (KundeID) REFERENCES Kunde(ID)
);





------------------------------------Oppgave section-------------------------
CREATE TABLE AnsattStatus (
    ID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

CREATE TABLE AnsattPosisjon (
    ID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

CREATE TABLE Ansatt (
    ID INT PRIMARY KEY,
    AnsattStatusID INT,
    AnsattPosisjonID INT,
    Navn VARCHAR(255),
    Epost VARCHAR(255),
    FOREIGN KEY (AnsattStatusID) REFERENCES AnsattStatus(ID),
    FOREIGN KEY (AnsattPosisjonID) REFERENCES AnsattPosisjon(ID),
    UNIQUE (Epost)
);

CREATE TABLE AnsattOppgave (
    AnsattID INT,
    OppgaveID INT,
    SalID INT,
    ForestillingStartTime DATETIME,
    PRIMARY KEY (AnsattID, OppgaveID, SalID, ForestillingStartTime),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(ID),
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(ID),
    FOREIGN KEY (SalID, ForestillingStartTime) REFERENCES Forestilling(SalID, StartTid)
);

CREATE TABLE Oppgave (
    ID INT PRIMARY KEY,
    Beskrivelse VARCHAR(255)
);
