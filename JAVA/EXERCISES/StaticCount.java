public class StaticCount{
    static int objectCount = 0;

    public StaticCount(){
        objectCount++;
    }

    public static void main(String[] args){
        StaticCount item1 = new StaticCount();
        StaticCount item2 = new StaticCount();
        System.out.println(objectCount);
    }
}