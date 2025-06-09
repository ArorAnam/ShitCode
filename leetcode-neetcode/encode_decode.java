import java.util.*;

public class Codec {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String str : strs) {
            // Append length of string, followed by a delimiter '#'
            encoded.append(str.length()).append('#').append(str);
        }
        return encoded.toString();
    }
    

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> decoded = new ArrayList<>();
        int i = 0;
        
        while (i < s.length()) {
            // Find the position of the delimiter '#'
            int delimiterPos = s.indexOf('#', i);
            // Extract the length of the string
            int length = Integer.parseInt(s.substring(i, delimiterPos));
            // Extract the string using the length
            String str = s.substring(delimiterPos + 1, delimiterPos + 1 + length);
            decoded.add(str);
            // Move the pointer to the start of next string
            i = delimiterPos + 1 + length;
        }
        
        return decoded;
    }
}

// Example usage
class Main {
    public static void main(String[] args) {
        Codec codec = new Codec();
        List<String> original = Arrays.asList("Hello", "World", "!");
        
        // Test encoding
        String encoded = codec.encode(original);
        System.out.println("Encoded string: " + encoded);
        
        // Test decoding
        List<String> decoded = codec.decode(encoded);
        System.out.println("Decoded strings: " + decoded);
    }
}
