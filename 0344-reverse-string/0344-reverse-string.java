class Solution {
    public void reverseString(char[] s) {
        int char_length = s.length;
        int i = 0, j = char_length - 1;

        while(i < j){
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }
    }
}