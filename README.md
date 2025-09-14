# File Renamer Tool

A simple Python utility that renames all files in a specified folder by adding timestamps and replacing spaces with underscores.

## Features

- Adds a timestamp at the end of each file name
- Replaces spaces with underscores in file names
- Works with all file types (images, documents, etc.)
- Includes error handling
- Logs all renamed files

## Requirements

- Python 3.x

## Usage

1. Run the script:
   ```
   python file_renamer.py
   ```

2. When prompted, enter the path to the folder containing the files you want to rename.

3. The script will rename all files in the folder and display a log of the renamed files.

## Example

If you have a file named `my document.txt` in the specified folder, it will be renamed to something like `my_document_20230815_142536.txt` (where `20230815_142536` is the current timestamp).

## Notes

- The script does not rename subfolders or files within subfolders.
- The original file extension is preserved.
- The script will ask for confirmation before exiting.