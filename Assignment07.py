# ------------------------------------------------- #
# Title: Assignment 07
# Description: Create a new script that demonstrates how
#              Pickling and Structured error handling work
# ChangeLog (Who,When,What):
# GFlores,11/20/2019,Modified code to complete assignment 7
# ------------------------------------------------- #
import pickle # Pickle has been added
# Data--------------------------------------------- #
strFileName = 'Toolbox.txt'
strFileName = 'Toolbox.dat'
lstCustomer = []

# Processing--------------------------------------- #
def SaveDataFile(file_name, list_of_data): # Created 11/20/2019
    while (True):
        try:
            intID = int(input("Enter the item ID: "))
        except ValueError as e:
            print("Not a valid integer. Please Enter again.") # Displays an error message when a character is not numeric
            print("Built-in python error info:")
            print(e, e.__doc__, type(e), sep='\n')
        try:
            strName = str(input("Enter the item: "))
            if strName.isnumeric():
                raise Exception('Not a valid entry, this needs to be an item name') # Displays an error message when a character is  numeric
            break
        except Exception as e:
            print("Built-in python error info:")
            print(e, e.__doc__, type(e), sep='\n')
    lstCustomer = [intID, strName]
    objFile = open(file_name, "wb")  # Writing binary
    pickle.dump(lstCustomer, objFile)
    objFile.close() # Always close the file

def ReadDataFile(file_name): # Created 11/20/2019
    objFile = open(file_name, "rb") # Reading binary
    list_of_data = pickle.load(objFile)
    objFile.close() # Always close the file
    return (list_of_data)

# Presentation------------------------------------ #
while (True):
    print("""    
    Menu of Options    
    1) Add and Save Data to File    
    2) Show Current Data    
    3) Exit Program    
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 3] - "))
    print()  # adding a new line for look

    if (strChoice.strip() == '1'):
        SaveDataFile(strFileName, lstCustomer)
        print("Your data has been saved!")
    elif (strChoice.strip() == '2'):
        print(ReadDataFile(strFileName))
    elif (strChoice.strip() == '3'):
        print('Exiting the program')
        break