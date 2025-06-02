/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode curr1 = head;
        ListNode curr2 = slow;
        ListNode prev = null;

        while (curr2 != null) {
            ListNode next_node = curr2.next;
            curr2.next = prev;
            prev = curr2;
            curr2 = next_node;
        }
        curr2 = prev;
        while (curr1 != null && curr2 != null) {
            if (curr1.val != curr2.val) return false;
            curr1 = curr1.next;
            curr2 = curr2.next;
        }

        return true;

    }
}