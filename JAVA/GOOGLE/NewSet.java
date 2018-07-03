import java.util.*;

class NewSet {
    ArrayList array = new ArrayList();
    HashMap hash = new HashMap();

    public void Insert(Object elem) {
        this.array.add(elem);
        int object_index = this.array.indexOf(elem);
        this.hash.put(elem, object_index);
    }

    public void Get(Object elem){
        // this.array.get(object);
        // this.hash.get(object);
        int object_index = this.array.indexOf(elem);
        System.out.println(this.array.get(object_index));
        System.out.println(this.hash.get(elem));

    }

    public void Delete() {
        // pass
    }

    public void ReturnRandom() {
        // pass
    }

    public static void main(String[] args) {
        NewSet newset = new NewSet();
        newset.Insert(10);
        newset.Get(10);
    }
}