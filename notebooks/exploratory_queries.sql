-- 1. Top 5 Companies by Net Profit (Average over years)
SELECT company_name, AVG(net_profit) as avg_profit 
FROM profitandloss p
JOIN companies c ON p.company_id = c.id
GROUP BY company_name
ORDER BY avg_profit DESC LIMIT 5;

-- 2. Companies with highest Operating Profit Margin (OPM)
SELECT company_name, AVG(opm_percentage) as avg_opm
FROM profitandloss p
JOIN companies c ON p.company_id = c.id
GROUP BY company_name
ORDER BY avg_opm DESC LIMIT 5;

-- 3. Debt-to-Equity Snapshot
SELECT company_name, year, borrowings, reserves
FROM balancesheet b
JOIN companies c ON b.company_id = c.id
WHERE year = 2024;