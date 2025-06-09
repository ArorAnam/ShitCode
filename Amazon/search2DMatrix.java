public class search2DMatrix {
    // Brute Force Solution
    // Time Complexity: O(m * n)
    // Space Complexity: O(1)
    public boolean searchMatrixBruteForce(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == target) {
                    return true;
                }
            }
        }
        return false;
    }
    
    // Optimized Solution
    // Time Complexity: O(log(m * n))
    // Space Complexity: O(1)
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        int left = 0;
        int right = m * n - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int row = mid / n;
            int col = mid % n;
            
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
    
    public static void main(String[] args) {
        search2DMatrix solution = new search2DMatrix();
        
        // Test case 1
        int[][] matrix1 = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        int target1 = 3;
        System.out.println("Test case 1:");
        System.out.println("Brute Force: " + solution.searchMatrixBruteForce(matrix1, target1));
        System.out.println("Optimized: " + solution.searchMatrix(matrix1, target1));
        
        // Test case 2
        int[][] matrix2 = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        int target2 = 13;
        System.out.println("\nTest case 2:");
        System.out.println("Brute Force: " + solution.searchMatrixBruteForce(matrix2, target2));
        System.out.println("Optimized: " + solution.searchMatrix(matrix2, target2));
    }
}
