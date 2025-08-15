/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
// class Solution {
//     public List<Integer> postorderTraversal(TreeNode root) {
//         List<Integer> resu = new ArrayList<>();
//         postorder(root, result);
//         return result;
//     }

//     private void postorder(TreeNode node, List<Integer> result) {
//         if(node == null) return;

//         postorder(node.left, result);
//         postorder(node.right, result);
//         result.add(node.val);
//     }
// }

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Stack<TreeNode> stk = new Stack<>();
        stk.push(root);

        while(!stk.isEmpty()) {
            TreeNode node = stk.pop();
            result.add(node.val);
            if(node.left != null) stk.push(node.left);
            if(node.right != null) stk.push(node.right);
        }
        Collections.reverse(result);
        return result;
    }
}