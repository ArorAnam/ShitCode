/*
Approach
Here’s how we can solve the problem step by step:

Start by skipping any leading spaces in the input string.
Check if there’s a sign (+/-) at the current position. If yes, remember it and move to the next character.
Loop through the string from the current position to process each character:
If the character is a digit (0–9), convert it to a number and add it to our result (num).
Be careful not to exceed the maximum allowed integer value (INT_MAX) to prevent overflow. If num becomes too large, return INT_MAX or INT_MIN depending on the sign.
Update num by multiplying it by 10 and adding the digit’s value.
If the character is not a digit, break out of the loop.
4. Finally, apply the sign to num and return it as a result.


*/
#include <string>
using namespace std;

class Solution {
public:
    int Atoi(std::string s) {
        int num = 0, sign = 1, i = 0;
        
        // Skip leading spaces
        while (i < s.length() && s[i] == ' ')
            i++;

        // Handle the sign
        if (i < s.length() && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        for (; i < s.length(); i++) {
            if (s[i] >= '0' && s[i] <= '9') {
                if (num > INT_MAX / 10 || (num == INT_MAX / 10 && s[i] - '0' > 7)) {
                    return (sign == 1) ? INT_MAX : INT_MIN;
                }
                num = num * 10 + (s[i] - '0');
            } else {
                break;
            }
        }
        
        num = num * sign;
        return num;
    }
}