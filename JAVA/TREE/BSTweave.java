public class BSTweave {
    static class Node {
        private int data;
        private Node left;
        private Node right;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public void setRight(Node right) {
            this.right = right;
        }

        public Node getLeft() {
            return this.left;
        }

        public Node getRight() {
            return this.right;
        }

        public int getData() {
            return this.data;
        }

        public boolean equals(Node n) {
            if (this.data == n.getData()) {
                return true;
            }
            return false;
        }
    }

    public static void main(String[] args) {
    }
}