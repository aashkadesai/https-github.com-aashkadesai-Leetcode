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
//     public TreeNode insertIntoBST(TreeNode root, int val) {
//         if(root == null){
//             return new TreeNode(val);
//         }

//         TreeNode curr = root;

//         while(true){
//             if(val < curr.val){
//                 if(curr.left == null) {
//                     curr.left = new TreeNode(val);
//                     break;
//                 }
//                 else 
//                     curr = curr.left;
//             } else {
//                 if(curr.right == null) {
//                     curr.right = new TreeNode(val);
//                     break;
//                 } else 
//                     curr = curr.right;
//             }
//         }
//         return root;
//     }
// }


class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null) return new TreeNode(val);

        if (root.val > val) 
            root.left = insertIntoBST(root.left, val);
        else
            root.right = insertIntoBST(root.right, val);
        return root;
    }
}