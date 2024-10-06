from matrix_operations import MatrixOperations
from sparse_matrix import SparseMatrix


def main():
    print("Sparse Matrix Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Select operation (1/2/3): ").strip()

    # Predefined paths for the matrix files
    matrix_file_1 = "/home/kerie/Documents/school-work/SparseMatrix/sample_input_for_students/test_file_1.txt"  
    matrix_file_2 = "/home/kerie/Documents/school-work/SparseMatrix/sample_input_for_students/test_file_2.txt"  
    result_file = "/home/kerie/Documents/school-work/SparseMatrix/sample_input_for_students/easy_sample_result.txt"  

    try:
        print(f"Loading matrix A from {matrix_file_1}...")
        matrix_a = SparseMatrix(matrix_file_1)
        print(f"Matrix A loaded successfully: {matrix_a}")

        print(f"Loading matrix B from {matrix_file_2}...")
        matrix_b = SparseMatrix(matrix_file_2)
        print(f"Matrix B loaded successfully: {matrix_b}")

        ops = MatrixOperations()  # Create an instance of MatrixOperations

        # Perform the chosen operation
        if choice == '1':
            print("Performing addition of two matrices...")
            result = ops.add(matrix_a, matrix_b)
            print("Addition result:\n", result)
        elif choice == '2':
            print("Performing subtraction of two matrices...")
            result = ops.subtract(matrix_a, matrix_b)
            print("Subtraction result:\n", result)
        elif choice == '3':
            print("Performing multiplication of two matrices...")
            result = ops.multiply(matrix_a, matrix_b)
            print("Multiplication result:\n", result)
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
