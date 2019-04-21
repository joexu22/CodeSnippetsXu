import java.util.*;

class SubStringSubCharacter {
    public int solution(String A, String B) {
        HashMap<Character, Integer> Astring = new HashMap<>();
        HashMap<Character, Integer> Bstring = new HashMap<>();

        char[] Astr = A.toCharArray();
        char[] Bstr = B.toCharArray();

        for(int i=0;i<Astr.length;i++) {
            if (!Astring.containsKey(Astr[i])) {
                Astring.put(Astr[i], 1);
            } else {
                int new_value = Astring.get(Astr[i]);
                new_value++;
                Astring.put(Astr[i], new_value);
            }
        }

        for(int i=0;i<Bstr.length;i++) {
            if (!Bstring.containsKey(Bstr[i])) {
                Bstring.put(Bstr[i], 1);
            } else {
                int new_value = Bstring.get(Bstr[i]);
                new_value++;
                Bstring.put(Bstr[i], new_value);
            }
        }

        System.out.println(Astring);
        System.out.println(Bstring);

        int answer = -1;
        for (Character key : Bstring.keySet()) {
            if (!Astring.containsKey(key)) {
                return -1;
            }
        }
        
        int value = 0;
        for (Map.Entry<Character, Integer> entryB : Bstring.entrySet()){
            int div = (int) Math.ceil((double)entryB.getValue() / (double)Astring.get(entryB.getKey()));
            value = Math.max(value, div);
        }
        answer = value;

        return answer;
    }
    public static void main(String[] args) {
        String test1 = "aabcd";
        String test2 = "cdabcdaba";
        SubStringSubCharacter Solution = new SubStringSubCharacter();
        int out = Solution.solution(test1, test2);
        System.out.println(out);
        System.out.println(Integer.MAX_VALUE);
    }
}