print("                       PROGRAM FOR DATA BASE MANAGEMENT SYSTEM                        ")
import csv   #Enables to interact with the csv files,making it easier to read,write and format the data stored
import os    #This module provide ways to interact with the operating system

# Function to create a new database file with specified fields
def create_database():
    db_name = input("-> Enter the name for the new database: ") + ".csv" #appends the database name with .csv
    print("-" * 100) #print a separator line

    # Prompt for number of fields with validation
    while True:
        try:
            fields = int(input("->  Enter the number of fields: ")) #ask user for the number of fields in the database
            break # Exit the loop if a valid number is entered
        except ValueError:
            print("! Please enter a valid integer.") # Handle the case where the user enters something other than an integer


    # Gather field names and save to the CSV file
    field_names = []  # Initialize an empty list to store the field names
    for i in range(fields):
        field_name = input(f"-> Enter name of field {i + 1}: ") # Ask user to enter field names
        field_names.append(field_name) # Add the field name to the lis

    # Write headers to the CSV file
    with open(db_name, 'w', newline='') as csvfile: # Open the file in write mode (creates a new file
        writer = csv.writer(csvfile) # Create a CSV writer object
        writer.writerow(field_names) # Write the field names as the header row
    
    print(f"\n Database '{db_name}' created successfully.") # Inform the user the database was created
    print("-" * 100) #Again Print a separator line



# Function to open an existing database
def open_database():
    db_name = input("->  Enter the name of the existing database: ") + ".csv" # Ask user for the database name and add .csv extension
    print("-" * 100) #Again Print a separator line

    # Check if the file exists
    if not os.path.exists(db_name):  # If the file does not exist in the system
        print(f"! Database '{db_name}' does not exist.") # Inform the user the database doesn't exist
        return None # Return None if the database doesn't exist
    else:
        print(f" Database '{db_name}' opened.") # Inform the user the database was successfully opened
        return db_name # Return the database name if it exists


# Function to add a record to the database
def add_record(db_name):
    with open(db_name, 'a+', newline='') as csvfile: # Open the database file in append mode to add new records
        csvfile.seek(0)  # Go to the beginning of the file to read header
        reader = csv.reader(csvfile) # Create a CSV reader object

        # Check if the file has a header row
        try:
            fields = next(reader) # Read the header (first row) to get the field names
        except StopIteration: # If the file is empty (no rows), handle the error
            print("! Error: The database has no fields defined. Please create a new database with fields.") #inform the user
            return #Exit the function if no fields are defined

        # Collect data for each field and write to file
        record = [] # Initialize an empty list to store the new record's data
        for field in fields: # Iterate over the field names
            value = input(f"-> Enter value for {field}: ") # Ask user to input a value for each field
            record.append(value)  # Add the value to the record lis

        writer = csv.writer(csvfile) # Create a CSV writer object
        writer.writerow(record) # Write the new record as a new row in the file

    print("\n Record added successfully.") # Inform the user that the record was added
    print("-" * 100) #Again Print a separator line


# Function to delete a record from the database
def delete_field_value(db_name):
    print("\n Current records:")
    display_records(db_name) # Display all records in the database before making any modifications

    # Open and read the CSV file
    with open(db_name, 'r') as csvfile: #here the 'r' is the read mode
        reader = csv.reader(csvfile)
        rows = list(reader) # Read all rows of the CSV into a list

        # Check if there are records other than the header
        if len(rows) <= 1: # If only the header is present, there are no records to modify
            print("! No records to modify.") # Inform the user there are no records
            return # Exit the function if no records exist

    # Display all records for user reference
    field_names = rows[0]  # First row is the header
    print("\n Choose the field to clear the value from:") # Asking the user which field to modify
    for i, field in enumerate(field_names): # Loop through the field names and display them
        print(f"{i + 1}. {field}")

    # Get the field index from user input
    try:
        field_index = int(input("-> Enter the field number: ")) - 1 # Get the field number and adjust the index
        if field_index < 0 or field_index >= len(field_names): # Check if the input is valid
            print("! Invalid field number.")  # Inform the user if the input is invalid
            return # Exit the function if the field number is out of range
    except ValueError: # Handle the case where the input is not a valid integer
        print("! Please enter a valid number.")
        return # Exit the function if the input is invalid

    # Get the value to find the specific record
    record_to_modify = input(f"->  Enter the value of '{field_names[field_index]}' to clear the field value: ")

    temp_file = 'temp.csv' # Define a temporary file to store modified data
    modified = False # Flag to track whether any modification was made

    # Copy data to a temporary file, clearing only the specified field value
    with open(db_name, 'r') as csvfile, open(temp_file, 'w', newline='') as tempfile:
        reader = csv.reader(csvfile) # Read the original database
        writer = csv.writer(tempfile) # Write to the temporary file

        for i, row in enumerate(reader): # Loop through all rows in the database
            if i == 0: # If it's the header row
                # Write header row
                writer.writerow(row)
            else:
                # Check if the current row matches the value in the specified field
                if row[field_index] == record_to_modify:
                    row[field_index] = ''  # Clear the field value
                    modified = True # Set the flag to True indicating a modification
                writer.writerow(row) # Write the row (modified or not) to the temporary file

    # Replace the original file with updated content
    os.replace(temp_file, db_name) # Replace the original database with the temporary file


    if modified:
        print("\n Field value cleared successfully.")  # Inform the user the value was cleared
    else:
        print("\n! No matching record found to modify.") # Inform the user if no matching record was found
    print("-" * 100) #Again Print a separator line


