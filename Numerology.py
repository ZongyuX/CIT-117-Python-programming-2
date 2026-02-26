# Name: Zongyu Xie
# Assignment: Numerology Classes
# Reflection: Share what you liked about this assignment?
#    I liked how this assignment uses real-world numerology concepts to teach object-oriented programming, making it more engaging than abstract examples. The connection between letters and numbers was interesting to implement.
#    Share what you struggled with?
#    I struggled with understanding which methods should be private vs public and how to properly encapsulate the helper functions. Also making sure all numbers reduce correctly to single digits.
#    Think back to a previous assignment how could rewrite it to use Python classes?
#    A previous grade calculator assignment could be rewritten with a Student class that has attributes for name, scores, and methods to calculate averages and letter grades.
#    Share exactly 2 things you learned on this assignment:
#    1. How to use private methods (with double underscore) to hide internal calculations from outside code, just like the BankAccount example.
#    2. How to implement the __str__ method to display object state nicely, making output formatting clean and reusable.

class Numerology:
    """Numerology class that calculates various numbers from a person's name and birth date."""
    
    # Letter to number mapping as a class-level constant (private)
    __LETTER_VALUES = {
        'A': 1, 'J': 1, 'S': 1,
        'B': 2, 'K': 2, 'T': 2,
        'C': 3, 'L': 3, 'U': 3,
        'D': 4, 'M': 4, 'V': 4,
        'E': 5, 'N': 5, 'W': 5,
        'F': 6, 'O': 6, 'X': 6,
        'G': 7, 'P': 7, 'Y': 7,
        'H': 8, 'Q': 8, 'Z': 8,
        'I': 9, 'R': 9
    }
    
    def __init__(self, sName, sDOB):
        """Initialize the Numerology object with name and date of birth."""
        # Store the data as private attributes
        self.__name = sName.strip().upper()
        self.__dob = sDOB.strip()
        
        # Parse the date components
        self.__month, self.__day, self.__year = self.__parse_date()
        
        # Initialize calculated values as None (will be computed when needed)
        self.__attitude = None
        self.__birthday = None
        self.__life_path = None
        self.__soul = None
        self.__personality = None
        self.__power_name = None
    
    def __parse_date(self):
        """Private method to parse and return month, day, year as integers."""
        if '-' in self.__dob:
            parts = self.__dob.split('-')
        else:
            parts = self.__dob.split('/')
        
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        
        return month, day, year
    
    def __reduce_to_single_digit(self, number):
        """Private method to reduce a number to a single digit (1-9)."""
        while number > 9:
            total = 0
            for digit in str(number):
                total += int(digit)
            number = total
        return number
    
    def __get_letter_value(self, char):
        """Private method to get the numerological value of a letter."""
        if char.isalpha() and char in self.__LETTER_VALUES:
            return self.__LETTER_VALUES[char]
        return 0
    
    def __is_vowel(self, char):
        """Private method to check if a character is a vowel."""
        vowels = 'AEIOU'
        return char in vowels
    
    # Public accessor methods (getters)
    def getName(self):
        """Return the subject's name."""
        return self.__name
    
    def getBirthdate(self):
        """Return the subject's date of birth."""
        return self.__dob
    
    def getAttitude(self):
        """Return the computed attitude number."""
        if self.__attitude is None:
            # Add month and day digits (no year)
            # Convert month to string and add its digits
            month_str = str(self.__month)
            month_sum = 0
            for digit in month_str:
                month_sum += int(digit)
            
            # Convert day to string and add its digits
            day_str = str(self.__day)
            day_sum = 0
            for digit in day_str:
                day_sum += int(digit)
            
            attitude_sum = month_sum + day_sum
            self.__attitude = self.__reduce_to_single_digit(attitude_sum)
        return self.__attitude
    
    def getBirthDay(self):
        """Return the computed birthday number."""
        if self.__birthday is None:
            # Reduce the day to a single digit
            day_str = str(self.__day)
            day_sum = 0
            for digit in day_str:
                day_sum += int(digit)
            self.__birthday = self.__reduce_to_single_digit(day_sum)
        return self.__birthday
    
    def getLifePath(self):
        """Return the computed life path number."""
        if self.__life_path is None:
            # Sum all digits in the birth date
            total = 0
            
            # Add month digits
            month_str = str(self.__month)
            for digit in month_str:
                total += int(digit)
            
            # Add day digits
            day_str = str(self.__day)
            for digit in day_str:
                total += int(digit)
            
            # Add year digits
            year_str = str(self.__year)
            for digit in year_str:
                total += int(digit)
            
            self.__life_path = self.__reduce_to_single_digit(total)
        return self.__life_path
    
    def getSoul(self):
        """Return the computed soul number (vowels only)."""
        if self.__soul is None:
            total = 0
            for char in self.__name:
                if char.isalpha() and self.__is_vowel(char):
                    total += self.__get_letter_value(char)
            if total > 0:
                self.__soul = self.__reduce_to_single_digit(total)
            else:
                self.__soul = 0
        return self.__soul
    
    def getPersonality(self):
        """Return the computed personality number (consonants only)."""
        if self.__personality is None:
            total = 0
            for char in self.__name:
                if char.isalpha() and not self.__is_vowel(char):
                    total += self.__get_letter_value(char)
            if total > 0:
                self.__personality = self.__reduce_to_single_digit(total)
            else:
                self.__personality = 0
        return self.__personality
    
    def getPowerName(self):
        """Return the computed power name number."""
        if self.__power_name is None:
            soul = self.getSoul()
            personality = self.getPersonality()
            total = soul + personality
            self.__power_name = self.__reduce_to_single_digit(total)
        return self.__power_name
    
    def __str__(self):
        """
        Return a string representation of the Numerology object.
        Like the BankAccount example's __str__ method.
        """
        # Calculate all numbers first (they'll be cached)
        life_path = self.getLifePath()
        attitude = self.getAttitude()
        birthday = self.getBirthDay()
        personality = self.getPersonality()
        power_name = self.getPowerName()
        soul = self.getSoul()
        
        # Create a nicely formatted string (like the sample output)
        result = "\n" + "=" * 50 + "\n"
        result += "NUMEROLOGY READING RESULTS\n"
        result += "=" * 50 + "\n"
        result += f"Client Name: {self.__name}\n"
        result += f"Client DOB:  {self.__dob}\n"
        result += "-" * 50 + "\n"
        result += f"Life Path:     {life_path}\n"
        result += f"Attitude:      {attitude}\n"
        result += f"Birthday:      {birthday}\n"
        result += f"Personality:   {personality}\n"
        result += f"Power Name:    {power_name}\n"
        result += f"Soul:          {soul}\n"
        result += "=" * 50
        
        return result
