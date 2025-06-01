// class Solution {
//     public boolean isValid(String s) {
//         Stack<Character> stack = new Stack<>();

//         for(char ch: s.toCharArray()){
//             if (ch == '(') stack.push(')');
//             else if (ch == '[') stack.push(']');
//             else if (ch == '{') stack.push('}');
//             else{
//                 if(stack.isEmpty() || stack.pop() != ch) return false;
//             }
//         }
//         return stack.isEmpty();
//     }
// }


class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> braces = new HashMap<>();
        braces.put('(', ')');
        braces.put('[', ']');
        braces.put('{', '}');

        Stack<Character> stack = new Stack<>();

        for(char ch: s.toCharArray()){
            if (braces.containsKey(ch)) stack.push(braces.get(ch));
            else {
                if (stack.isEmpty() || stack.pop() != ch) return false;
            }
        }
        return stack.isEmpty();
    }
}