# Function to search for a record in the database
def search_record(db_name):
    search_value = input("-> Enter the value to search: ") # Asking user for the search value
    found = False   # Flag to track if the record is found

    # Read through the file to find matching records
    with open(db_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader: # Loop through each row in the database
            if search_value in row:  # If the search value is found in the row
                print("Record found:", row) # Display the matching record
                found = True # Set the flag to True

    if not found: # If no matching records were found
        print(" ! Record not found.") # Inform the user no record was found
    print("-" * 100) # Printing a separator line


# Function to display all records in the database
def display_records(db_name):
    print("\n Displaying all records:")

    # Read and print all records
    with open(db_name, 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Get all rows and check if there are records beyond the header
        rows = list(reader)  # Read all rows of the CSV file
        if len(rows) <= 1: # If no records are present
            print("! No records to display.") # Informing that there are no record present
        else:
            for row in rows: # Loop through and display each record
                print(row) #printing the row
    print("-" * 100) # Printing a separator line


# Main function to handle user choices and control the whole program!
def main():
    while True: # Infinite loop to keep the menu options active until the user exits
        # Display the main menu options
        print("\n=== Main Menu ===")
        print("1. Create a new database") # Option to create a new database
        print("2. Open an existing database") # Option to open an existing database
        print("3. Exit") # Option to exit the program
        print("=================") #for formatting purpose

        choice = input("-> Enter your choice: ") # Take the user's choice for the main menu

        if choice == "1": # If the user selects option 1, create a new database
            create_database() #used to define a function that creates a new database.
        elif choice == "2": # If the user selects option 2, open an existing database
            db_name = open_database() #used to define a function that opens an existing database assigned to the name db_name
            if db_name: # If the database is successfully opened
                while True:  # Infinite loop for the database menu options until the user exits or goes back
                    # Display the database menu options
                    print("\n=== Database Menu ===")
                    # Option to add a new record to the database
                    print("1. Add a record")
                    # Option to delete a specific record from the database
                    print("2. Delete a record")
                    # Option to search for a specific record in the database
                    print("3. Search a record")
                    # Option to display all records in the database
                    print("4. Display all records")
                    # Option to go back to the main menu
                    print("5. Back to main menu")
                    #for formatting
                    print("=====================")

                    db_choice = input("-> Enter your choice: ")  # Take the user's choice for the database menu

                    if db_choice == "1": # If the user selects option 1, add a record to the database
                        add_record(db_name)
                    elif db_choice == "2": # If the user selects option 2, delete a record from the database
                        delete_field_value(db_name)
                    elif db_choice == "3": # If the user selects option 3, search for a record in the database
                        search_record(db_name)
                    elif db_choice == "4":  # If the user selects option 4, display all records in the database
                        display_records(db_name)
                    elif db_choice == "5": # If the user selects option 5, break the loop and return to the main menu
                        break
                    else:
                        print("! Invalid choice. Try again.")  # If the user inputs an invalid choice in the database menu
        # If the user selects option 3, exit the program
        elif choice == "3":
            print(" Exiting the program.")
            break
        # If the user inputs an invalid choice in the main menu (a wrong number or other)
        else:
            print("! Invalid choice. Try again.")

# Run the main function if the script is executed directly!
if __name__ == "__main__":
    main() #calling main function