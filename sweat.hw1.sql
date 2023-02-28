# Question 1
# Write SQL Code to count the number of employees.

select count(*) from employees;

# Question 2
# Write SQL Code to output the current name of all of the departments.

select dept_name from departments;

# Question 3
# How many employees are in Finance?

select count(*) from dept_emp where dept_no=(select dept_no from departments where dept_name="Finance");

# Question 4
# How many women work in development?

select count(emp_no) from dept_emp

where emp_no in (select emp_no from employees where gender="F")

and dept_no in (select dept_no from departments where dept_name="Development");

# Question 5
# What is the top salary in the company?

select max(salary) from salaries;

# Question 6
# What is the average salary for Marketing?

select avg(salary) from salaries where emp_no

in (select emp_no from dept_emp where dept_no

in (select dept_no from departments where dept_name="Development"));

# Question 7
# What is the lowest salary in the company, who is it and what is their title and department?

create table lowestPaidEmployee(

fname varchar(100),

lname varchar(100),

sal varchar(100),

titl varchar(100),

dept varchar(100)

);

select min(salary) from salaries;

select emp_no from salaries where salary="38623";

select dept_no from dept_emp where emp_no="253406";

insert into lowestPaidEmployee (fname, lname, sal, titl, dept)

values (

(select first_name from employees where emp_no="253406"),

(select last_name from employees where emp_no="253406"),

(select min(salary) from salaries),

(select title from titles where emp_no="253406"),

(select dept_name from departments where dept_no="d004"));

select * from lowestPaidEmployee;

# Question 8
# Who is the oldest person at the company and what is their age?

select first_name, last_name, substring(20230202-(birth_date), 1, 2) as age from employees

where birth_date=(select min(birth_date) from employees);# Question 1
# Write SQL Code to count the number of employees.

select count(*) from employees;

# Question 2
# Write SQL Code to output the current name of all of the departments.

select dept_name from departments;

# Question 3
# How many employees are in Finance?

select count(*) from dept_emp where dept_no=(select dept_no from departments where dept_name="Finance");

# Question 4
# How many women work in development?

select count(emp_no) from dept_emp

where emp_no in (select emp_no from employees where gender="F")

and dept_no in (select dept_no from departments where dept_name="Development");

# Question 5
# What is the top salary in the company? 

select max(salary) from salaries;

# Question 6
# What is the average salary for Marketing?

select avg(salary) from salaries where emp_no

in (select emp_no from dept_emp where dept_no

in (select dept_no from departments where dept_name="Development"));

# Question 7
# What is the lowest salary in the company, who is it and what is their title and department?

create table lowestPaidEmployee(

fname varchar(100),

lname varchar(100),

sal varchar(100),

titl varchar(100),

dept varchar(100)

);

select min(salary) from salaries;

select emp_no from salaries where salary="38623";

select dept_no from dept_emp where emp_no="253406";

insert into lowestPaidEmployee (fname, lname, sal, titl, dept)

values (

(select first_name from employees where emp_no="253406"),

(select last_name from employees where emp_no="253406"),

(select min(salary) from salaries),

(select title from titles where emp_no="253406"),

(select dept_name from departments where dept_no="d004"));

select * from lowestPaidEmployee;

# Question 8
# Who is the oldest person at the company and what is their age? 

select first_name, last_name, substring(20230202-(birth_date), 1, 2) as age from employees

where birth_date=(select min(birth_date) from employees);