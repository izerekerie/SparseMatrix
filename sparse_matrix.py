class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.next = None


class RowList:
    def __init__(self, row_index):
        self.row_index = row_index
        self.first = None
        self.next = None


class SparseMatrix:
    def __init__(self, matrix_file_path=None):
        self.first_row = None
        self.row_pointers = {}  # Dictionary to store quick access to rows
        self.num_rows = 0
        self.num_columns = 0

        if matrix_file_path:
            self._read_matrix_from_file(matrix_file_path)

    def _read_matrix_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                # Read header information
                rows_line = file.readline().strip()
                cols_line = file.readline().strip()

                if not rows_line.startswith("rows=") or not cols_line.startswith("cols="):
                    raise ValueError("Invalid file format: Missing rows or columns declaration")

                self.num_rows = int(rows_line.split('=')[1])
                self.num_columns = int(cols_line.split('=')[1])
                print(f"Reading matrix with {self.num_rows} rows and {self.num_columns} columns.")

                # Read all elements
                for line in file:
                    if line.strip():  # Skip empty lines
                        try:
                            # Remove parentheses and split by comma
                            values = line.strip()[1:-1].split(',')
                            if len(values) != 3:
                                raise ValueError(f"Invalid line format: {line.strip()}")
                            row, col, value = map(int, values)
                            if value != 0:  # Only store non-zero values
                                self.set_element(row, col, value)
                        except ValueError as ve:
                            print(f"Error parsing line: {line.strip()} - {ve}")

                print("Matrix loading completed.")

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred while reading the matrix file: {e}")

    def set_element(self, row, col, value):
        if value == 0:
            return

        # Check if the row already exists
        if row in self.row_pointers:
            current_row = self.row_pointers[row]
        else:
            # Create a new row
            new_row = RowList(row)
            self.row_pointers[row] = new_row

            # Insert new row in sorted order
            if self.first_row is None or self.first_row.row_index > row:
                new_row.next = self.first_row
                self.first_row = new_row
            else:
                current = self.first_row
                while current.next and current.next.row_index < row:
                    current = current.next
                new_row.next = current.next
                current.next = new_row
            current_row = new_row

        # Insert the element into the row's linked list
        new_node = Node(row, col, value)
        if current_row.first is None or current_row.first.col > col:
            new_node.next = current_row.first
            current_row.first = new_node
            return

        current = current_row.first
        while current.next and current.next.col < col:
            current = current.next

        if current.next and current.next.col == col:
            current.next.value = value  # Update existing value
        else:
            new_node.next = current.next
            current.next = new_node

    def get_element(self, row, col):
        if row in self.row_pointers:
            current = self.row_pointers[row].first
            while current and current.col <= col:
                if current.col == col:
                    return current.value
                current = current.next
        return 0

    def __str__(self):
        result = f"rows={self.num_rows}\ncols={self.num_columns}\n"
        current_row = self.first_row
        while current_row:
            current = current_row.first
            while current:
                result += f"({current.row},{current.col},{current.value})\n"
                current = current.next
            current_row = current_row.next
        return result
