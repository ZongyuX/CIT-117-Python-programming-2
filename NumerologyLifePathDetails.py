# Name: Zongyu Xie
# Assignment: Numerology Inheritance
# Code Name: NumerologyLifePathDetails

# Reflection: Share what you liked about this assignment?
#    I liked how this assignment builds on the original Numerology class using inheritance, showing how to extend functionality without modifying existing code. Learning to use properties with the @property decorator made the code more elegant and Pythonic.

# Share what you struggled with?
#    I struggled with understanding how to properly convert the getters to properties while maintaining the inheritance chain. Making sure the parent class methods were still accessible through the child class properties required careful planning.

# In your own words describe how decoration works & how does it help coders write better code?
#    Decoration works by wrapping a function or method with additional functionality using the @ syntax. The @property decorator specifically allows methods to be accessed like attributes, which makes code cleaner and more intuitive. It helps coders write better code by reducing the need for explicit getter/setter method calls, following the principle of encapsulation while maintaining a simple interface.

# Share exactly 2 things you learned on this assignment:
#    1. How to use the @property decorator to convert traditional getter methods into Python properties, making them accessible as attributes.
#    2. How to use a dictionary mapping instead of if/else statements for cleaner, more maintainable conditional logic.

from Numerology import Numerology

class NumerologyLifePathDetails(Numerology):
    """Child class that extends Numerology with property accessors and life path description."""
    
    def __init__(self, name, birthdate):
        """
        Initialize the child class by calling the parent class initializer.
        Important: Must call super().__init__() to properly set up parent attributes.
        """
        # Call the parent class initializer
        super().__init__(name, birthdate)
    
    # Convert getName to property
    @property
    def Name(self):
        """Return the subject's name as a property."""
        return self.getName()
    
    # Convert getBirthdate to property
    @property
    def Birthdate(self):
        """Return the subject's date of birth as a property."""
        return self.getBirthdate()
    
    # Convert getAttitude to property
    @property
    def Attitude(self):
        """Return the computed attitude number as a property."""
        return self.getAttitude()
    
    # Convert getBirthDay to property
    @property
    def BirthDay(self):
        """Return the computed birthday number as a property."""
        return self.getBirthDay()
    
    # Convert getLifePath to property
    @property
    def LifePath(self):
        """Return the computed life path number as a property."""
        return self.getLifePath()
    
    # Convert getPersonality to property
    @property
    def Personality(self):
        """Return the computed personality number as a property."""
        return self.getPersonality()
    
    # Convert getPowerName to property
    @property
    def PowerName(self):
        """Return the computed power name number as a property."""
        return self.getPowerName()
    
    # Convert getSoul to property
    @property
    def Soul(self):
        """Return the computed soul number as a property."""
        return self.getSoul()
    
    # Add new property for life path description
    @property
    def LifePathDescription(self):
        """
        Return a description based on the life path number.
        Using dictionary mapping instead of if/else statements for cleaner code.
        """
        life_path_number = self.getLifePath()
        
        # Dictionary mapping for life path descriptions (more Pythonic than if/else)
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        
        # Using dictionary get method with default value
        return descriptions.get(life_path_number, "Unknown life path number")
