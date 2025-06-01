/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        Node newNode = new Node(insertVal);

        if(head == null){
            newNode.next = newNode;
            return newNode;
        }

        Node curr = head;
        while(true){
            Node next = curr.next;
            if (insertVal >= curr.val && insertVal <= next.val) {
                break;
                }
            if (curr.val > next.val) {
                if (insertVal >= curr.val || insertVal <= next.val) {
                    break;
                }
            }
            curr = curr.next;
            if (curr == head) {
                break;
            }
        }
        newNode.next = curr.next;
        curr.next = newNode;
        return head;
    }
}