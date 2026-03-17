# Name: Zongyu Xie
# Assignment: Real Estate Sales Analyzer
# Reflection:
# Share what you liked about this assignment?
# I enjoyed learning how to parse raw string data manually. It gave me a better 
# understanding of how data is structured behind the scenes.
#
# Share what you struggled with?
# I struggled with the specific naming conventions and ensuring the manual 
# median calculation logic exactly matched the assignment requirements.
#
# Which approach did you use to import the data and why did you choose it?
# I used the readlines() method to read the file into a list of strings. I chose 
# this because the instructions explicitly forbade using AI or external libraries 
# for parsing, requiring manual string manipulation instead.
#
# How many dictionaries did you use for this assignment?
# I used 3 dictionaries (City, Zip, and Property Type).
#
# Share exactly 2 things you learned on this assignment:
# 1. How to use string splitting to extract specific data fields from a CSV line.
# 2. How to accumulate totals in dictionaries to create category-based summaries.

def getDataInput():
    # Instruction 3: Read entire file in as strings, skip header
    sFileNameZX = "RealEstateData.csv"
    try:
        with open(sFileNameZX, 'r') as file:
            allLinesZX = file.readlines()
            # Return all records except the first (heading)
            return allLinesZX[1:]
    except FileNotFoundError:
        print("Error: RealEstateData.csv not found.")
        return []

def getMedian(fListZX):
    # Instruction 4: Manual Median Logic
    fListZX.sort()
    iCountZX = len(fListZX)
    
    if iCountZX == 0:
        return 0.0
    
    if iCountZX % 2 == 1:
        # Odd: Use middle entry
        fMedianZX = fListZX[iCountZX // 2]
    else:
        # Even: Average middle two
        iMidZX = iCountZX // 2
        fMedianZX = (fListZX[iMidZX] + fListZX[iMidZX - 1]) / 2
        
    return float(fMedianZX)

def main():
    # Call the input function
    sRecordsListZX = getDataInput()
    
    if not sRecordsListZX:
        return

    # Initialize lists and dictionaries
    fPriceListZX = []
    dictCityZX = {}
    dictZipZX = {}
    dictTypeZX = {}

    # Instruction 5: Loop through records and extract columns
    for sRecordZX in sRecordsListZX:
        # Split string by comma
        sDataZX = sRecordZX.strip().split(',')
        
        if len(sDataZX) >= 9:
            # Extract columns based on assignment description
            sCityZX = sDataZX[1]
            sZipZX = sDataZX[2]
            sTypeZX = sDataZX[7]
            
            try:
                fPriceZX = float(sDataZX[8])
                
                # Add price to list for summary stats
                fPriceListZX.append(fPriceZX)
                
                # Total up prices in dictionaries
                dictCityZX[sCityZX] = dictCityZX.get(sCityZX, 0) + fPriceZX
                dictZipZX[sZipZX] = dictZipZX.get(sZipZX, 0) + fPriceZX
                dictTypeZX[sTypeZX] = dictTypeZX.get(sTypeZX, 0) + fPriceZX
            except ValueError:
                continue

    # Calculate Overall Stats
    fMinZX = min(fPriceListZX)
    fMaxZX = max(fPriceListZX)
    fSumZX = sum(fPriceListZX)
    fAvgZX = fSumZX / len(fPriceListZX)
    fMedZX = getMedian(fPriceListZX)

    # Output 1: Sample Output Style (Matching Screenshot)
    print(f"{'Minimum':<20} {fMinZX:>15,.2f}")
    print(f"{'Maximum':<20} {fMaxZX:>15,.2f}")
    print(f"{'Sum':<20} {fSumZX:>15,.2f}")
    print(f"{'Avg':<20} {fAvgZX:>15,.2f}")
    print(f"{'Median':<20} {fMedZX:>15,.2f}")

    # Output 2: Summary by Property Type
    print("\nSummary by Property Type:")
    for sTypeZX, fTotalZX in dictTypeZX.items():
        print(f"{sTypeZX:<20} {fTotalZX:>15,.2f}")

    # Output 3: Summary by City
    print("\nSummary by City:")
    for sCityZX, fTotalZX in dictCityZX.items():
        print(f"{sCityZX:<20} {fTotalZX:>15,.2f}")

    # Output 4: Summary by Zip
    print("\nSummary by Zip:")
    for sZipZX, fTotalZX in dictZipZX.items():
        print(f"{sZipZX:<20} {fTotalZX:>15,.2f}")

if __name__ == "__main__":
    main()
