class LRUCache {
    int capacity;
    HashMap<Integer, Node> cache = new HashMap<Integer, Node>();
    Node head = null;
    Node end = null;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            Node n = cache.get(key);
            remove(n);
            setHead(n);
            return n.value;
        }
        return -1;
    }

    public void remove(Node n) {
        if (n.pre != null) {
            n.pre.next = n.next;
        } else {
            head = n.next;
        }

        if (n.next != null) {
            n.next.pre = n.pre;
        } else {
            end = n.pre;
        }
    }

    public void setHead(Node n) {
        n.next = head;
        n.pre = null;

        if (head != null) {
            head.pre = n;
        }
        head = n;

        if (end == null) {
            end = head;
        }
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node old = cache.get(key);
            old.value = value;
            remove(old);
            setHead(old);
        } else {
            Node entry = new Node(key, value);
            if (cache.size() >= capacity) {
                cache.remove(end.key);
                remove(end);
                setHead(entry);

            } else {
                setHead(entry);
            }

            cache.put(key, entry);
        }
    }
}

class Node {
    int key;
    int value;
    Node pre;
    Node next;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}