import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Create a HashMap to store groups of anagrams
        Map<String, List<String>> anagramGroups = new HashMap<>();
        
        // Iterate through each string in the input array
        for (String str : strs) {
            // Create a character count array for lowercase letters
            int[] charCount = new int[26];
            
            // Count frequency of each character
            for (char c : str.toCharArray()) {
                charCount[c - 'a']++;
            }
            
            // Create a unique key by appending character counts
            StringBuilder keyBuilder = new StringBuilder();
            for (int count : charCount) {
                keyBuilder.append('#').append(count);
            }
            String key = keyBuilder.toString();
            
            // If the key is not in the map, create a new list
            if (!anagramGroups.containsKey(key)) {
                anagramGroups.put(key, new ArrayList<>());
            }
            
            // Add the original string to the corresponding group
            anagramGroups.get(key).add(str);
        }
        
        // Return all groups as a list of lists
        return new ArrayList<>(anagramGroups.values());
    }
}
