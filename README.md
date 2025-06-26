# Library Management System
name: piyush bohra 
A simple Python-based library management system that allows you to manage books in a digital library. This system provides basic functionality to add, remove, and display books using object-oriented programming concepts.

## Features

- **Book Management**: Create book objects with title, author, and ISBN
- **Library Operations**: Add books, remove books by ISBN, and display all books
- **Object-Oriented Design**: Clean class structure with encapsulation

## Classes

### Book Class
Represents a book with the following attributes:
- `title`: The title of the book
- `author`: The author of the book  
- `isd`: The ISBN (International Standard Book Number) of the book

**Methods:**
- `info()`: Displays the book's title, author, and ISBN

### Library Class
Represents a library that can store multiple books:
- `name`: The name of the library
- `books`: A list to store book objects

**Methods:**
- `add_book(book)`: Adds a book object to the library
- `remove_book(isd1)`: Removes a book from the library using its ISBN
- `display()`: Shows all books currently in the library

## Usage Example

```python
# Create book objects
b1 = book("Physics", "HC Verma", "10000021")
b2 = book("Maths", "S Dey", "2000948575")

# Create a library
l1 = library("digital_library")

# Add books to the library
l1.add_book(b1)
l1.add_book(b2)

# Display all books
l1.display()

# Access book information
b2.author  # Returns "S Dey"
```

## Sample Output

```
AuthorHC Vermais added to your library
AuthorS Deyis added to your library
books in digital_library is
Physics HC Verma 10000021
Maths S Dey 2000948575
```

## Code Structure

```
├── Book Class
│   ├── __init__(title, author, isd)
│   └── info()
└── Library Class
    ├── __init__(name)
    ├── add_book(book)
    ├── remove_book(isd1)
    └── display()
```

## Requirements

- Python 3.x
- No external libraries required

## Installation and Running

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```

3. Run the Python script:
   ```bash
   python library_system.py
   ```

## Known Issues

- The constructor method should be `__init__` instead of `_init_` (missing underscores)
- The `remove_book` method has a bug where it references undefined variable `isd` instead of `isd1`
- String formatting in print statements could be improved for better readability

## Future Enhancements

- Add search functionality by title or author
- Implement book borrowing and returning system
- Add data persistence (save/load from file)
- Include book availability status
- Add input validation for ISBN format

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available under the MIT License.
