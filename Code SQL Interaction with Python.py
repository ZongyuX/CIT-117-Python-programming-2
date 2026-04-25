# Name: Zongyu Xie
# Assignment: SQL and Python
# Reflection:  
# *Share what you liked about this assignment?*  
# I liked the real-world application of SQL and Python together, especially how data from multiple files can be joined and analyzed.
#
# *Share what you struggled with?*  
# Importing data without duplication and making sure the joins produced the correct results.
#
# *In your own words how does the DDL and DML Statements work and how you used them?*  
# DDL (Data Definition Language) is used to define the database structure — creating tables (CREATE TABLE).  
# DML (Data Manipulation Language) is used to manage data inside tables — INSERT for adding data, SELECT for querying.
#
# *In your own words describe how the SQL Select Joins work in your code?*  
# I used INNER JOIN to combine Employee with Pay on EmployeeID, and then Pay with SocialSecurityMinimum on Year.  
# This pulls together employee name, earnings, and the minimum salary needed for that year.
#
# *Share exactly 2 things you learned on this assignment:*  
# 1. How to check for existing data before inserting to avoid duplicates.  
# 2. Formatting output to align with columns properly.

import sqlite3
import csv

# Paths to files (adjust as needed)
employee_file = "Employee.txt"
pay_file = "Pay.txt"
ss_min_file = "SocialSecurityMinimum.txt"

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect("retirement.db")
cursor = conn.cursor()

# --- DDL: Create tables if they don't exist ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pay (
        EmployeeID INTEGER,
        Year INTEGER,
        Earnings REAL,
        FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS SocialSecurityMinimum (
        Year INTEGER PRIMARY KEY,
        Minimum REAL
    )
''')

conn.commit()

# --- Helper function to check if table is empty ---
def is_table_empty(table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    return count == 0

# --- DML: Insert data if tables are empty ---

# Insert Employee data
if is_table_empty("Employee"):
    try:
        with open(employee_file, "r") as f:
            reader = csv.reader(f)
            header_skipped = False
            for row in reader:
                # Skip empty rows
                if not row or len(row) == 0:
                    continue
                    
                # Skip header row
                if not header_skipped and row[0].strip().lower() == "employeeid":
                    header_skipped = True
                    continue
                header_skipped = True
                
                # Validate row has at least 2 columns
                if len(row) >= 2:
                    try:
                        emp_id = int(row[0].strip())
                        name = row[1].strip()
                        if name:  # Only insert if name is not empty
                            cursor.execute("INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?)", (emp_id, name))
                    except (ValueError, IndexError):
                        continue  # Skip invalid rows
        conn.commit()
        print("Employee data inserted.")
    except Exception as e:
        print(f"Error inserting Employee data: {e}")

# Insert Pay data
if is_table_empty("Pay"):
    try:
        with open(pay_file, "r") as f:
            reader = csv.reader(f)
            header_skipped = False
            for row in reader:
                # Skip empty rows
                if not row or len(row) == 0:
                    continue
                    
                # Skip header row
                if not header_skipped and row[0].strip().lower() == "employeeid":
                    header_skipped = True
                    continue
                header_skipped = True
                
                # Validate row has at least 3 columns
                if len(row) >= 3:
                    try:
                        emp_id = int(row[0].strip())
                        year = int(row[1].strip())
                        earnings = float(row[2].strip())
                        cursor.execute("INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?)", 
                                     (emp_id, year, earnings))
                    except (ValueError, IndexError):
                        continue  # Skip invalid rows
        conn.commit()
        print("Pay data inserted.")
    except Exception as e:
        print(f"Error inserting Pay data: {e}")

# Insert SocialSecurityMinimum data
if is_table_empty("SocialSecurityMinimum"):
    try:
        with open(ss_min_file, "r") as f:
            reader = csv.reader(f)
            header_skipped = False
            for row in reader:
                # Skip empty rows
                if not row or len(row) == 0:
                    continue
                    
                # Skip header row
                if not header_skipped and row[0].strip().lower() == "year":
                    header_skipped = True
                    continue
                header_skipped = True
                
                # Validate row has at least 2 columns
                if len(row) >= 2:
                    try:
                        year = int(row[0].strip())
                        minimum = float(row[1].strip())
                        cursor.execute("INSERT INTO SocialSecurityMinimum (Year, Minimum) VALUES (?, ?)", 
                                     (year, minimum))
                    except (ValueError, IndexError):
                        continue  # Skip invalid rows
        conn.commit()
        print("SocialSecurityMinimum data inserted.")
    except Exception as e:
        print(f"Error inserting SocialSecurityMinimum data: {e}")

# Verify data was inserted
cursor.execute("SELECT COUNT(*) FROM Employee")
emp_count = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Pay")
pay_count = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM SocialSecurityMinimum")
ss_count = cursor.fetchone()[0]

print(f"\nData counts - Employee: {emp_count}, Pay: {pay_count}, SocialSecurityMinimum: {ss_count}")

if emp_count == 0 or pay_count == 0 or ss_count == 0:
    print("\nWARNING: Some tables are empty. Please check your data files.")
    print("Make sure the files exist and are in the correct format.")
    conn.close()
    exit()

# --- Part 2: Reporting ---
# Join Employee, Pay, and SocialSecurityMinimum
query = """
    SELECT Employee.Name, Pay.Year, Pay.Earnings, SocialSecurityMinimum.Minimum
    FROM Employee
    JOIN Pay ON Employee.EmployeeID = Pay.EmployeeID
    JOIN SocialSecurityMinimum ON Pay.Year = SocialSecurityMinimum.Year
    ORDER BY Employee.Name, Pay.Year
"""

try:
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if not rows:
        print("No data found after joining tables.")
    else:
        # Print formatted output
        print(f"\n{'Employee Name':<20} {'Year':<6} {'Earnings':<12} {'Minimum':<12} {'Include'}")
        print("-" * 70)
        
        for row in rows:
            name, year, earnings, minimum = row
            include = "Yes" if earnings >= minimum else "No"
            # Check if earnings is None
            if earnings is None:
                earnings = 0
            print(f"{name:<20} {year:<6} {earnings:>12,.2f} {minimum:>12,.2f} {include}")
            
except Exception as e:
    print(f"Error executing query: {e}")

# Close connection
conn.close()
