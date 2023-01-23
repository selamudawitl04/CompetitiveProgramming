class Solution {
    public int[] rearrangeArray(int[] nums) {
        int len = nums.length;
        Arrays.sort(nums);
        int[]result = new int[len];
        int mid = len/2;
        int i = 0, j = 1;
        for(i = 0,j = 1; j < len || i < len; j = j + 2, i = i + 2){
           if(i < len)
           result[i] = nums[mid++];
           if(j < len)
           result[j] = nums[j/2];
        }
        return result;
    }
}