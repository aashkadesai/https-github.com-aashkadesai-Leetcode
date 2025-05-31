class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        char[] sList = s.toCharArray();
        int n = sList.length;
        long[] longShifts = new long[n];

        // Copy shifts into long[]
        for (int i = 0; i < n; i++) {
            longShifts[i] = shifts[i];
        }

        // Accumulate shifts from right to left (mod 26 early to avoid overflow)
        for (int i = n - 2; i >= 0; i--) {
            longShifts[i] = (longShifts[i] + longShifts[i + 1]) % 26;
        }

        // Apply shifts safely
        for (int i = 0; i < n; i++) {
            int shift = (int)(longShifts[i] % 26);
            char c = sList[i];
            char shiftedChar = (char)((c - 'a' + shift) % 26 + 'a');
            sList[i] = shiftedChar;
        }

        return new String(sList);
    }
}
