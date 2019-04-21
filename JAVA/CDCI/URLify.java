class URLify {
    public String mySolution(String S, int stringLength) {
        char[] strCharArray = S.toCharArray();
        int spaceCount = 0;
        for (int i = 0; i < S.length(); i++) {
            if (strCharArray[i] == ' ') {
                spaceCount++;
            }
        }
        int index = stringLength + spaceCount * 2; //
        // this line is strange - appearantly it does not quite do anything in Java
        // where strings are not 0 delimited
        if (stringLength < strCharArray.length) {
            strCharArray[stringLength] = '\0';
        }

        char[] newString = new char[index];
        for (int i = strCharArray.length - 1; i >= 0; i--) {
            if (strCharArray[i] == ' ') {
                newString[--index] = '0';
                newString[--index] = '2';
                newString[--index] = '%';
            } else {
                newString[--index] = strCharArray[i];
            }
        }
        return new String(newString);
    }

    // It's been recommended that I use StringBuilder...

    public static void main(String[] args) {
        String S = "This Is Cool";
        URLify Solution = new URLify();
        System.out.println(Solution.mySolution(S, 12));
    }
}
