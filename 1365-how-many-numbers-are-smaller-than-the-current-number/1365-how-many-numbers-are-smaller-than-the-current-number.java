class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int result[] = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            int lessThan = 0;
            if(i != 0 && nums[i] == nums[i -1]){
                result[i] = result[i -1];
                continue;
            }
            for(int j = 0; j < nums.length; j++){
                if(nums[j] < nums[i])
                    lessThan++;
            }
                
            result[i] = lessThan;
            
        }
        return result;
    }
}