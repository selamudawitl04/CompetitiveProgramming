class Solution {
    public int maxVowels(String s, int k) {
      int currentMax = 0;
      int maxVowel = Integer.MIN_VALUE;
      int windowStart = 0;
      for(int i = 0 ; i < s.length(); i++){
          char ch = s.charAt(i);
          if(ch == 'a' || ch == 'e'||ch == 'i'||ch == 'o'||ch == 'u')
            currentMax++;
          if(i >= k - 1){
              maxVowel = Math.max(maxVowel, currentMax);
              char ch2 = s.charAt(windowStart);
              if(ch2 == 'a' || ch2 == 'e'||ch2 == 'i'||ch2 == 'o'||ch2 == 'u')
                  currentMax--;
              windowStart++;
  
          }
      }
       return maxVowel;
    }
}