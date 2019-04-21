
/* The following program generates a rectangular map (with zero-based indices).
   Given an initial starting point, find the point with the lowest altitude that
   can be reached under these conditions:
   1) moving adjacent only sideways, up, or down (no diagonals)
   2) moving only when the altitude of the neighboring location is equal
      to or less than that of the current location

   If there are multiple points with the same lowest altitude that can be
   reached, select the path that encounters the steepest drop at the point of
   divergence. If each of the paths start out with the same drop in altitude,
   compare the drop at the next step of each route (and if those are the same,
   continue comparing until a difference is found). If there is more than one
   path with the exact same ending altitude and same drops along the way, favor
   points whose row is closest to R0; with points along the same row, Favor
   points whose columns is closest to C0.

Sample map:

      C0  C1  C2  C3
  R0  67  72  93   5
  R1  38  53  71  48
  R2  64  56  52  44
  R3  44  51  57  49

Starting at R0, C1 should end up at R1, C0.
Starting at R1, C3 should end up at R0, C3.
Starting at R3, C2 should end up at R2, C3 since the drop from 57 to 49 is
steeper than the drop from 57 to 51 when comparing R3, C0 to R2, C3.

*/

import java.util.Random;
import java.util.*;

public class LowPointFinder {
    public static class Map {
        // do not change anything in the Map class
        private int mGrid[][] = null;

        // -----------------------------------------
        //Testing
        public void setGrid(int[][] grid) {
            mGrid = grid;
        }
        // -----------------------------------------

        public int getNumRows() {
            return mGrid.length;
        }

        public int getNumColumns() {
            return mGrid[0].length;
        }

        public int getAltitude(int iRow, int iColumn) {
            return mGrid[iRow][iColumn];
        }

        public void printMap() {
            StringBuilder sbRow = new StringBuilder("    ");
            for (int i = 0; i < mGrid[0].length; i++) {
                String strCell = String.format("%4s", "C" + i);
                sbRow.append(strCell);
            }
            System.out.println(sbRow.toString());
            for (int i = 0; i < mGrid.length; i++) {
                String strCell = String.format("%4s", "R" + i);
                sbRow = new StringBuilder(strCell);
                for (int j = 0; j < mGrid[0].length; j++) {
                    strCell = String.format("%4d", getAltitude(i, j));
                    sbRow.append(strCell);
                }
                System.out.println(sbRow.toString());
            }
        }

        private int changeAltitude(int iAltitude, Random random) {
            return iAltitude + random.nextInt(11) - 5;
        }

        public Map(int iNumRows, int iNumColumns, int iRandomSeed) {
            mGrid = new int[iNumRows][iNumColumns];
            Random random = new Random(iRandomSeed);
            for (int i = 0; i < iNumRows; i++) {
                for (int j = 0; j < iNumColumns; j++) {
                    int iAltitude = 0;
                    if (i == 0) {
                        iAltitude = random.nextInt(101);
                    } else {
                        int iSideAltitude = 0;
                        if (j == 0)
                            iSideAltitude = random.nextInt(101);
                        else
                            iSideAltitude = getAltitude(i, j - 1);
                        int iTopAltitude = getAltitude(i - 1, j);
                        iAltitude = (changeAltitude(iSideAltitude, random) + changeAltitude(iTopAltitude, random)) / 2;
                        if (iAltitude < 0)
                            iAltitude = 0;
                        else if (iAltitude > 100)
                            iAltitude = 100;
                    }
                    mGrid[i][j] = iAltitude;
                }
            }
        }
    }

    public static class Node<T> {
        private List<Node<T>> children = new ArrayList<Node<T>>();
        private Node<T> parent = null;
        private T data = null;

        public Node(T data) {
            this.data = data;
        }

        public T getData() {
            return this.data;
        }

        public void  addChild(Node<T> child) {
            this.children.add(child);
            child.setParent(parent);
        }

        public void setParent(Node<T> parent) {
            this.parent = parent;
        }

        public List<Node<T>> getChildren() {
            return children;
        }

