var groupAnagrams = function(strs) {
    const final = [];
     const seenKeys = []; // Stores unique sorted forms to identify groups
 
     for (let i = 0; i < strs.length; i++) {
         const sortedKey = strs[i].split("").sort().join("");
 
         // Find if this sorted form already exists in `seenKeys`
         let index = seenKeys.indexOf(sortedKey);
         
         if (index === -1) {
             // New anagram group
             seenKeys.push(sortedKey);
             final.push([strs[i]]);
         } else {
             // Existing anagram group
             final[index].push(strs[i]);
         }
     }
 
     return final;
 
 
     
 };
