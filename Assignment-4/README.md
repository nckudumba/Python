# Assignment-4

## Task 1 – Read a File and Handle Errors
- The program attempts to open a text file named `sample.txt`.
- If the file exists:
  - It prints `"Reading file content:"`.
  - The file content is displayed line by line with line numbers using `enumerate()`.
- If the file does not exist:
  - The error is handled gracefully with a `try-except` block.
  - A message `"Error: The file 'sample.txt' was not found."` is displayed.
- The `with open()` statement is used to ensure the file is properly closed after reading.

## Task 2 – Write and Append Data to a File
- The user is prompted to enter text input.
- The entered text is written to a file named `output.txt`.
- The user is then prompted to enter additional text.
- The additional text is appended to the same file using append mode (`"a"`).
- Finally, the program opens `output.txt` in read mode and displays the complete content.
- File handling ensures that:
  - Old content is overwritten when writing.
  - New content is preserved when appending.