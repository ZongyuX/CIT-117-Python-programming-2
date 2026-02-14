# Name: Zongyu Xie
# Assignment: Real Estate Sales Analyzer

# Reflection:
# *Share what you liked about this assignment?*
# I liked how this assignment connected programming with real-world business applications. 
# Analyzing real estate data felt practical and useful, especially calculating commissions 
# and statistics that a real company would actually use.
#
# *Share what you struggled with?*
# I struggled with handling the CSV file properly and dealing with invalid data entries 
# like the properties with zero prices. Making sure the program didn't crash when 
# encountering bad data required careful error handling.
#
# *How did you like working with CSV files and data analysis concepts?*
# I found working with CSV files to be very practical since this is how real data is 
# often stored. The data analysis concepts like median, average, and filtering by 
# property type showed me how programming can extract meaningful insights from raw data.
#
# *Share exactly 2 things you learned on this assignment:*
# 1. How to read and parse CSV files in Python using the csv module, including skipping 
#    headers and handling missing or invalid data gracefully.
# 2. How to implement data filtering and sorting to analyze specific subsets of data, 
#    like filtering properties by type or price range.

import csv
import os

def getFloatInput(prompt):
    """
    Get a positive float input from user with validation
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input a number that is greater than 0.")
                continue
            return value
        except ValueError:
            print("Input a number that is greater than 0.")

def getMedian(sales_list):
    """
    Calculate the median of a sorted list
    """
    n = len(sales_list)
    if n == 0:
        return 0.0
    
    if n % 2 == 1:  # Odd number of elements
        return sales_list[n // 2]
    else:  # Even number of elements
        return (sales_list[n // 2 - 1] + sales_list[n // 2]) / 2

def readSalesFromCSV(filename):
    """
    Read property sales data from CSV file
    Returns a list of property prices and property details
    """
    sales_prices = []
    property_details = []
    
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read header row
            
            for row_num, row in enumerate(csv_reader, start=2):
                if row and len(row) >= 9:  # Check if row has enough columns
                    try:
                        # Price is in the 9th column (index 8)
                        price = float(row[8])
                        
                        # Only include positive prices (some entries have 0 or invalid)
                        if price > 0:
                            sales_prices.append(price)
                            
                            # Store property details for reference
                            property_details.append({
                                'street': row[0] if len(row) > 0 else '',
                                'city': row[1] if len(row) > 1 else '',
                                'zip': row[2] if len(row) > 2 else '',
                                'state': row[3] if len(row) > 3 else '',
                                'beds': row[4] if len(row) > 4 else '',
                                'baths': row[5] if len(row) > 5 else '',
                                'sqft': row[6] if len(row) > 6 else '',
                                'type': row[7] if len(row) > 7 else '',
                                'price': price
                            })
                    except (ValueError, IndexError) as e:
                        print(f"Skipping row {row_num}: Invalid price data - {row[8] if len(row) > 8 else 'missing'}")
                        continue
        
        return sales_prices, property_details
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], []
    except Exception as e:
        print(f"Error reading file: {e}")
        return [], []

def displayStatistics(sales_prices, property_details, commission_rate=0.03):
    """
    Calculate and display statistics from sales data
    """
    if not sales_prices:
        print("No valid sales data to analyze.")
        return
    
    # Sort the sales prices
    sales_prices.sort()
    
    # Calculate statistics
    minimum = min(sales_prices)
    maximum = max(sales_prices)
    total = sum(sales_prices)
    average = total / len(sales_prices)
    median = getMedian(sales_prices)
    commission = total * commission_rate
    
    # Display header
    print("\n" + "=" * 60)
    print("REAL ESTATE SALES ANALYSIS REPORT")
    print("=" * 60)
    
    # Display sorted properties (show first 20 as sample)
    print(f"\nTotal properties analyzed: {len(sales_prices)}")
    print("\nFirst 20 properties (sorted by price):")
    print("-" * 40)
    
    for i, price in enumerate(sales_prices[:20], 1):
        print(f"Property {i:3d}: ${price:12,.2f}")
    
    if len(sales_prices) > 20:
        print(f"... and {len(sales_prices) - 20} more properties")
    
    # Display statistics
    print("\n" + "-" * 40)
    print("SUMMARY STATISTICS")
    print("-" * 40)
    print(f"Minimum:     ${minimum:12,.2f}")
    print(f"Maximum:     ${maximum:12,.2f}")
    print(f"Total:       ${total:12,.2f}")
    print(f"Average:     ${average:12,.2f}")
    print(f"Median:      ${median:12,.2f}")
    print(f"Commission:  ${commission:12,.2f} (at {commission_rate*100:.1f}%)")
    print("=" * 60)

def filterByPropertyType(property_details, property_type):
    """
    Filter properties by type and return prices
    """
    prices = []
    for prop in property_details:
        if prop['type'].lower() == property_type.lower():
            prices.append(prop['price'])
    return prices

def main():
    """
    Main program function
    """
    print("=" * 60)
    print("WELCOME TO THE REAL ESTATE SALES ANALYZER")
    print("=" * 60)
    
    # Read sales data from CSV file
    filename = "RealEstateData.csv"
    print(f"\nReading data from {filename}...")
    
    sales_prices, property_details = readSalesFromCSV(filename)
    
    if not sales_prices:
        print("No valid sales data found. Exiting program.")
        return
    
    print(f"Successfully read {len(sales_prices)} property records.")
    
    # Main menu loop
    while True:
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("1. View complete sales analysis")
        print("2. Filter by property type")
        print("3. View price range statistics")
        print("4. Exit")
        print("-" * 40)
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Complete analysis
            displayStatistics(sales_prices, property_details)
            
        elif choice == '2':
            # Filter by property type
            print("\nAvailable property types:")
            # Get unique property types
            types = set(prop['type'] for prop in property_details)
            for prop_type in sorted(types):
                count = sum(1 for prop in property_details if prop['type'] == prop_type)
                print(f"  - {prop_type}: {count} properties")
            
            filter_type = input("\nEnter property type to filter: ").strip()
            filtered_prices = filterByPropertyType(property_details, filter_type)
            
            if filtered_prices:
                print(f"\nAnalysis for '{filter_type}' properties ({len(filtered_prices)} properties):")
                # Create filtered property details list
                filtered_details = [p for p in property_details if p['type'].lower() == filter_type.lower()]
                displayStatistics(filtered_prices, filtered_details)
            else:
                print(f"No properties found with type '{filter_type}'")
                
        elif choice == '3':
            # Price range statistics
            try:
                min_price = getFloatInput("Enter minimum price: $")
                max_price = getFloatInput("Enter maximum price: $")
                
                if min_price > max_price:
                    min_price, max_price = max_price, min_price
                    print(f"Swapped values: min=${min_price:,.2f}, max=${max_price:,.2f}")
                
                # Filter properties in range
                range_prices = [p for p in sales_prices if min_price <= p <= max_price]
                
                if range_prices:
                    print(f"\nProperties priced between ${min_price:,.2f} and ${max_price:,.2f}:")
                    print(f"Found {len(range_prices)} properties in this range.")
                    
                    # Create filtered property details
                    range_details = [p for p in property_details if min_price <= p['price'] <= max_price]
                    displayStatistics(range_prices, range_details)
                else:
                    print(f"No properties found in the price range ${min_price:,.2f} - ${max_price:,.2f}")
                    
            except Exception as e:
                print(f"Error in price range selection: {e}")
                
        elif choice == '4':
            # Exit
            print("\n" + "=" * 60)
            print("Thank you for using the Real Estate Sales Analyzer!")
            print("=" * 60)
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

# Call the main function
if __name__ == "__main__":
    main()
