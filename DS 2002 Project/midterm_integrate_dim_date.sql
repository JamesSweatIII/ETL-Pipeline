# ===================================================================================
# How to Integrate a Dimension table. In other words, how to look-up Foreign Key
# values FROM a dimension table and add them to new Fact table columns.
#
# First, go to Edit -> Preferences -> SQL Editor and disable 'Safe Edits'.
# Close SQL Workbench and Reconnect to the Server Instance.
# ===================================================================================

select * from fact_employees;

USE `ds2002-midterm`;

# ==============================================================
# Step 1: Add New Column(s)
# ==============================================================
ALTER TABLE `ds2002-midterm`.fact_employees
ADD COLUMN employee_birthday_date_key int NOT NULL AFTER birth_date,
ADD COLUMN employee_hire_date_key int NOT NULL AFTER hire_date,
ADD COLUMN employee_from_date_key int NOT NULL AFTER from_date,
ADD COLUMN employee_to_date_key int NOT NULL AFTER to_date;

# ==============================================================
# Step 2: Update New Column(s) with value from Dimension table
#         WHERE Business Keys in both tables match.
# ==============================================================
UPDATE `ds2002-midterm`.fact_employees as fe
JOIN `ds2002-midterm`.dim_date AS dd
ON DATE(fe.birth_date) = dd.full_date
SET fe.employee_birthday_date_key = dd.date_key;

UPDATE `ds2002-midterm`.fact_employees as fe
JOIN `ds2002-midterm`.dim_date AS dd
ON DATE(fe.hire_date) = dd.full_date
SET fe.employee_hire_date_key = dd.date_key;

UPDATE `ds2002-midterm`.fact_employees as fe
JOIN `ds2002-midterm`.dim_date AS dd
ON DATE(fe.from_date) = dd.full_date
SET fe.employee_from_date_key = dd.date_key;

UPDATE `ds2002-midterm`.fact_employees as fe
JOIN `ds2002-midterm`.dim_date AS dd
ON DATE(fe.to_date) = dd.full_date
SET fe.employee_to_date_key = dd.date_key;


# ==============================================================
# Step 3: Validate that newly updated columns contain valid data
# ==============================================================
SELECT employee_birthday_date_key,
employee_hire_date_key,
employee_from_date_key,
employee_to_date_key
FROM `ds2002-midterm`.fact_employees
LIMIT 10;

# =============================================================
# Step 4: If values are correct then drop old column(s)
# =============================================================
ALTER TABLE `ds2002-midterm`.fact_employees
DROP COLUMN employee_birthday_date_key,
DROP COLUMN employee_hire_date_key,
DROP COLUMN employee_from_date_key,
DROP COLUMN employee_to_date_key;

# =============================================================
# Step 5: Validate Finished Fact Table.
# =============================================================
SELECT * FROM `ds2002-midterm`.fact_employees
LIMIT 10;

