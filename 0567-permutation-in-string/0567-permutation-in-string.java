class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] need = new int[26];
        int[] want = new int[26];

        for (char c : s1.toCharArray()) {
            need[c - 'a']++;
        }

        int left = 0, right = 0;

        while (right < s2.length()) {
            char c = s2.charAt(right);
            right++;
            want[c - 'a']++;

            if(right - left > s1.length()) {
                want[s2.charAt(left) - 'a']--;
                left++;
            }

            if(Arrays.equals(need, want)) {
                return true;
            }
        }
        return false;
    }
}