        public boolean hasChildren() {
            return (!(this.children.size() == 0));
        }
    }

    public static boolean checkNearby(Map map, int iRow, int iColumn, boolean[][] travelled) {
        // checks if current location is within the borders && if the current
        // location
        // has already been visited
        return (iRow >= 0 && iColumn >= 0 && iRow < map.getNumRows() && iColumn < map.getNumColumns()
                && travelled[iRow][iColumn] == false);
    }

    public static Node<int[]> moveLower(Map map, int iRow, int iColumn, boolean[][] travelled, ArrayList<Node<int[]>> path) {
        travelled[iRow][iColumn] = true;
        int thisAltitude = map.getAltitude(iRow, iColumn);
        int minAltitude = thisAltitude; // used to track which direction to check
        ArrayList<Node<int[]>> path_to_take = new ArrayList<Node<int[]>>();
        boolean is_lowest = true;

        //up
        if (checkNearby(map, iRow - 1, iColumn, travelled) == true) {
            int upAltitude = map.getAltitude(iRow - 1, iColumn);
            if (thisAltitude >= upAltitude) {
                int[] node_value = { iRow - 1, iColumn, upAltitude };
                Node direction = new Node(node_value);
                if (upAltitude < minAltitude) {
                    path_to_take.clear();
                    path_to_take.add(direction);
                    minAltitude = upAltitude;
                } else if (upAltitude == minAltitude) {
                    path_to_take.add(direction);
                }

                System.out.println("Up!");
                System.out.print(iRow - 1 + " ");
                System.out.print(iColumn + " ");
                System.out.println(map.getAltitude(iRow - 1, iColumn));
                is_lowest = false;
            }
        }

        //down
        if (checkNearby(map, iRow + 1, iColumn, travelled) == true) {
            int downAltitude = map.getAltitude(iRow + 1, iColumn);
            if (thisAltitude >= downAltitude) {
                int[] node_value = { iRow + 1, iColumn, downAltitude };
                Node direction = new Node(node_value);
                if (downAltitude < minAltitude) {
                    path_to_take.clear();
                    path_to_take.add(direction);
                    minAltitude = downAltitude;
                } else if (downAltitude == minAltitude) {
                    path_to_take.add(direction);
                }

                System.out.println("Down!");
                System.out.print(iRow + 1 + " ");
                System.out.print(iColumn + " ");
                System.out.println(map.getAltitude(iRow + 1, iColumn));
                is_lowest = false;
            }
            
        }

        //left
        if (checkNearby(map, iRow, iColumn - 1, travelled) == true) {
            int leftAltitude = map.getAltitude(iRow, iColumn - 1);
            if (thisAltitude >= leftAltitude) {
                 int[] node_value = { iRow, iColumn - 1, leftAltitude };
                Node direction = new Node(node_value);
                if (leftAltitude < minAltitude) {
                    path_to_take.clear();
                    path_to_take.add(direction);
                    minAltitude = leftAltitude;
                } else if (leftAltitude == minAltitude) {
                    path_to_take.add(direction);
                }
                
                System.out.println("Left!");
                System.out.print(iRow + " ");
                System.out.print(iColumn - 1 + " ");
                System.out.println(map.getAltitude(iRow, iColumn - 1));
                is_lowest = false;
            }
        }
        
        //right
        if (checkNearby(map, iRow, iColumn + 1, travelled) == true) {
            int rightAltitude = map.getAltitude(iRow, iColumn + 1);
            if (thisAltitude >= rightAltitude) {
                 int[] node_value = { iRow, iColumn + 1, rightAltitude };
                Node direction = new Node(node_value);
                if (rightAltitude < minAltitude) {
                    path_to_take.clear();
                    path_to_take.add(direction);
                    minAltitude = rightAltitude;
                } else if (rightAltitude == minAltitude) {
                    path_to_take.add(direction);
                }

                System.out.println("Right!");
                System.out.print(iRow + " ");
                System.out.print(iColumn + 1 + " ");
                System.out.println(map.getAltitude(iRow, iColumn + 1));
                is_lowest = false;
            }
        }
        System.out.println("Length of Array: " + path_to_take.size());
        // System.out.println("Lowest Altitude: " + path_to_take.get(0).getData()[2]);

        if (is_lowest) {
            System.out.println("Found Lowest!");
             return path.get(0);
        }

        if (path_to_take.size() == 1) {
            int nextRow = path_to_take.get(0).getData()[0];
            int nextColumn = path_to_take.get(0).getData()[1];
            path.set(0, path_to_take.get(0));
            return moveLower(map, nextRow, nextColumn, travelled, path);
        }

        if (path_to_take.size() >= 2) {
            System.out.println("Divergence!");
            for (

                path.get(0).addChild(element);
                return moveLower(map, element.getData()[0], element.getData()[1], travelled, path);
            }
            while (path.get(0).hasChildren()) {
                System.out.println("Overflow");
            }
         

             System.out.println(num1);
            System.out.println(num2);
        }
        return path.get(0);
    }

