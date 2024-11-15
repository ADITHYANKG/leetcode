/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function(s) {


    const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
       let vowelsInString = [];
       let indices = [];
   
       // Step 1: Collect vowels and their indices
       for (let i = 0; i < s.length; i++) {
           if (vowels.has(s[i])) {
               vowelsInString.push(s[i]);
               indices.push(i);
           }
       }
   
       // Step 2: Sort the collected vowels
       vowelsInString.sort();
   
       // Step 3: Reconstruct the string with sorted vowels
       let result = s.split('');
       for (let i = 0; i < indices.length; i++) {
           result[indices[i]] = vowelsInString[i];
       }
   
       return result.join('');
   
       
   };