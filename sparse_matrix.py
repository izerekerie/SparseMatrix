class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=0, num_columns=0):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.elements = {}  # Dictionary to store non-zero elements

        if matrix_file_path:
            self.num_rows, self.num_columns = self._read_matrix_from_file(matrix_file_path)

    def _read_matrix_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                rows = int(file.readline().strip().split('=')[1])
                columns = int(file.readline().strip().split('=')[1])

                for line in file:
                    if line.strip():
                        try:
                            row, column, value = map(int, line.strip()[1:-1].split(','))
                            self.set_element(row, column, value)
                        except ValueError:
                            raise ValueError("Input file has wrong format")
        except Exception as exception:
            raise exception
        
        return rows, columns

    def set_element(self, row, column, value):
        if value != 0:
            self.elements[(row, column)] = value  # Store value in dictionary

    def get_element(self, row, column):
        return self.elements.get((row, column), 0)  # Return 0 if the element is not found

    def __str__(self):
        result = f"Rows: {self.num_rows}, Columns: {self.num_columns}\n"
        for (row, column), value in self.elements.items():
            result += f"({row}, {column}, {value})\n"
        return result
