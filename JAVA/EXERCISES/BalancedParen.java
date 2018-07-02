import java.util.*;

class BalancedParen
{
    public static void main(String[] args)
    {
        String exp1 = "[()]{}{[()()]()}";
        String exp2 = "[(])";
        System.out.println(Balanced(exp1));
        System.out.println(Balanced(exp2));
    }

    public static boolean Balanced(String exp)
    {   
        //Parenthesis to Manipulate
        char[] content = exp.toCharArray();

        //Using The Java Stack
        //Bugs Out When I Use Character Instead Of String
        Stack st = new Stack();
        for(String c : content){
            if(c=="(" || c=="[" || c=="{"){
                st.push(c);
            }else if(c==")" || c=="]" || c=="}"){
                if(st.pop()==c){
                    continue;
                }else{
                    return false;
                }
            }else{
                return false;
            }
            return true;
        }
    }
}