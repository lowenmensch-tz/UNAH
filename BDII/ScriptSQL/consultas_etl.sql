----------PARA LA TABLA TIEMPO------------
SELECT CONVERT(DATE, OrderDate) tiempoId, DATEPART(YEAR, OrderDate) año, 
DATEPART(MONTH, OrderDate) mes, DATEPART(WEEK, OrderDate) semana, 
DATEPART(QUARTER, OrderDate) trimestre, DATENAME(WEEKDAY, OrderDate) dia_semana
FROM Orders 
GROUP BY Orders.OrderDate

----------PARA LA TABLA PRODUCTOS------------
select ProductID, ProductName from Products

----------PARA LA TABLA EMPLEADOS------------
select EmployeeID, CONCAT(FirstName, ' ', LastName) Nombre from Employees

----------PARA LA TABLA TRANSPORTISTAS------------
select ShipperID, CompanyName from Shippers

----------PARA LA TABLA HECHOS ORDENES------------
SELECT Orders.EmployeeID, Shippers.ShipperID, CONVERT(DATE,OrderDate) tiempoId, 
Products.ProductID, 
SUM([Order Details].Quantity*[Order Details].UnitPrice*(1-[Order Details].Discount)) total_venta_producto
FROM Orders 
INNER JOIN [Order Details] ON Orders.OrderID=[Order Details].OrderID INNER JOIN Shippers ON
Orders.ShipVia=Shippers.ShipperID INNER JOIN Products ON Products.ProductID=[Order Details].ProductID
GROUP BY Orders.EmployeeID, Shippers.ShipperID, Products.ProductID,
OrderDate