    public static int[] currAltitude(Map map, int iRow, int iColumn, boolean[][] travelled) {
        travelled[iRow][iColumn] = true; //duplicate?
        int[] result = { iRow, iColumn, map.getAltitude(iRow, iColumn) };
        
        // int[] bad_out = { 0, 0, 0 };
        Node<int[]> initialPosition = new Node<int[]>(result);
        ArrayList<Node<int[]>> nodeContainer= new ArrayList<Node<int[]>>();
        nodeContainer.add(initialPosition);

        // Pass By Reference Test...
        // test(nodeContainer);
        Node<int[]> output = moveLower(map, iRow, iColumn, travelled, nodeContainer);
        
        
        
        System.out.print("Final Destination: ");
        System.out.print(output.getData()[0] + " ");
        System.out.print(output.getData()[1] + " ");
        System.out.println(output.getData()[2]);
        result[0] = output.getData()[0];
        result[1] = output.getData()[1]; 
        result[2] = output.getData()[2]; 

        // while (!moveLower(...)) {}

        /*
        if (moveLower(map, iRow, iColumn, travelled, pathStart)) {
            System.out.println("Hit Lowest!");
            return result;
        } else {
            System.out.println("Did Not Hit Lowest!");
            moveLower(map, pathStart.getData()[0], pathStart.getData()[1], travelled, pathStart);
        }
        */

        return result;
    }

    public static int[] isLowest(Map map, int iRow, int iColumn) {
        // Uses recursion to calculate if adjacent location is lowest point

        // Keep tracks of visited locations, prevents backtracking and infinate
        // loops
        // initially all false by default
        boolean[][] travelled = new boolean[map.getNumRows()][map.getNumColumns()];

        // Stores the results {Altitude, iRow, iColumn}
        // int[] result = { iRow, iColumn, map.getAltitude(iRow, iColumn) };
        int[] result = new int[3]; // { iRow, iColumn, map.getAltitude(iRow, iColumn) };
 
        // uses currAltitude

        
        // Flags to determine steepest drop
        /* 
        boolean UP_STEEPEST = false;
        boolean DOWN_STEEPEST = false;
        boolean LEFT_STEEPEST = false;
        boolean RIGHT_STEEPEST = false;
        */

        
    public static void printLowestPoint(Map map, int iRow, int iColumn) {
        // Return the altitude and coordinates of the lowest point
        System.out.print("Start: "+iRow + " ");
        System.out.print(iColumn + " ");
        System.out.println(map.getAltitu
        int[] result = isLowest(map, iRo

                + " with an altitude of " + result[2]);
    }

         * ic static void main(String[] args) {
         *  map = new Map( map.prin
         * rintLowestPoint(map, 1, 9); rintLowestPoin
         * (map, 3, 0); p
         // printLowestPoint(map, 0, 9);
        */
        Map map = new Map(3,3,0);
        int[][] testgrid = {{1,2,1},{2,3,2},{1,2,1}};
        map.setGrid(testgrid);
        map.printMap();
        printLowestPoint(map,1,1);
    }
}

                             