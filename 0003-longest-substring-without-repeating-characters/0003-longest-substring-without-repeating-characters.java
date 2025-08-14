// class Solution {
//     public int lengthOfLongestSubstring(String s) {
//         int i = 0, j = 0;
//         int maxLength = 0;
//         List<Character> sList = new ArrayList<>();

//         while (j < s.length()) {
//             char curr = s.charAt(j);

//             if (sList.contains(curr)) {
//                 sList.remove((Character) s.charAt(i));  
//                 i++;
//             } else {
//                 sList.add(curr);
//                 maxLength = Math.max(maxLength, j - i + 1);
//                 j++;
//             }
//         }

//         return maxLength;
//     }
// }

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int start = 0;
        int maxLength = 0;

        for(int end = 0; end < s.length(); end++) {
            char current = s.charAt(end);

            if(lastSeen.containsKey(current) && lastSeen.get(current) >= start) {
                start = lastSeen.get(current) + 1;
            }
        lastSeen.put(current, end);
        maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}