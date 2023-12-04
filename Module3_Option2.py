Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Initial salaries of six employees
>>> salaries = [500, 300, 700, 400, 600, 550]
>>> 
>>> # Increase each salary by 5%
>>> salaries_with_increase = [salary * 1.05 for salary in salaries]
>>> 
>>> # Sort salaries in ascending and descending order
>>> ascending_order = sorted(salaries_with_increase)
>>> descending_order = sorted(salaries_with_increase, reverse=True)
>>> 
>>> # Calculate average salary
>>> average_salary = sum(salaries_with_increase) / len(salaries_with_increase)
>>> 
>>> # Print results
>>> print("Salaries with 5% increase:", salaries_with_increase)
Salaries with 5% increase: [525.0, 315.0, 735.0, 420.0, 630.0, 577.5]
>>> print("Salaries in ascending order:", ascending_order)
Salaries in ascending order: [315.0, 420.0, 525.0, 577.5, 630.0, 735.0]
>>> print("Salaries in descending order:", descending_order)
Salaries in descending order: [735.0, 630.0, 577.5, 525.0, 420.0, 315.0]
>>> print("Average salary:", average_salary)
Average salary: 533.75
