import os

## this function takes notes from the user and saves them to a file.
def take_notes():
    ## Getting the file name from the user
    file_name = input("Enter a file name for your notes :\n")
    file_path = file_name + ".txt"
    
    ## Checking if the file already exists
    if os.path.exists(file_path):
        print("File already exists. Appending to existing file.")
        mode = "a"
    else:
        mode = "w"
    
    ## Getting the user's notes
    notes = input("Enter your notes :\n")
    
    ## Saving the notes to the file
    with open(file_path, mode) as f:
        f.write(notes)
    
    print("Notes saved to", file_path)


## allowing the user to view existing notes.
def view_notes():
    ## Getting the file name from the user
    file_name = input("Enter the file name of the notes you want to view :\n")
    file_path = file_name + ".txt"
    
    ## Checking if the file exists
    if os.path.exists(file_path):
        ## Reading the contents of the file
        with open(file_path, "r") as f:
            notes = f.read()
        
        ## Printing the contents of the file
        print("Notes for", file_name, ":\n")
        print(notes)
    else:
        print("File not found.")


## allowing the user to delete existing notes.
def delete_notes():
    ## Getting the file name from the user
    file_name = input("Enter the file name of the notes you want to delete :\n")
    file_path = file_name + ".txt"
    
    ## Checking if the file exists
    if os.path.exists(file_path):
        ## Deleting the file
        os.remove(file_path)
        print(file_path, "has been deleted.")
    else:
        print("File not found.")

        
## Main function
def main():
    while True:
        ## Displaying options to the user
        print("\nOptions:")
        print("1. Take notes")
        print("2. View notes")
        print("3. Delete notes")
        print("4. Exit")
        
        ## Getting the user's choice
        choice = input("\nEnter an option :\n")
        
        ## Taking notes
        if choice == "1":
            take_notes()
        
        ## Viewing notes
        elif choice == "2":
            view_notes()
        
        ## Deleting notes
        elif choice == "3":
            delete_notes()
        
        ## Exiting the program
        elif choice == "4":
            print("Goodbye!")
            break
        
        ## Handling the invalid input
        else:
            print("Invalid option. Please try again.")

## Running the program
main()
