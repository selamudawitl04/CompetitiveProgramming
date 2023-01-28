class Solution {
    public int numIdenticalPairs(int[] nums) {
        Arrays.sort(nums);
        HashMap<Integer, Integer>numberPair = new HashMap<>();
        int head = nums[0];
        numberPair.put(head, 1);
        for(int i = 1; i < nums.length; i++){
            if(nums[i] == head){
                numberPair.put(head, numberPair.get(head) + 1);
            }else{
                numberPair.put(nums[i], 1);
                head = nums[i];
            }
        }
        int result = 0;
        for(int num : numberPair.values()){
            result+= (num * (num - 1))/2;
        }
        return result;
    }
}