class Solution {
    public int longestOnes(int[] nums, int k) {
        int longestOne = Integer.MIN_VALUE;
        int currentMax = 0;
        int windowStart = 0;
        for(int i = 0; i < nums.length; i++){
            currentMax++;
            if(nums[i] == 0){
                if(k == 0){
                    longestOne = Math.max(longestOne, currentMax - 1);
                    while(nums[windowStart] != 0){
                        windowStart++;
                        currentMax--;      
                    }
                    windowStart++;
                    currentMax--;
                }else{
                    k--;
                }
            }
        }
        longestOne = Math.max(longestOne, currentMax);
      return longestOne;
    }
}