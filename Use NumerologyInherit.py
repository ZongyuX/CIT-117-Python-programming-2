# Name: Zongyu Xie
# Assignment: Numerology Inheritance
# Code Name: Use NumerologyInherit

# Reflection: Share what you liked about this assignment?
#    I enjoyed creating the client program that uses the inherited NumerologyLifePathDetails class with properties. The property access makes the code much cleaner than calling getters, and the dictionary mapping for descriptions is elegant.

# Share what you struggled with?
#    I struggled with ensuring all input validation worked correctly with the inheritance pattern and making sure the property access syntax was consistent throughout the program.

# In your own words describe how decoration works & how does it help coders write better code?
#    Decoration works by adding functionality to existing code through the @ syntax. The @property decorator specifically allows methods to be accessed like attributes, which makes code more readable and intuitive. It helps coders write better code by providing a clean way to implement encapsulation without requiring explicit getter/setter method calls.

# Share exactly 2 things you learned on this assignment:
#    1. How to use properties to create cleaner, more Pythonic access to class attributes without changing the underlying class structure.
#    2. How to properly validate date formats using regular expressions with both dash and slash separators.

import re
from NumerologyLifePathDetails import NumerologyLifePathDetails

def isValidDateFormat(DateToTest: str) -> bool:
    """
    Checks using regex to make sure a date is in mm-dd-yyyy or mm/dd/yyyy format.
    Positions 1-2 are numbers, position 3 is - or /, positions 4-5 are numbers,
    position 6 is - or /, positions 7-10 are numbers.
    """
    return bool(re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', DateToTest))

def get_valid_date():
    """Prompt user for a valid date and return it."""
    while True:
        date_input = input("Enter birth date (mm-dd-yyyy or mm/dd/yyyy): ").strip()
        
        # Check if it's in the correct format
        if isValidDateFormat(date_input):
            return date_input
        else:
            print("Invalid format. Please use mm-dd-yyyy or mm/dd/yyyy format with 8 digits.")

def get_valid_name():
    """Prompt user for a valid name and return it."""
    while True:
        name_input = input("Enter birth name: ").strip()
        if name_input:
            return name_input
        else:
            print("Name cannot be empty. Please enter a valid name.")

def main():
    """Main program function."""
    print("=" * 50)
    print("WELCOME TO THE NUMEROLOGY READER (INHERITANCE VERSION)")
    print("=" * 50)
    print("Program by: Zongyu Xie")
    print("=" * 50)
    
    # Get user input
    name = get_valid_name()
    dob = get_valid_date()
    
    # Create NumerologyLifePathDetails object (inherited class)
    numerology = NumerologyLifePathDetails(name, dob)
    
    # Display results using PROPERTIES (NOT getters)
    print("\n" + "=" * 50)
    print("YOUR NUMEROLOGY READING")
    print("=" * 50)
    print(f"Client Name: {numerology.Name}")        # Property - not getName()
    print(f"Client DOB:  {numerology.Birthdate}")    # Property - not getBirthdate()
    print("-" * 50)
    print(f"Life Path:     {numerology.LifePath}")           # Property
    print(f"Attitude:      {numerology.Attitude}")           # Property
    print(f"Birthday:      {numerology.BirthDay}")           # Property
    print(f"Personality:   {numerology.Personality}")        # Property
    print(f"Power Name:    {numerology.PowerName}")          # Property
    print(f"Soul:          {numerology.Soul}")               # Property
    
    # Display the new life path description (using property)
    print("\n" + "-" * 50)
    print("LIFE PATH DESCRIPTION:")
    print(f"Life Path {numerology.LifePath}: {numerology.LifePathDescription}")
    print("=" * 50)
    
    print("\nThank you for using the Numerology Reader!")

# Call the main function
if __name__ == "__main__":
    main()
