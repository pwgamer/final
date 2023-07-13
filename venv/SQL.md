# 1 задание

SELECT c.login, COUNT(*) AS total_orders
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login

# 2 задание

SELECT track,
CASE
WHEN finished = true THEN 2
WHEN cancelled = true THEN -1
WHEN "inDelivery" = true THEN 1
ELSE 0
END AS status
FROM "Orders";