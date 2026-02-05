# Name: Zongyu Xie
# Assignment: Planetary Weights Dictionaries

# Reflection:  
# *Share what you liked about this assignment?*  
# I liked how this assignment combined practical programming skills with real-world concepts. 
# It was interesting to see how Python can be used to solve problems related to physics 
# and space exploration while also learning important data structures.
#
# *Share what you struggled with?*  
# I struggled with implementing the pickle functionality correctly and handling the 
# case-insensitive name checking. Making sure that the history feature worked properly 
# with file I/O operations was challenging at first.
#
# *How did you like working with dictionaries and pickling concepts?*  
# I found dictionaries to be very powerful and efficient for organizing data. Pickling 
# was a new concept for me, and I appreciated learning how to persist data between 
# program runs. Both concepts are practical tools that I can use in future projects.
#
# *Share exactly 2 things you learned on this assignment:*  
# 1. How to use dictionaries to efficiently store and retrieve key-value pairs, 
#    especially for organizing related data like planetary gravity factors.
# 2. How to use pickle module for serializing Python objects to files and 
#    restoring them, enabling data persistence across program executions.

import pickle
import os

def main():
    # Create dictionary for planet gravity factors
    dictPlanetFactors = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.12,
        "Pluto": 0.066
    }
    
    # Open pickle file for history - using Zongyu Xie's initials
    sFileName = "zxPlanetaryWeights.db"
    
    try:
        with open(sFileName, 'rb') as f:
            dictPlanetHistory = pickle.load(f)
    except FileNotFoundError:
        dictPlanetHistory = {}
    
    # Ask if user wants to see history
    while True:
        sSeeHistory = input("Would you like to see the history y/n: ")
        
        if sSeeHistory.lower() == 'y':
            if dictPlanetHistory:
                print("\n=== History ===")
                for sNameKey, dictPersonWeights in dictPlanetHistory.items():
                    print(f"\n{sNameKey}, here are your weights on our Solar System's planets.")
                    # Display weights in correct order
                    print(f"Weight on Mercury: " + format(dictPersonWeights["Mercury"], '10.2f'))
                    print(f"Weight on Venus:   " + format(dictPersonWeights["Venus"], '10.2f'))
                    print(f"Weight on our Moon:" + format(dictPersonWeights["Moon"], '10.2f'))
                    print(f"Weight on Mars:    " + format(dictPersonWeights["Mars"], '10.2f'))
                    print(f"Weight on Jupiter: " + format(dictPersonWeights["Jupiter"], '10.2f'))
                    print(f"Weight on Saturn:  " + format(dictPersonWeights["Saturn"], '10.2f'))
                    print(f"Weight on Uranus:  " + format(dictPersonWeights["Uranus"], '10.2f'))
                    print(f"Weight on Neptune: " + format(dictPersonWeights["Neptune"], '10.2f'))
                    print(f"Weight on Pluto:   " + format(dictPersonWeights["Pluto"], '10.2f'))
                print("=" * 20)
            else:
                print("No history available yet.")
            break
        elif sSeeHistory.lower() == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")
    
    # Main calculation loop
    while True:
        print("\n" + "=" * 40)
        
        # Get unique name
        while True:
            sNameInput = input("What is your name (enter key to quit): ")
            
            # Exit if empty input
            if not sNameInput:
                # Save data before exiting
                try:
                    with open(sFileName, 'wb') as f:
                        pickle.dump(dictPlanetHistory, f)
                    print(f"\nData saved to {sFileName}")
                    print("Thank you for using the Planetary Weight Calculator!")
                    return
                except Exception as e:
                    print(f"Error saving data: {e}")
                    return
            
            # Check if name already exists (case insensitive)
            bNameExists = False
            for sNameKey in dictPlanetHistory.keys():
                if sNameKey.lower() == sNameInput.lower():
                    bNameExists = True
                    break
            
            if bNameExists:
                print(f"{sNameInput} is already in the history file. Enter a unique name.")
            else:
                sName = sNameInput
                break
        
        # Get earth weight with validation
        while True:
            try:
                sWeightInput = input("What is your weight: ")
                nEarthWeight = float(sWeightInput)
                
                if nEarthWeight <= 0:
                    print("Weight must be positive. Please try again.")
                    continue
                    
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Calculate weights (using original variable names)
        nWeightMercury = nEarthWeight * dictPlanetFactors["Mercury"]
        nWeightVenus = nEarthWeight * dictPlanetFactors["Venus"]
        nWeightMoon = nEarthWeight * dictPlanetFactors["Moon"]
        nWeightMars = nEarthWeight * dictPlanetFactors["Mars"]
        nWeightJupiter = nEarthWeight * dictPlanetFactors["Jupiter"]
        nWeightSaturn = nEarthWeight * dictPlanetFactors["Saturn"]
        nWeightUranus = nEarthWeight * dictPlanetFactors["Uranus"]
        nWeightNeptune = nEarthWeight * dictPlanetFactors["Neptune"]
        nWeightPluto = nEarthWeight * dictPlanetFactors["Pluto"]
        
        # Output results (using original format)
        print(f"\n{sName}, here are your weights on our Solar System's planets:")
        print(f"Weight on Mercury: " + format(nWeightMercury, '10.2f'))
        print(f"Weight on Venus:   " + format(nWeightVenus, '10.2f'))
        print(f"Weight on our Moon:" + format(nWeightMoon, '10.2f'))
        print(f"Weight on Mars:    " + format(nWeightMars, '10.2f'))
        print(f"Weight on Jupiter: " + format(nWeightJupiter, '10.2f'))
        print(f"Weight on Saturn:  " + format(nWeightSaturn, '10.2f'))
        print(f"Weight on Uranus:  " + format(nWeightUranus, '10.2f'))
        print(f"Weight on Neptune: " + format(nWeightNeptune, '10.2f'))
        print(f"Weight on Pluto:   " + format(nWeightPluto, '10.2f'))
        
        # Create person's weight dictionary
        dictPersonWeights = {
            "Mercury": nWeightMercury,
            "Venus": nWeightVenus,
            "Moon": nWeightMoon,
            "Mars": nWeightMars,
            "Jupiter": nWeightJupiter,
            "Saturn": nWeightSaturn,
            "Uranus": nWeightUranus,
            "Neptune": nWeightNeptune,
            "Pluto": nWeightPluto
        }
        
        # Add to history dictionary
        dictPlanetHistory[sName] = dictPersonWeights
        
        print("=" * 40)
        
        # Ask if user wants another calculation
        while True:
            sAnother = input("\nWould you like to perform another calculation? (y/n): ")
            if sAnother.lower() == 'n':
                # Save data before exiting
                try:
                    with open(sFileName, 'wb') as f:
                        pickle.dump(dictPlanetHistory, f)
                    print(f"\nData saved to {sFileName}")
                    print("Thank you for using the Planetary Weight Calculator!")
                    return
                except Exception as e:
                    print(f"Error saving data: {e}")
                    return
            elif sAnother.lower() == 'y':
                break
            else:
                print("Please enter 'y' or 'n'.")

# Call main function
if __name__ == "__main__":
    main()
