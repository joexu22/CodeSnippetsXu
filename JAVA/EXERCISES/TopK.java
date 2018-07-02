import java.util.*;
class Solution {
    
    public static <K, V extends Comparable<V>> Map<K, V> sortByValues(final Map<K, V> map)
    {
        Comparator<K> valueComparator = new Comparator<K>() 
        {
            public int compare(K k1, K k2)
            {
                int compare = map.get(k2).compareTo(map.get(k1));
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

    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer> values = new ArrayList<>();
        TreeMap<Integer, Integer> counter = new TreeMap<Integer, Integer>();
        
        int count = 0;
        for(Integer i : nums)
        {
            if(!counter.containsKey(i))
            {
                counter.put(i, 1);
            } else {
                count = counter.get(i) + 1;
                counter.put(i, count);
            }
        }
        
        int v_length = k;
        for(Map.Entry<Integer,Integer> entry : sortByValues(counter).entrySet())
        {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if(v_length > 0)
            {
                values.add(key);
                v_length--;
            }
        }
        return values;
    }
}