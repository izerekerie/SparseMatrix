from sparse_matrix import SparseMatrix
from matrix_operations import MatrixOperations

def main():
    print("Sparse Matrix Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Select operation (1/2/3): ").strip()

    # Predefined paths for the matrix files
    matrix_file_1 = "/home/kerie/Documents/school-work/SparseMatrix/sample_input_for_students/easy_sample_03_1.txt"  
    matrix_file_2 = "/home/kerie/Documents/school-work/SparseMatrix/sample_input_for_students/easy_sample_03_2.txt"  
    result_file = "/home/kerie/Documents/school-work/SparseMatrix/sample_input_for_students/easy_sample_result3.txt"  

    try:
        # Initialize the sparse matrices by reading from the predefined file paths
        print(f"Loading matrix A from {matrix_file_1}...")
        matrix_a = SparseMatrix(matrix_file_1)
        print(f"Matrix A loaded successfully: {matrix_a}")

        print(f"Loading matrix B from {matrix_file_2}...")
        matrix_b = SparseMatrix(matrix_file_2)
        print(f"Matrix B loaded successfully: {matrix_b}")

        ops = MatrixOperations()  # Instantiate MatrixOperations without arguments

        # Perform the chosen operation
        if choice == '1':
            print("Performing addition of two matrices...")
            result = ops.add(matrix_a, matrix_b)  # Pass both matrices to the add method
            print("Addition result:", result)
        elif choice == '2':
            print("Performing subtraction of two matrices...")
            result = ops.subtract(matrix_a, matrix_b)  # Pass both matrices to the subtract method
            print("Subtraction result:", result)
        elif choice == '3':
            print("Performing multiplication of two matrices...")
            result = ops.multiply(matrix_a, matrix_b)  # Pass both matrices to the multiply method
            print("Multiplication result:", result)
        else:
            print("Invalid choice! Please select either 1, 2, or 3.")
            return

        # Save the result to the predefined output file path
        with open(result_file, 'w') as file:
            file.write(str(result))  # Assuming SparseMatrix has a __str__ method to represent the matrix as a string
        print(f"Result saved to {result_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
