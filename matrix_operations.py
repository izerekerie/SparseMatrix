class SparseMatrix:
    # Other functions are assumed to be the same as the earlier explanation
    
    def add(self, other_matrix):
        """
        Perform matrix addition with another sparse matrix and return the result.
        This function assumes that both matrices have the same dimensions.
        """
        # Ensure both matrices have the same dimensions
        if self.num_rows != other_matrix.num_rows or self.num_columns != other_matrix.num_columns:
            raise ValueError("Matrices must have the same dimensions for addition.")

        # Initialize the result matrix with the same dimensions
        result = SparseMatrix(num_rows=self.num_rows, num_columns=self.num_columns)

        # Traverse the first matrix and add all its elements to the result matrix
        current = self.head
        while current:
            result.set_element(current.row, current.column, current.value)
            current = current.next

        # Traverse the second matrix and add its elements to the result matrix
        current = other_matrix.head
        while current:
            # Add the value to the result matrix by retrieving any existing value and adding to it
            existing_value = result.get_element(current.row, current.column)
            new_value = existing_value + current.value
            result.set_element(current.row, current.column, new_value)
            current = current.next

        return result
    def subtract(self, other_matrix):
        """
        Perform matrix subtraction with another sparse matrix and return the result.
        This function assumes that both matrices have the same dimensions.
        """
        # Ensure both matrices have the same dimensions
        if self.num_rows != other_matrix.num_rows or self.num_columns != other_matrix.num_columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        # Initialize the result matrix with the same dimensions
        result = SparseMatrix(num_rows=self.num_rows, num_columns=self.num_columns)

        # Traverse the first matrix and add all its elements to the result matrix
        current = self.head
        while current:
            result.set_element(current.row, current.column, current.value)
            current = current.next

        # Traverse the second matrix and subtract its elements from the result matrix
        current = other_matrix.head
        while current:
            # Subtract the value from the result matrix by retrieving any existing value and subtracting from it
            existing_value = result.get_element(current.row, current.column)
            new_value = existing_value - current.value
            result.set_element(current.row, current.column, new_value)
            current = current.next

        return result
    def multiply(self, other_matrix):
        """
        Perform matrix multiplication with another sparse matrix and return the result.
        For matrix multiplication, the number of columns in the first matrix must match
        the number of rows in the second matrix.
        """
        # Ensure the matrices have compatible dimensions for multiplication
        if self.num_columns != other_matrix.num_rows:
            raise ValueError("The number of columns in the first matrix must equal the number of rows in the second matrix.")

        # Initialize the result matrix with the appropriate dimensions
        result = SparseMatrix(num_rows=self.num_rows, num_columns=other_matrix.num_columns)

        # Traverse the first matrix and perform multiplication
        current = self.head
        while current:
            # For each non-zero element in the first matrix, look for corresponding elements in the second matrix
            other_current = other_matrix.head
            while other_current:
                if current.column == other_current.row:
                    # Perform multiplication: value from the first matrix * value from the second matrix
                    # The result is added to the appropriate position in the result matrix
                    existing_value = result.get_element(current.row, other_current.column)
                    new_value = existing_value + current.value * other_current.value
                    result.set_element(current.row, other_current.column, new_value)
                other_current = other_current.next
            current = current.next

        return result