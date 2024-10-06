from sparse_matrix import SparseMatrix


class MatrixOperations:
    def add(self, matrix_a, matrix_b):
        if matrix_a.num_rows != matrix_b.num_rows or matrix_a.num_columns != matrix_b.num_columns:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = SparseMatrix()  # Create an empty SparseMatrix
        
        # Process both matrices row by row
        row_a = matrix_a.first_row
        row_b = matrix_b.first_row
        
        while row_a is not None or row_b is not None:
            if row_b is None or (row_a is not None and row_a.row_index < row_b.row_index):
                # Copy row from matrix_a
                self._copy_row(result, row_a)
                row_a = row_a.next
            elif row_a is None or row_a.row_index > row_b.row_index:
                # Copy row from matrix_b
                self._copy_row(result, row_b)
                row_b = row_b.next
            else:
                # Add corresponding rows
                self._add_rows(result, row_a, row_b)
                row_a = row_a.next
                row_b = row_b.next
        
        return result

    def subtract(self, matrix_a, matrix_b):
        if matrix_a.num_rows != matrix_b.num_rows or matrix_a.num_columns != matrix_b.num_columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        
        result = SparseMatrix()  # Create an empty SparseMatrix
        
        # Process both matrices row by row
        row_a = matrix_a.first_row
        row_b = matrix_b.first_row
        
        while row_a is not None or row_b is not None:
            if row_b is None or (row_a is not None and row_a.row_index < row_b.row_index):
                # Copy row from matrix_a
                self._copy_row(result, row_a)
                row_a = row_a.next
            elif row_a is None or row_a.row_index > row_b.row_index:
                # Copy negative of row from matrix_b
                self._copy_row_negative(result, row_b)
                row_b = row_b.next
            else:
                # Subtract corresponding rows
                self._subtract_rows(result, row_a, row_b)
                row_a = row_a.next
                row_b = row_b.next
        
        return result

    # def multiply(self, matrix_a, matrix_b):
    #     if matrix_a.num_columns != matrix_b.num_rows:
    #         raise ValueError("Matrix dimensions are incompatible for multiplication.")
        
    #     result = SparseMatrix()  # Create an empty SparseMatrix
        
    #     row_a = matrix_a.first_row
    #     while row_a is not None:
    #         row_b = matrix_b.first_row
    #         while row_b is not None:
    #             # Multiply corresponding elements and add to result
    #             self._multiply_row_col(result, row_a, row_b)
    #             row_b = row_b.next
    #         row_a = row_a.next
        
    #     return result

    def _copy_row(self, result, row):
        current = row.first
        while current is not None:
            result.set_element(row.row_index, current.col, current.value)
            current = current.next

    def _copy_row_negative(self, result, row):
        current = row.first
        while current is not None:
            result.set_element(row.row_index, current.col, -current.value)
            current = current.next

    def _add_rows(self, result, row_a, row_b):
        node_a = row_a.first
        node_b = row_b.first
        
        while node_a is not None or node_b is not None:
            if node_b is None or (node_a is not None and node_a.col < node_b.col):
                result.set_element(row_a.row_index, node_a.col, node_a.value)
                node_a = node_a.next
            elif node_a is None or node_a.col > node_b.col:
                result.set_element(row_a.row_index, node_b.col, node_b.value)
                node_b = node_b.next
            else:
                sum_value = node_a.value + node_b.value
                if sum_value != 0:
                    result.set_element(row_a.row_index, node_a.col, sum_value)
                node_a = node_a.next
                node_b = node_b.next

    def _subtract_rows(self, result, row_a, row_b):
        node_a = row_a.first
        node_b = row_b.first
        
        while node_a is not None or node_b is not None:
            if node_b is None or (node_a is not None and node_a.col < node_b.col):
                result.set_element(row_a.row_index, node_a.col, node_a.value)
                node_a = node_a.next
            elif node_a is None or node_a.col > node_b.col:
                result.set_element(row_a.row_index, node_b.col, -node_b.value)
                node_b = node_b.next
            else:
                diff_value = node_a.value - node_b.value
                if diff_value != 0:
                    result.set_element(row_a.row_index, node_a.col, diff_value)
                node_a = node_a.next
                node_b = node_b.next

    # def _multiply_row_col(self, result, row_a, row_b):
    #     node_a = row_a.first
    #     while node_a is not None:
    #         node_b = row_b.first
    #         while node_b is not None:
    #             if node_a.col == row_b.row_index:
    #                 product = node_a.value * node_b.value
    #                 current_value = result.get_element(row_a.row_index, node_b.col)
    #                 result.set_element(row_a.row_index, node_b.col, current_value + product)
    #             node_b = node_b.next
    #         node_a = node_a.next

    # Other methods...

    def _multiply_row_col(self, result, row_a, row_b):
        node_a = row_a.first
        while node_a is not None:  # Traverse row A
            node_b = row_b.first
            while node_b is not None:  # Traverse row B
                if node_a.col == node_b.row_index:  # Check column of node_a with row index of node_b
                    # Calculate the product
                    product = node_a.value * node_b.value
                    
                    # Update the result matrix
                    current_value = result.get_element(row_a.row_index, node_b.col)
                    result.set_element(row_a.row_index, node_b.col, current_value + product)
                    
                node_b = node_b.next  # Move to the next column in row B
            node_a = node_a.next  # Move to the next column in row A

    def multiply(self, matrix_a, matrix_b):
        if matrix_a.num_columns != matrix_b.num_rows:
            raise ValueError("Matrix dimensions are incompatible for multiplication.")
        
        # Create a result SparseMatrix with the correct dimensions
        result = SparseMatrix(matrix_a.num_rows, matrix_b.num_columns)
        
        row_a = matrix_a.first_row
        while row_a is not None:  # Traverse each row in matrix A
            row_b = matrix_b.first_row
            while row_b is not None:  # Traverse each row in matrix B
                # Perform multiplication for the current rows
                self._multiply_row_col(result, row_a, row_b)
                row_b = row_b.next  # Move to the next row in matrix B
            row_a = row_a.next  # Move to the next row in matrix A
        
        return result

