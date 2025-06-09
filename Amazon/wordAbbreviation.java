class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i = 0; // pointer for word
        int j = 0; // pointer for abbr
        
        while (i < word.length() && j < abbr.length()) {
            // Basic character matching
            if (word.charAt(i) != abbr.charAt(j)) {
                return false;
            }
            i++;
            j++;
        }
        return i == word.length() && j == abbr.length();
    }
}
