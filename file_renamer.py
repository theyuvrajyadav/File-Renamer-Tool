import os
import datetime
import sys

def rename_files_in_folder(folder_path):
    """Rename all files in the given folder by adding timestamp and replacing spaces with underscores."""
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Error: The folder '{folder_path}' does not exist.")
            return False
        
        # Check if the path is a directory
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a directory.")
            return False
        
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Counter for renamed files
        renamed_count = 0
        
        # Iterate through all files in the directory
        for filename in os.listdir(folder_path):
            # Get the full path of the file
            file_path = os.path.join(folder_path, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
            
            try:
                # Split the filename and extension
                name, extension = os.path.splitext(filename)
                
                # Replace spaces with underscores
                name = name.replace(" ", "_")
                
                # Create new filename with timestamp
                new_filename = f"{name}_{timestamp}{extension}"
                
                # Create the new file path
                new_file_path = os.path.join(folder_path, new_filename)
                
                # Rename the file
                os.rename(file_path, new_file_path)
                
                # Log the renamed file
                print(f"Renamed: '{filename}' -> '{new_filename}'")
                
                renamed_count += 1
                
            except Exception as e:
                print(f"Error renaming '{filename}': {str(e)}")
        
        # Print summary
        print(f"\nRenaming complete. {renamed_count} file(s) renamed.")
        return True
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    print("File Renamer Tool")
    print("=================\n")
    
    # Get folder path from user
    folder_path = input("Enter the folder path to rename files: ").strip()
    
    # Remove quotes if the user included them
    if (folder_path.startswith('"') and folder_path.endswith('"')) or \
       (folder_path.startswith('\'') and folder_path.endswith('\'')):
        folder_path = folder_path[1:-1]
    
    # Rename files
    success = rename_files_in_folder(folder_path)
    
    if success:
        print("\nThank you for using File Renamer Tool!")
    else:
        print("\nFile renaming operation failed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
    
    # Wait for user input before closing
    input("\nPress Enter to exit...")