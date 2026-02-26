# Name: Zongyu Xie
# Assignment: Numerology Classes - Client Program
# Reflection: Share what you liked about this assignment?
#    I liked creating the user interface and using the Numerology class to get the calculated numbers. The test cases helped verify everything works correctly.
#    Share what you struggled with?
#    I struggled with validating the date format correctly and making sure the output matches exactly what's required in the sample.
#    Think back to a previous assignment how could rewrite it to use Python classes?
#    A previous temperature converter could use a Temperature class with conversion methods.
#    Share exactly 2 things you learned on this assignment:
#    1. How to import and use a custom class in a client program.
#    2. How to format output to match specific requirements like the sample output.

import re
from Numerology import Numerology

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
    print("WELCOME TO THE NUMEROLOGY READER")
    print("=" * 50)
    print("Program by: Zongyu Xie")
    print("=" * 50)
    
    # Get user input
    name = get_valid_name()
    dob = get_valid_date()
    
    # Create Numerology object
    numerology = Numerology(name, dob)
    
    # Display results using individual getters (as required)
    print("\n" + "=" * 50)
    print("YOUR NUMEROLOGY READING")
    print("=" * 50)
    print(f"Client Name: {numerology.getName()}")
    print(f"Client DOB:  {numerology.getBirthdate()}")
    print("-" * 50)
    print(f"Life Path:     {numerology.getLifePath()}")
    print(f"Attitude:      {numerology.getAttitude()}")
    print(f"Birthday:      {numerology.getBirthDay()}")
    print(f"Personality:   {numerology.getPersonality()}")
    print(f"Power Name:    {numerology.getPowerName()}")
    print(f"Soul:          {numerology.getSoul()}")
    print("=" * 50)
    
    print("\nThank you for using the Numerology Reader!")

# Call the main function (like in the course examples)
if __name__ == "__main__":
    main()
