SELECT F.StartTid, S.Navn AS Stykke, COUNT(BT.Navn) AS AntallSolgtePlasser
FROM Forestilling AS F JOIN BillettType AS BT ON ((F.SalID = BT.SalID) AND (F.StartTid = BT.ForestillingStartTid))
JOIN Billett AS B ON ((BT.ID = B.BillettTypeID) AND (BT.SalID = B.SalID))
JOIN Stykke AS S ON (BT.StykkeID = S.ID)
GROUP BY
    F.StartTid, Stykke
ORDER BY
    AntallSolgtePlasser DESC;