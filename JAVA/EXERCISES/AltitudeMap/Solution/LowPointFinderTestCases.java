import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

class LowPointFinderTestCases {
	public static void main(String[] args) {
        LowPointFinder.Map map1 = new LowPointFinder.Map(4,4,0);
        int[][] testgrid0 = {{67,72,93,5},{38,53,71,48},{64,56,52,44},{44,51,57,49}};
        map1.setGrid(testgrid0);
        map1.printMap();

        System.out.println("Starting at R0, C1 should end up at R1, C0");
        LowPointFinder.printLowestPoint(map1, 0, 1);
        System.out.println("Starting at R1, C3 should end up at R0, C3");
        LowPointFinder.printLowestPoint(map1, 1, 3);
        System.out.println("Starting at R3, C2 should end up at R2, C3");
        LowPointFinder.printLowestPoint(map1, 3, 2);
        System.out.println();


        LowPointFinder.Map map = new LowPointFinder.Map(5,5,0);
        int[][] testgrid1 = {{1,2,3,2,1},{2,3,4,3,2},{3,4,5,4,3},{2,3,4,3,2},{1,2,3,2,1}};
        map.setGrid(testgrid1);
        map.printMap();
        System.out.println("Starting at R2, C2 should end up at R0, C0");
        LowPointFinder.printLowestPoint(map,2,2);
        System.out.println();

        int[][] testgrid2 = {{1,2,3,4,5},{99,99,99,99,6},{3,2,1,99,7},{4,99,99,99,8},{5,6,7,8,9}};
        map.setGrid(testgrid2);
        map.printMap();
        System.out.println("Starting at R4, C4 should end up at R0, C0");
        LowPointFinder.printLowestPoint(map,4,4);
        System.out.println();
        
        int[][] testgrid3 = {{1,2,3,4,5},{99,99,99,99,6},{1,1,1,99,7},{1,99,99,99,8},{1,1,1,1,9}};
        map.setGrid(testgrid3);
        map.printMap();
        // Starting at the Corner (R4, C4)
        System.out.println("Starting at R4, C4 should end up at R2, C2");
        System.out.println("(R2, C2) as opposed to (R2, C0) because R2, C2 has more 'drops'");
        LowPointFinder.printLowestPoint(map,4,4);
        System.out.println();

        int[][] testgrid4 = {{9,2,3,4,9},{9,1,9,5,9},{6,1,9,8,9},{7,7,9,9,1},{9,9,9,1,9}};
        map.setGrid(testgrid4);
        map.printMap();
        // Starting at spot (R3, C3)
        System.out.println("Starting at R3, C3 should end up at R1, C1");
        System.out.println("(R1, C1) as opposed to (R3, C4) because I am considering any drop > no drop");
        LowPointFinder.printLowestPoint(map,3,3);
        System.out.println();

        int[][] testgrid5 = {{2,2,2,2,2},{2,2,2,2,2},{2,2,2,2,2},{2,2,2,2,2},{2,2,2,2,3}};
        map.setGrid(testgrid5);
        map.printMap();
        // Starting at the Corner (R4, C4)
        System.out.println("Starting at R4, C4 shoudl end up at R0, C0");
        LowPointFinder.printLowestPoint(map,4,4);

        int[][] testgrid6 = {{99,0,2,99,99},{99,99,4,99,99},{1,4,5,4,3},{99,99,4,99,99},{99,99,3,99,99}};
        map.setGrid(testgrid6);
        map.printMap();
        // Starting at the Corner (R2, C2)
        System.out.println("Starting at R2, C2 shoudl end up at R0, C1");
        LowPointFinder.printLowestPoint(map,2,2);
	}
}