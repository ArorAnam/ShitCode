import java.util.HashMap;
import java.util.Map;
import java.util.HashSet;
import java.util.Set;

public class longestWithoutRepeating {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        
        Map<Character, Integer> charMap = new HashMap<>();
        int maxLength = 0;
        int start = 0;
        
        for (int end = 0; end < s.length(); end++) {
            char currentChar = s.charAt(end);
            
            // If we find a repeating character, update the start pointer
            if (charMap.containsKey(currentChar)) {
                // Take the maximum of current start and the position after the last occurrence
                start = Math.max(start, charMap.get(currentChar) + 1);
            }
            
            // Update the character's position in the map
            charMap.put(currentChar, end);
            
            // Update maxLength if current window is larger
            maxLength = Math.max(maxLength, end - start + 1);
        }
        
        return maxLength;
    }

    public int lengthOfLongestSubstringBruteForce(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }
        
        int maxLength = 0;
        
        // Try all possible starting positions
        for (int start = 0; start < s.length(); start++) {
            // Try all possible ending positions
            for (int end = start; end < s.length(); end++) {
                // Check if current substring has all unique characters
                if (hasUniqueCharacters(s, start, end)) {
                    maxLength = Math.max(maxLength, end - start + 1);
                }
            }
        }
        
        return maxLength;
    }
    
    private boolean hasUniqueCharacters(String s, int start, int end) {
        Set<Character> seen = new HashSet<>();
        
        for (int i = start; i <= end; i++) {
            char currentChar = s.charAt(i);
            if (seen.contains(currentChar)) {
                return false;
            }
            seen.add(currentChar);
        }
        
        return true;
    }
}
