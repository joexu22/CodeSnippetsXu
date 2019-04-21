class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class TestingNodes {
    public static void main(String[] args) {
        ListNode A = new ListNode(10);
        ListNode B = new ListNode(10);
        A.next = B;
        B.next = A;
        System.out.println(A.equals(B.next));
        System.out.println(B.equals(A.next));
    }
}