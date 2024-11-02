var removeDuplicates = function(nums) {
    const out = nums;
    for (let i = nums.length - 1; i >= 0; i--) {  // Start from the end of the array
        let count = 0;
        for (let j = 0; j < nums.length; j++) {   // Count occurrences
            if (nums[i] === nums[j]) {
                count += 1;
            }
        }
        
        if (count > 1) {
            out.splice(i, 1);  // Remove duplicate if found
        }
    }
    return out.length;
};