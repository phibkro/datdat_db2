SELECT Stykke.Navn AS StykkeNavn, Ansatt.Navn AS SkuespillerNavn , Rolle.RolleNavn
FROM AktRolle
INNER JOIN Ansatt ON (AktRolle.AnsattID = Ansatt.ID)
INNER JOIN Rolle ON (AktRolle.RolleID = Rolle.ID)
INNER JOIN Stykke ON (AktRolle.StykkeID = Stykke.ID)
GROUP BY StykkeNavn, SkuespillerNavn , Rolle.RolleNavn;