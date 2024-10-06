from sparse_matrix import SparseMatrix


class MatrixOperations:
    def add(self, matrix_a, matrix_b):
        """
        Perform matrix addition and return the result as a new SparseMatrix.
        Assumes both matrices have the same dimensions.
        """
        if matrix_a.num_rows != matrix_b.num_rows or matrix_a.num_columns != matrix_b.num_columns:
            raise ValueError("Matrices must have the same dimensions for addition.")

        # Initialize the result matrix
        result = SparseMatrix(num_rows=matrix_a.num_rows, num_columns=matrix_a.num_columns)

        # Add elements from the first matrix
        for (row, col), value in matrix_a.elements.items():
            result.set_element(row, col, value)

        # Add elements from the second matrix
        for (row, col), value in matrix_b.elements.items():
            existing_value = result.get_element(row, col)
            result.set_element(row, col, existing_value + value)

        return result

    def subtract(self, matrix_a, matrix_b):
        """
        Perform matrix subtraction and return the result as a new SparseMatrix.
        Assumes both matrices have the same dimensions.
        """
        if matrix_a.num_rows != matrix_b.num_rows or matrix_a.num_columns != matrix_b.num_columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        # Initialize the result matrix
        result = SparseMatrix(num_rows=matrix_a.num_rows, num_columns=matrix_a.num_columns)

        # Add elements from the first matrix
        for (row, col), value in matrix_a.elements.items():
            result.set_element(row, col, value)

        # Subtract elements from the second matrix
        for (row, col), value in matrix_b.elements.items():
            existing_value = result.get_element(row, col)
            result.set_element(row, col, existing_value - value)

        return result

    def multiply(self, matrix_a, matrix_b):
        """
        Perform matrix multiplication and return the result as a new SparseMatrix.
        The number of columns in the first matrix must equal the number of rows in the second matrix.
        """
        if matrix_a.num_columns != matrix_b.num_rows:
            raise ValueError("Matrix dimensions are incompatible for multiplication.")

        # Initialize the result matrix
        result = SparseMatrix(num_rows=matrix_a.num_rows, num_columns=matrix_b.num_columns)

        # Perform multiplication
        for (row_a, col_a), value_a in matrix_a.elements.items():
            for (row_b, col_b), value_b in matrix_b.elements.items():
                if col_a == row_b:
                    # Multiply corresponding elements and add to the result matrix
                    existing_value = result.get_element(row_a, col_b)
                    result.set_element(row_a, col_b, existing_value + value_a * value_b)

        return result
