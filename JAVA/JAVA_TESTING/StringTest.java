class StringTest {
    public static void main(String[] args) {
        char[] array = new char[] { 'a', 'b', 'c', 'd', 'e' };
        String out = new String(array);
        System.out.println(out);
        array[2] = '\0';
        String out2 = new String(array);
        System.out.println(out2);

    }
}