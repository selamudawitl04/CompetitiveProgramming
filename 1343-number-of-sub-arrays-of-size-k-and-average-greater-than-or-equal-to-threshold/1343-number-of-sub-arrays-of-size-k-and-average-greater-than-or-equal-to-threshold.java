class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int numberOfSubArray = 0;
        int currentSum = 0;
        for(int i = 0; i < arr.length; i++){
            currentSum+= arr[i];
            if(i >= k - 1){
                if(currentSum / k >= threshold)
                    numberOfSubArray++;
                currentSum-= arr[i-k + 1]; 
            }
        }
        return numberOfSubArray;
    }
}