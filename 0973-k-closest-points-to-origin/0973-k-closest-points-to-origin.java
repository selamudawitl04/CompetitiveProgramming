class Solution {
    public int[][] kClosest(int[][] points, int k) {
        HashMap<Integer,ArrayList<int[]>> result = new HashMap<>();
        int len = points.length;
        int distance = 0;
        for(int i = 0; i < len; i++){
            distance = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            int point[] = points[i];
            if(result.containsKey(distance)){
                result.get(distance).add(point);
            }else{
                ArrayList<int[]>temp = new ArrayList<>();
                temp.add(point);
                result.put(distance, temp);
            }
        }
        ArrayList<Integer> sortedKeys = new ArrayList<Integer>(result.keySet());
        Collections.sort(sortedKeys);
        int solution[][] = new int[k][2];
        for(Integer key : sortedKeys){
             if(k < 0 ) break;
             for(int j = 0 ; j < result.get(key).size()&& k > 0; j++){
                k--;
                solution[k][0] = result.get(key).get(j)[0];
                solution[k][1] = result.get(key).get(j)[1];
            }
        }
        return solution;
    }
}