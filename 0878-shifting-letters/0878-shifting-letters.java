// class Solution {
//     public String shiftingLetters(String s, int[] shifts) {
//         char[] sList = s.toCharArray();
//         int n = sList.length;

//         for (int i = n - 2; i >= 0; i--) {
//             shifts[i] = (shifts[i] + shifts[i + 1]) % 26;
//         }

//         for (int i = 0; i < n; i++) {
//             char c = sList[i];
//             char shiftedChar = (char)((c - 'a' + (int)shifts[i]) % 26 + 'a');
//             sList[i] = shiftedChar;
//         }

//         return new String(sList);
//     }
// }

class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        int n = s.length();
        long totalShifts = 0;
        char[] res = new char[n];

        for (int i = n - 1; i >= 0; i--) {
            totalShifts = (totalShifts + shifts[i]) % 26;
            char original = s.charAt(i);
            int shifted = (original - 'a' + (int)totalShifts) % 26;
            res[i] = (char)('a' + shifted);
        }
        return new String(res);
    }
}