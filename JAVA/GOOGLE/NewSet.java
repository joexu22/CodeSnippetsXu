import java.util.*;

class NewSet {
    ArrayList array = new ArrayList();
    HashMap hash = new HashMap();

    public void Insert(Object elem) {
        this.array.add(elem);
        int objectIndex = this.array.indexOf(elem);
        this.hash.put(elem, objectIndex);
    }

    public Object Get(Object elem) {
        int objectIndex = (Integer) this.hash.get(elem);
        System.out.println(this.array.get(objectIndex));
        System.out.println(this.hash.get(elem));
        return this.array.get(objectIndex);
    }

    public void Delete(Object elem) {
        int objectIndex = (Integer) this.hash.get(elem);
        this.array.remove(objectIndex);
        this.hash.remove(elem);
    }

    public Object ReturnRandom() {
        int randomIndex = (int) (Math.random() * (array.size()));
        System.out.println(randomIndex);
        System.out.println(array.get(randomIndex));
        return this.array.get(randomIndex);
    }

    public static void main(String[] args) {
        NewSet newset = new NewSet();
        newset.Insert(10);
        newset.Insert(20);
        newset.Insert(30);
        newset.Insert(40);
        newset.Insert(50);
        newset.Get(10);
        newset.ReturnRandom();
        for (int i = 0; i < 10; i++) {
            newset.ReturnRandom();
        }
        newset.Delete(30);
        // data visualization work to determine statistically if things has worked out
        for (int i = 0; i < 10; i++) {
            newset.ReturnRandom();
        }
    }
}