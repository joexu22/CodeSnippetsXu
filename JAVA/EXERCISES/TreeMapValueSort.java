import java.util.*;
class TreeMapValueSort
{
    public static <K, V extends Comparable<V>> Map<K, V> sortByValues(final Map<K, V> map)
    {
        Comparator<K> valueComparator = new Comparator<K>() 
        {
            public int compare(K k1, K k2)
            {
                int compare = map.get(k1).compareTo(map.get(k2));
                if (compare == 0)
                    return 1;
                else
                    return compare;
            }
        };

        Map<K, V> sortedByValues = new TreeMap<K, V>(valueComparator);
        sortedByValues.putAll(map);
        return sortedByValues;
    }
    public static void main(String[] args)
    {
        TreeMap<String, Integer> treemap = new TreeMap<String, Integer>();
        treemap.put("C",3);
        treemap.put("E",5);
        treemap.put("A",1);
        treemap.put("D",4);
        treemap.put("B",2);

        Map sortedMap = sortByValues(treemap);
        Set set = sortedMap.entrySet();
        Iterator i = set.iterator();

        while(i.hasNext()){
            Map.Entry me = (Map.Entry)i.next();
            System.out.print(me.getKey() + ": ");
            System.out.println(me.getValue());
        }
    }
}