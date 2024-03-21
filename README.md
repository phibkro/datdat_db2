# DatDat DB2 - Gruppe 122
Oppgave 1, 2, 3, 4, 5, 6 og 7 blir kjørt automatisk via main.py

## Oppskrift

Utfør følgende steg beskrevet under i terminalen inni mappen «datdat_db2»
#### Kjør `python3 main.py` i terminalen
    
1. Dette oppretter tabeller og seed data i db2.db 
    
2. Deretter kjøres Oppgave2_insertAndBuySeatsHovedScenen.py

    Dette setter inn stoler for Hovedscenen i db2.db samt kjøper billetter for forestilling 2024-02-03 Kongsemne

3. Deretter kjøres Oppgave2_insertAndBuySeatsGamleScene.py

    Dette setter inn stoler for Gamle Scene i db2.db samt kjøper billetter for forestillingen 2024-02-03 Størst av alt er kjærligheten

4.  Deretter kjøres oppgave3.py

    Programmet printer ut resultatet i terminalen
    
5. Deretter kjøres oppgave4.py

    > Programmet ber om dato i format (YYYY-MM-DD)
    
    Programmet printer ut resultatet i terminalen

6. Deretter kjøres oppgave5.sql

    Resultatet printes ut i terminalen
    
7. Deretter kjøres oppgave6.sql

    Resultatet printes ut i terminalen
    
8. Deretter kjøres oppgave7.py

    > Programmet ber om navn til skuespilleren. NB: input er case sensetiv. 
    
    Resultatet printes ut i terminalen.

## Forventede resultat

Oppgave 3:
Programmet velger random seksjon og rad i Gamlescene og kjøper 9 voksenbilletter i valgt seksjon og rad.

![Oppgave 3](./Bilder/Oppgave3.png)

Oppgave 4:
(NB: Det finnes bare en forestillingsdato (2024-02-03) der det er solgte billetter.)

![Oppgave 4](./Bilder/Oppgave4.png)

Oppgave 5:

![Oppgave 5](./Bilder/Oppgave5.png)

Oppgave 6:

![Oppgave 6](./Bilder/Oppgave6.png)

Oppgave 7:

![Oppgave 7](./Bilder/Oppgave7.png)

## Diagram av skjema

```mermaid
erDiagram

%% Play section
Season {
    int ID PK
    string Name
}
PlaySeason }|--|| Season : in
PlaySeason {
    int SeasonID PK,FK
    int Year PK
    int PlayID FK
    int HallID FK
}
PlaySeason ||--o| Play : hosts
PlaySeason }|--|| Hall : hosts
Play {
    int ID PK
    string Name
}
Play ||--|{ Act : divided_into

Act {
    int PlayID PK,FK
    int ActNR PK
    string Name
}
Role {
    int ID PK
    string RoleName
}

ActRoleActor {
%% Act FK START:
    int PlayID PK,FK
    int ActNR PK,FK
%% Act FK END;
    string RoleName PK,FK
    string ActorName PK,FK
}
Act ||--|{ ActRoleActor : has
ActRoleActor }|--|| Role : is
Employee ||--o{ ActRoleActor : performs

%% Performance section
Performance {
    int HallID PK,FK
    datetime StartTime PK
}
Performance }o--|| Hall : of

Hall {
    int ID PK
    string Name 
}
Hall ||--|{ Area : divided_into
Area {
    int HallID PK,FK
    string Name PK
}
Area ||--|{ Seat : has

Seat {
%% Area FK START:
    int HallID PK,FK
    string AreaName PK,FK
%% Area FK END;
    int RowNR PK
    int SeatNR PK
}

%% Ticket section
Customer {
    int ID PK
    string Address
    string Name
    string PhoneNR UK
}
Customer ||--o{ TicketPurchase : has

TicketPurchase {
%% Ticket FK START:
    string TicketTypeName PK,FK
    int HallID PK,FK
    string AreaName PK,FK
    int RowNR PK,FK
    int SeatNR PK,FK
%% Ticket FK END;
    int CustomerID FK
    datetime TimeOfPurchase
}
Ticket ||--o{ TicketPurchase : in

TicketType {
    string Name PK
%% Play FK START:
    int PlayID PK,FK
    int HallID PK,FK
%% Play FK END;
    datetime StartTime PK,FK
    int Price
}
TicketType }|--|| Performance : for
Ticket {
%% TicketType FK START:
    string TicketTypeName PK,FK
    int HallID PK,FK
%% TicketType FK END;
%% Seat FK START:
    int RowNR PK,FK
    int SeatNR PK,FK
    string AreaName PK,FK
%% Seat FK END;
}
Ticket ||--|| TicketType : is_of
Ticket ||--|| Seat : for

%% Task section
EmployeeStatus {
    int ID PK
    string Name
}
EmployeePosition {
    int ID PK
    string Name
}
Employee {
    int ID PK
    int EmployeeStatusID FK
    int EmployeePositionID FK
    string Name
    string Email UK
}
Employee }o..|| EmployeePosition : is_of
Employee ||--o{ Assignment : assigned
Employee }o..|| EmployeeStatus : is_of

Assignment {
%% Employee FK START:
    int EmployeeID PK,FK
%% Employee FK END;
%% Task FK START:
    int TaskID PK,FK
%% Task FK END;
%% Performance FK START:
    int HallID PK,FK
    datetime PerformanceStartTime PK, FK
%% Performance FK END;
}
Assignment }o--|| Task : is
Assignment }o--|| Performance : during

Task {
    int ID PK
    string Description
}
```