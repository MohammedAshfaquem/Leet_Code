# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE CONCAT(' ', COALESCE(conditions, ''), ' ') LIKE '% DIAB1%';

