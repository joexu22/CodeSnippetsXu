import java.util.*;

class Node {
    int p;
    int s;
    Node pre;
    Node next;

    public Node(int p, int s) {
        this.p = p;
        this.s = s;
    }
}

class CarFleet {
    public static int partition(int[] p, int[] s, int l, int h) {
        int pivot = s[h];
        int i = (l - 1);
        for (int j = l; j < h; j++) {
            if (s[j] <= pivot) {
                i++;
                int temp = s[i];
                s[i] = s[j];
                s[j] = temp;

                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
        int temp = s[i + 1];
        s[i + 1] = s[h];
        s[h] = temp;

        temp = p[i + 1];
        p[i + 1] = p[h];
        p[h] = temp;

        return i + 1;
    }

    public static void sort(int[] p, int[] s, int l, int h) {
        if (l < h) {
            int pi = partition(p, s, l, h);
            sort(p, s, l, pi - 1);
            sort(p, s, pi + 1, h);
        }
    }

    public static int carFleet(int target, int[] position, int[] speed) {
        sort(position, speed, 0, position.length - 1);
        Node head = null;
        Node end = null;
        Node connect = new Node(position[0], speed[0]);
        sort(position, speed, 0, position.length - 1);
        // int[] next = new int[position.length];
        for (int i = 0; i < position.length; i++) {
            Node newNode = new Node(position[i], speed[i]);
            if (i == 0) {
                head = newNode;
                newNode.pre = head;
            }
            if (i == position.length) {
                end = newNode;
                newNode.next = end;
            }
            connect.next = newNode;
            newNode.pre = connect;
            connect = newNode;
        }

        System.out.println(Arrays.toString(position));
        System.out.println(Arrays.toString(speed));
        connect = head;
        while (connect.next) {
            System.out.println(connect.p + " " + connect.s);
            connect = connect.next;
        }

        int out = 0;
        return out;
    }

    public static void main(String[] args) {
        int[] po = new int[] { 10, 8, 0, 5, 3 };
        int[] sp = new int[] { 2, 4, 1, 1, 3 };
        carFleet(10, po, sp);
        // sort(po, sp, 0, 4);
        // System.out.println(Arrays.toString(po));
        // System.out.println(Arrays.toString(sp));
    }
}