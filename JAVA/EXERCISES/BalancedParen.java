import java.util.*;

class BalancedParen {
    public static void main(String[] args) {
        String exp1 = "[()]{}{[()()]()}";
        String exp2 = "[(])";
        String exp3 = "()";
        System.out.println(Balanced(exp1));
        System.out.println(Balanced(exp2));
        System.out.println(Balanced(exp3));
        // char[] test = exp1.toCharArray();
        // System.out.print(test);
    }

    static class stack {
        int top = -1;
        char items[] = new char[100];

        void push(char x) {
            if (top == 99) {
                System.out.print("Stack Full");
            } else {
                items[++top] = x;
            }
        }

        char pop() {
            if (top == -1) {
                System.out.println("Underflow Error");
                return '\0';
            } else {
                char element = items[top];
                top--;
                return element;
            }
        }

        boolean isEmpty() {
            return (top == -1) ? true : false;
        }
    }

    static boolean isMatchingPair(char character1, char chracter2) {
        if (character1 == '(' && chracter2 == ')') {
            return true;
        } else if (character1 == '[' && chracter2 == ']') {
            return true;
        } else if (character1 == '{' && chracter2 == '}') {
            return true;
        } else {
            return false;
        }
    }

    static boolean Balanced(String exp) {
        char[] content = exp.toCharArray();
        stack st = new stack();

        for (Character c : content) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            }
            if (c == ')' || c == ']' || c == '}') {
                if (st.isEmpty()) {
                    return false;
                } else if (!isMatchingPair(st.pop(), c)) {
                    return false;
                }
            }
        }
        if (st.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}