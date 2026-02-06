SELECT 
    c.CustomerID,
    c.Gender,
    c.Age
FROM Customers c
WHERE c.CustomerID NOT IN (
    SELECT DISTINCT o.CustomerID 
    FROM Orders o
    WHERE o.OrderDate >= DATEADD(month, -3, GETDATE()) 
);

SELECT TOP 5
    m.ManagerID,
    SUM(o.OrderSum) AS TotalSales
FROM Managers m
JOIN Orders o ON m.ManagerID = o.ManagerID
WHERE o.OrderDate >= DATEADD(month, -1, GETDATE())
GROUP BY m.ManagerID
ORDER BY TotalSales DESC;


SELECT 
    m.Experience_diap,
    AVG(m.WorkExperience) AS Average_Experience_Months
FROM Managers m
WHERE m.ManagerID IN (
    SELECT DISTINCT o.ManagerID
    FROM Orders o
    JOIN Customers c ON o.CustomerID = c.CustomerID
    WHERE c.Gender = 'Female'
      AND c.Age < 30
      AND o.OrderSum >= 3000
)
GROUP BY m.Experience_diap;