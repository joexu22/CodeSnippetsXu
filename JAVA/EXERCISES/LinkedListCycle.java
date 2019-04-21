
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

import java.util.*;

public class Solution {
    public boolean hasCycleTwoPointer(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && slow != null) {
            slow = head.next;
            fast = head.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

    public boolean hasCycleHashSet(ListNode head) {
        HashSet<ListNode> nodes = new HashSet<ListNode>();
        while (head != null) {
            if (nodes.contains(head)) {
                return true;
            } else {
                nodes.add(head);
            }
            head = head.next;
        }
        return false;
    }

    public static void main(String[] args) {
        // pass
    }
}