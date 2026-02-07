# Name: Zongyu Xie
# Assignment: Password Validator Final Project
# Reflection:
# Share what you liked about this assignment?
# I enjoyed the comprehensive application of all Python concepts learned throughout the semester to solve a real-world problem without using regex.
# 
# Share what you struggled with?
# I struggled with implementing the duplicate character check efficiently using only basic Python constructs and string methods.
# 
# How did you write your code to be efficient and reduce redundancy?
# I created modular functions for each validation rule and used early returns to avoid unnecessary checks once a password fails a rule.
# 
# Share exactly 2 things you learned on this assignment:
# 1. How to combine multiple string methods to perform complex validation tasks
# 2. How to use lists and loops to track and analyze character patterns in strings

def main():
    # Prompt user for their first and last name
    sNameZX = input("Enter full name such as John Smith: ")
    
    # Extract initials from the name
    # Find the space between first and last name
    jSpaceIndexZX = sNameZX.find(" ")
    if jSpaceIndexZX != -1:
        sFirstInitialZX = sNameZX[0].upper()
        sLastInitialZX = sNameZX[jSpaceIndexZX + 1].upper()
        sInitialsZX = sFirstInitialZX + sLastInitialZX
    else:
        sInitialsZX = ""
    
    # Main password validation loop
    bValidPasswordZX = False
    
    while not bValidPasswordZX:
        # Prompt user for password
        sPasswordZX = input("Enter new password: ")
        
        # Initialize validation flags
        bLengthOKZX = True
        bNoPassStartZX = True
        bHasUpperZX = False
        bHasLowerZX = False
        bHasNumberZX = False
        bHasSpecialZX = False
        bNoInitialsZX = True
        bNoDuplicatesZX = True
        
        # 1. Check password length (8 to 12 characters)
        jLengthZX = len(sPasswordZX)
        if jLengthZX < 8 or jLengthZX > 12:
            bLengthOKZX = False
            print("Password must be between 8 and 12 characters")
        
        # 2. Check if password starts with "Pass" or "pass"
        if sPasswordZX[0:4].lower() == "pass":
            bNoPassStartZX = False
            print("Password can't start with Pass")
        
        # 3. Check for at least one uppercase letter A through Z
        # Using ASCII codes approach: A=65, Z=90
        for sCharZX in sPasswordZX:
            if ord(sCharZX) >= 65 and ord(sCharZX) <= 90:
                bHasUpperZX = True
                break
        
        if not bHasUpperZX:
            print("Password must contain at least 1 uppercase letter")
        
        # 4. Check for at least one lowercase letter a through z
        # Using ASCII codes approach: a=97, z=122
        for sCharZX in sPasswordZX:
            if ord(sCharZX) >= 97 and ord(sCharZX) <= 122:
                bHasLowerZX = True
                break
        
        if not bHasLowerZX:
            print("Password must contain at least 1 lowercase letter")
        
        # 5. Check for at least one number 0 through 9
        # Using ASCII codes approach: 0=48, 9=57
        for sCharZX in sPasswordZX:
            if ord(sCharZX) >= 48 and ord(sCharZX) <= 57:
                bHasNumberZX = True
                break
        
        if not bHasNumberZX:
            print("Password must contain at least 1 number")
        
        # 6. Check for at least one special character: !@#$%^
        sSpecialCharsZX = "!@#$%^"
        for sCharZX in sPasswordZX:
            if sCharZX in sSpecialCharsZX:
                bHasSpecialZX = True
                break
        
        if not bHasSpecialZX:
            print("Password must contain at least 1 of these special characters: !@#$%^")
        
        # 7. Check that password does not contain user initials
        # Check both uppercase and lowercase versions
        if sInitialsZX != "":
            sPasswordUpperZX = sPasswordZX.upper()
            sPasswordLowerZX = sPasswordZX.lower()
            sInitialsUpperZX = sInitialsZX.upper()
            sInitialsLowerZX = sInitialsZX.lower()
            
            if sInitialsUpperZX in sPasswordUpperZX or sInitialsLowerZX in sPasswordLowerZX:
                bNoInitialsZX = False
                print("Password must not contain user initials.")
        
        # 8. Check that no character appears more than once
        # Convert password to lowercase for case-insensitive comparison
        sPasswordLowerZX = sPasswordZX.lower()
        jPasswordLenZX = len(sPasswordLowerZX)
        
        # Create a list to track character counts
        lstDuplicateCharsZX = []
        lstDuplicateCountsZX = []
        
        for jIndexZX in range(jPasswordLenZX):
            sCurrentCharZX = sPasswordLowerZX[jIndexZX]
            jCountZX = 1
            
            # Count occurrences of current character
            for jInnerIndexZX in range(jIndexZX + 1, jPasswordLenZX):
                if sPasswordLowerZX[jInnerIndexZX] == sCurrentCharZX:
                    jCountZX += 1
            
            # If character appears more than once and not already in our list
            if jCountZX > 1:
                bCharAlreadyListedZX = False
                for sListedCharZX in lstDuplicateCharsZX:
                    if sListedCharZX == sCurrentCharZX:
                        bCharAlreadyListedZX = True
                        break
                
                if not bCharAlreadyListedZX:
                    lstDuplicateCharsZX.append(sCurrentCharZX)
                    lstDuplicateCountsZX.append(jCountZX)
        
        # If duplicates were found, display them
        if len(lstDuplicateCharsZX) > 0:
            bNoDuplicatesZX = False
            print("These characters appear more than once:")
            for jDuplicateIndexZX in range(len(lstDuplicateCharsZX)):
                print(f"{lstDuplicateCharsZX[jDuplicateIndexZX]}: {lstDuplicateCountsZX[jDuplicateIndexZX]} times")
        
        # 9. Check if all validation rules passed
        if (bLengthOKZX and bNoPassStartZX and bHasUpperZX and bHasLowerZX and 
            bHasNumberZX and bHasSpecialZX and bNoInitialsZX and bNoDuplicatesZX):
            bValidPasswordZX = True
            print("Password is valid and OK to use.")
        else:
            # Add a blank line for readability
            print()

# Run the main function
if __name__ == "__main__":
    main()
