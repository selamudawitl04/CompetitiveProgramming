class Solution {
    public void moveZeroes(int[] nums) {
        int tail = nums.length - 1;
        for(int i = 0; i < tail; i++){
            if(nums[i] == 0){
                for(int j = i; j < tail; j++)
                    nums[j] = nums[j+1];    
                nums[tail--] = 0;
                i--;
            }
        }
    }
}