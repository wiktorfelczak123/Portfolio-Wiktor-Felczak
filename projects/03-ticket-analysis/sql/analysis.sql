-- SQLite queries for the synthetic portfolio dataset.
-- Import data/tickets.csv into a table named tickets before running these queries.

-- 1. Volume, escalation count, and escalation rate by category.
SELECT
  Category,
  COUNT(*) AS ticket_count,
  SUM(CASE WHEN Escalated = 'Yes' THEN 1 ELSE 0 END) AS escalated_count,
  ROUND(1.0 * SUM(CASE WHEN Escalated = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 3) AS escalation_rate
FROM tickets
GROUP BY Category
ORDER BY ticket_count DESC, Category;

-- 2. Monthly ticket volume and escalation rate.
SELECT
  substr(Opened_Date, 1, 7) AS month,
  COUNT(*) AS ticket_count,
  SUM(CASE WHEN Escalated = 'Yes' THEN 1 ELSE 0 END) AS escalated_count,
  ROUND(1.0 * SUM(CASE WHEN Escalated = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 3) AS escalation_rate
FROM tickets
GROUP BY substr(Opened_Date, 1, 7)
ORDER BY month;

-- 3. Closed-ticket resolution time by category. Open tickets have NULL time.
SELECT
  Category,
  COUNT(Resolution_Hours) AS closed_with_time,
  ROUND(AVG(Resolution_Hours), 1) AS average_resolution_hours
FROM tickets
WHERE Status = 'Closed'
GROUP BY Category
ORDER BY average_resolution_hours DESC;

-- 4. Repeat issues by category and queue.
SELECT Category, Queue, COUNT(*) AS repeat_ticket_count
FROM tickets
WHERE Repeat_Issue = 'Yes'
GROUP BY Category, Queue
ORDER BY repeat_ticket_count DESC, Category;

-- 5. Open or long-running cases for a simple review list.
SELECT Ticket_ID, Opened_Date, Category, Priority, Severity, Status, Resolution_Hours, Escalated
FROM tickets
WHERE Status = 'Open' OR Resolution_Hours >= 48
ORDER BY Opened_Date, Ticket_ID;
