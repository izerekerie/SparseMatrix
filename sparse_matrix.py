class Node:
    """
    A node in the linked list representing a non-zero element in the sparse matrix.
    Each node stores the row, column, and value of the element, as well as a pointer to the next node.
    """
    def __init__(self, row, column, value):
        """
        Initializes a node with the given row, column, and value.
        The 'next' pointer is initialized to None.
        """
        self.row = row  # The row index of the non-zero element
        self.column = column  # The column index of the non-zero element
        self.value = value  # The value of the non-zero element
        self.next = None  # Pointer to the next node (initially None)

class SparseMatrix:
    """
    This class represents a sparse matrix using a linked list. 
    It allows the efficient storage and operations on sparse matrices.
    """
    def __init__(self, matrix_file_path=None, num_rows=0, num_columns=0):
        """
        Initializes the sparse matrix.
        
        If a file path is provided, the matrix is initialized by reading from the file.
        Otherwise, the matrix is initialized with the specified number of rows and columns.
        """
        self.num_rows = num_rows  # The number of rows in the matrix
        self.num_columns = num_columns  # The number of columns in the matrix
        self.head = None  # The head (first node) of the linked list (initially None)
        
        # If a file path is provided, load the matrix from the file
        if matrix_file_path:
            self.num_rows, self.num_columns = self._read_matrix_from_file(matrix_file_path)

    def _read_matrix_from_file(self, file_path):
        """
        Reads the sparse matrix from the given file and stores the non-zero elements in a linked list.
        
        The file should have the following format:
        - First line: number of rows (e.g., 'rows=8433')
        - Second line: number of columns (e.g., 'cols=3180')
        - Subsequent lines: non-zero elements in the format '(row, column, value)'
        
        This function returns the number of rows and columns in the matrix.
        """
        try:
            with open(file_path, 'r') as file:
                # Read the first line to get the number of rows
                first_line = file.readline().strip()  # Read the first line and remove any leading/trailing spaces
                rows = int(first_line.split('=')[1])  # Extract the number of rows after '='
                
                # Read the second line to get the number of columns
                second_line = file.readline().strip()  # Read the second line and remove any leading/trailing spaces
                columns = int(second_line.split('=')[1])  # Extract the number of columns after '='
                
                # Read the subsequent lines to get the non-zero elements
                for line in file:
                    if line.strip():  # Ignore empty lines
                        # Extract the row, column, and value from the line
                        try:
                            row, column, value = map(int, line.strip()[1:-1].split(','))  # Remove parentheses and split the values
                            self._insert_node(row, column, value)  # Insert the non-zero element into the linked list
                        except ValueError:
                            # If the format of the file is incorrect, raise an error
                            raise ValueError("Input file has wrong format")
        except Exception as exception:
            # Rethrow any exceptions that occur while reading the file
            raise exception
        
        # Return the number of rows and columns read from the file
        return rows, columns

    def _insert_node(self, row, column, value):
        """
        Inserts a non-zero element into the linked list in a sorted order.
        
        The linked list is sorted first by row and then by column.
        """
        if value == 0:
            # Do not insert zero values (since it's a sparse matrix)
            return
        
        # Create a new node with the given row, column, and value
        new_node = Node(row, column, value)
        
        # If the list is empty, set the new node as the head of the list
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse the linked list to find the correct position for the new node
        current = self.head  # Start at the head of the list
        previous = None  # Keep track of the previous node during traversal
        
        while current is not None:
            # Check if the new node should be inserted before the current node
            if (row < current.row) or (row == current.row and column < current.column):
                break  # Exit the loop if the correct position is found
            previous = current  # Update the previous node
            current = current.next  # Move to the next node
        
        # Insert the new node into the list
        new_node.next = current  # Set the new node's next pointer to the current node
        if previous is None:
            # If there was no previous node, set the new node as the head of the list
            self.head = new_node
        else:
            # Otherwise, set the previous node's next pointer to the new node
            previous.next = new_node

    def get_element(self, row, column):
        """
        Returns the value of the element at the specified row and column.
        
        If the element is not found in the linked list, it is assumed to be zero.
        """
        current = self.head  # Start at the head of the linked list
        
        # Traverse the list to find the element
        while current is not None:
            if current.row == row and current.column == column:
                # Return the value if the element is found
                return current.value
            current = current.next  # Move to the next node
        
        # If the element is not found, return 0 (since it's a sparse matrix)
        return 0

    def set_element(self, row, column, value):
        """
        Sets the value of the element at the specified row and column.
        
        If the element is not found in the linked list, a new node is inserted.
        If the element is found, its value is updated.
        """
        if value == 0:
            # Do not store zero values (since it's a sparse matrix)
            return
        
        current = self.head  # Start at the head of the linked list
        previous = None  # Keep track of the previous node during traversal
        
        # Traverse the list to find the element
        while current is not None:
            if current.row == row and current.column == column:
                # Update the value if the element is found
                current.value = value
                return
            previous = current  # Update the previous node
            current = current.next  # Move to the next node
        
        # If the element is not found, insert a new node
        self._insert_node(row, column, value)

    def __str__(self):
        """
        Returns a string representation of the sparse matrix.
        The string includes the dimensions and non-zero elements of the matrix.
        """
        result = f"Rows: {self.num_rows}, Columns: {self.num_columns}\n"
        
        current = self.head  # Start at the head of the linked list
        
        # Traverse the list and append each non-zero element to the result string
        while current is not None:
            result += f"({current.row}, {current.column}, {current.value})\n"
            current = current.next  # Move to the next node
        
        return result  # Return the final string
