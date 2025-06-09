class Solution {
    public int characterReplacement(String s, int k) {
        int[] charCount = new int[26]; // Array to store frequency of each character
        int maxLength = 0;
        int maxCount = 0; // Most frequent character in current window
        int start = 0;
        
        for (int end = 0; end < s.length(); end++) {
            charCount[s.charAt(end) - 'A']++;
            maxCount = Math.max(maxCount, charCount[s.charAt(end) - 'A']);
            
            // If window size - maxCount > k, we need to shrink the window
            while (end - start + 1 - maxCount > k) {
                charCount[s.charAt(start) - 'A']--;
                start++;
            }
            
            maxLength = Math.max(maxLength, end - start + 1);
        }
        
        return maxLength;
    }
}
