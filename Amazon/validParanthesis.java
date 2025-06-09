import java.util.*;

class Solution {
    public String minRemoveToMakeValid(String s) {
        // Convert string to char array for easier manipulation
        char[] arr = s.toCharArray();
        Stack<Integer> stack = new Stack<>();
        
        // First pass: mark invalid parentheses
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '(') {
                stack.push(i);
            } else if (arr[i] == ')') {
                if (stack.isEmpty()) {
                    // Mark invalid closing parenthesis
                    arr[i] = '*';
                } else {
                    stack.pop();
                }
            }
        }
        
        // Mark remaining opening parentheses as invalid
        while (!stack.isEmpty()) {
            arr[stack.pop()] = '*';
        }
        
        // Build result string excluding marked characters
        StringBuilder result = new StringBuilder();
        for (char c : arr) {
            if (c != '*') {
                result.append(c);
            }
        }
        
        return result.toString();
    }
}
