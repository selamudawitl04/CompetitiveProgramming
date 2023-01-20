/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let len = nums.length;
    let j = 0;
    for(let i = 1;  i < len; i++){
        if(nums[j] != nums[i]){
            j++;
            nums[j] = nums[i];
        }
    }
    return j+1;
};