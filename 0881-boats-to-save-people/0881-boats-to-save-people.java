class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int tail = people.length - 1;
        int head = 0;
        int min = 0;
        Arrays.sort(people);
        while(head <= tail){
            if(people[head] + people[tail] <= limit){
                min++;
                head++;
                tail--;
            }else{
                min++;
                tail--;
            }
        }
        return min;
    }
}