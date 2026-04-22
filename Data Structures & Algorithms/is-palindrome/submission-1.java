class Solution {
    public boolean isPalindrome(String s) {
       StringBuilder lowerstr = new StringBuilder();
       for (char i : s.toCharArray()){
        if(Character.isLetterOrDigit(i)){
            lowerstr.append(Character.toLowerCase(i));
        }
       }
       return lowerstr.toString().equals(lowerstr.reverse().toString());
    }
}
