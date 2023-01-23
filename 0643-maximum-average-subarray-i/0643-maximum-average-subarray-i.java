class Solution {
    public double findMaxAverage(int[] nums, int k) {
       int maxSum = Integer.MIN_VALUE;
       int currentSum = 0;
       for(int i = 0; i < nums.length; i++){
           currentSum+= nums[i];
           if( i >= k-1){
              maxSum = Math.max(maxSum, currentSum);
              System.out.println(currentSum);
              if(i != nums.length - 1)
              currentSum-= nums[i-(k -1)];
           }
       }
        maxSum = Math.max(maxSum, currentSum);
        return maxSum/(double)k;
    }
}