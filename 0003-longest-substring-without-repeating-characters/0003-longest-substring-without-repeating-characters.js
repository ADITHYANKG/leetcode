/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let charSet = new Set(); // To store unique characters in the current window
    let left = 0; // Left pointer of the window
    let maxLength = 0; // Maximum length of substring without repeating characters

    for (let right = 0; right < s.length; right++) {
        // If the character at `right` is already in the set, shrink the window from the left
        while (charSet.has(s[right])) {
            charSet.delete(s[left]);
            left++;
        }
        // Add the current character to the set and update maxLength
        charSet.add(s[right]);
        maxLength = Math.max(maxLength, right - left + 1);
    }
    
    return maxLength;
};
