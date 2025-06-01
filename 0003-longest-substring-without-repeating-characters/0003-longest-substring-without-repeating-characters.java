class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0, j = 0;
        int maxLength = 0;
        List<Character> sList = new ArrayList<>();

        while (j < s.length()) {
            char curr = s.charAt(j);

            if (sList.contains(curr)) {
                sList.remove((Character) s.charAt(i));  
                i++;
            } else {
                sList.add(curr);
                maxLength = Math.max(maxLength, j - i + 1);
                j++;
            }
        }

        return maxLength;
    }
}