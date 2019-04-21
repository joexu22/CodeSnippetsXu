
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

    /* Tree data strucutre used to keep track of diverging paths */
    public static class Node<T> {
        private T data = null;
        Node(T data) {
            this.data = data;
        }
    }

    public static boolean checkLegal(Map map, int iRow, int iColumn, boolean[][] travelled) {
        // Checks if current location is within the borders && if the current location has
        // already been visited
        return (iRow >= 0 && iColumn >= 0 && iRow < map.getNumRows() && iColumn < map.getNumColumns()
                && travelled[iRow][iColumn] == false);
    }

    public static void findPath(Map map, int iRow, int iColumn, boolean[][] travelled, LinkedHashSet<int[]> lowestLocations) {
        if (!checkLegal(map, iRow, iColumn, travelled)) {
            return;
        }
        int currentAltitude = map.getAltitude(iRow, iColumn);
        int lowestAltitude = Integer.MAX_VALUE;
        int[] locationValues = {iRow, iColumn, currentAltitude};
        
        for (int[] location : lowestLocations) {
            lowestAltitude = Math.min(lowestAltitude, location[2]);
            if (currentAltitude < location[2]) {
                lowestLocation.remove(location);
            }
        }

        if (currentAltitude <= lowestAltitude) {
            lowestLocations.add(locationValues);
        }

        for (int[] location : lowestLocations) {
            System.out.print("Lowest Now: " + location[0] + " ");
            System.out.print(location[1] + " ");
            System.out.println(location[2]);
        }
        
        /*******************************
        //ACCOUNT FOR THE LOWEST ELEMENT
        *******************************/



    }

    public static int[] moveLower(Map map, int iRow, int iColumn, boolean[][] travelled, LinkedHashSet<int[]> lowestLocations) {
        travelled[iRow][iColumn] = true;
        int currentAltitude = map.getAltitude(iRow, iColumn);
        int minimumAltitude = currentAltitude;
        boolean isLowest = true;
        // Test UP, LEFT, DOWN, RIGHT to see if adjacent location has lower altitude
        // DOWN
        if (checkLegal(map, iRow+1, iColumn, travelled)) {
            int downAltitude = map.getAltitude(iRow+1,iColumn);
            if (currentAltitude >= downAltitude) {
                int[] nodeValue = {iRow+1, iColumn, downAltitude};
                if (downAltitude < minimumAltitude) {
                    for (java.util.Map.Entry<int[], Integer> entry : lowestPoints.entrySet()) {
                        if (downAltitude < entry.getValue()) {
                            lowestPoints.remove(entry.getKey());
                        }
                    }
                    lowestPoints.put(nodeValue, downAltitude);
                    minimumAltitude = downAltitude;
                } else if (downAltitude == minimumAltitude) {
                    lowestPoints.put(nodeValue, downAltitude);
                }
                System.out.println("Down!");
                System.out.print(iRow + 1 + " ");
                System.out.print(iColumn + " ");
                System.out.println(map.getAltitude(iRow + 1, iColumn));
                System.out.println("Size Of Array: "+lowestPoints.size());
                isLowest = false;
            } else if (currentAltitude < downAltitude) {
                travelled[iRow+1][iColumn] = true;
            }
        }
        // RIGHT
        if (checkLegal(map, iRow, iColumn+1, travelled)) {
            int rightAltitude = map.getAltitude(iRow,iColumn+1);
            System.out.println("RA: "+rightAltitude);
            System.out.println("MIN: "+minimumAltitude);
            if (currentAltitude >= rightAltitude) {
                int[] nodeValue = {iRow, iColumn+1, rightAltitude};
                if (rightAltitude < minimumAltitude) {
                    for (java.util.Map.Entry<int[], Integer> entry : lowestPoints.entrySet()) {
                        if (rightAltitude < entry.getValue()) {
                            lowestPoints.remove(entry.getKey());
                        }
                    }
                    lowestPoints.put(nodeValue, rightAltitude);
                    minimumAltitude = rightAltitude;
                } else if (rightAltitude == minimumAltitude) {
                    lowestPoints.put(nodeValue, rightAltitude);
                }
                System.out.println("Right!");
                System.out.print(iRow + " ");
                System.out.print(iColumn + 1 + " ");
                System.out.println(map.getAltitude(iRow, iColumn + 1));
                System.out.println("Size Of Array: "+lowestPoints.size());
                isLowest = false;
            } else if (currentAltitude < rightAltitude) {
                travelled[iRow][iColumn+1] = true;
            }
        }
        
        // LEFT
        if (checkLegal(map, iRow, iColumn-1, travelled)) {
            int leftAltitude = map.getAltitude(iRow,iColumn-1);
            if (currentAltitude >= leftAltitude) {
                int[] nodeValue = {iRow, iColumn-1, leftAltitude};
                if (leftAltitude < minimumAltitude) {
                    for (java.util.Map.Entry<int[], Integer> entry : lowestPoints.entrySet()) {
                        if (leftAltitude < entry.getValue()) {
                            lowestPoints.remove(entry.getKey());
                        }
                    }
                    lowestPoints.put(nodeValue, leftAltitude);
                    minimumAltitude = leftAltitude;
                } else if (leftAltitude == minimumAltitude) {
                    lowestPoints.put(nodeValue, leftAltitude);
                }
                System.out.println("Left!");
                System.out.print(iRow + " ");
                System.out.print(iColumn - 1 + " ");
                System.out.println(map.getAltitude(iRow, iColumn - 1));
                System.out.println("Size Of Array: "+lowestPoints.size());
                isLowest = false;
            } else if (currentAltitude < leftAltitude) {
                travelled[iRow][iColumn-1] = true;
            }
        }
        // UP
        if (checkLegal(map, iRow-1, iColumn, travelled)) {
            int upAltitude = map.getAltitude(iRow-1,iColumn);
            if (currentAltitude >= upAltitude) {
                int[] nodeValue = {iRow-1, iColumn, upAltitude};
                if (upAltitude < minimumAltitude) {
                    for (java.util.Map.Entry<int[], Integer> entry : lowestPoints.entrySet()) {
                        if (upAltitude < entry.getValue()) {
                            lowestPoints.remove(entry.getKey());
                        }
                    }
                    lowestPoints.put(nodeValue, upAltitude);
                    minimumAltitude = upAltitude;
                } else if (upAltitude == minimumAltitude) {
                    lowestPoints.put(nodeValue, upAltitude);
                }
                System.out.println("Up!");
                System.out.print(iRow - 1 + " ");
                System.out.print(iColumn + " ");
                System.out.println(map.getAltitude(iRow - 1, iColumn));
                System.out.println("Size Of Array: "+lowestPoints.size());
                isLowest = false;
            } else if (currentAltitude < upAltitude) {
                travelled[iRow-1][iColumn] = true;
            }
        }

        int num = lowestPoints.size();
        System.out.println("Size Of Array: "+lowestPoints.size());
        
        if (isLowest) {
            System.out.println("Found Lowest!");
            return lowestPoints.entrySet().iterator().next().getKey();
        }
        
        if (lowestPoints.size() == 1) {
            int nextRow = lowestPoints.entrySet().iterator().next().getKey()[0];
            int nextCol = lowestPoints.entrySet().iterator().next().getKey()[1];
            return moveLower(map, nextRow, nextCol, travelled, lowestPoints);
        }
        
        if (lowestPoints.size() > 1) {
            for (java.util.Map.Entry<int[], Integer> entry : lowestPoints.entrySet()) {
                int nextRow = entry.getKey()[0];
                int nextCol = entry.getKey()[1];
                return moveLower(map, nextRow, nextCol, travelled, lowestPoints);
            }
        }
        
        return new int[]{0,0,0};
    }

    public static int[] findLowest(Map map, int iRow, int iColumn) {
        // table of locations checked, prevents backtracking and infinite loops
        // initilized to false
        boolean[][] travelled = new boolean[map.getNumRows()][map.getNumColumns()];
        int[] result = { iRow, iColumn, map.getAltitude(iRow, iColumn) };

        LinkedHashMap<int[], Integer> lowestPoints = new LinkedHashMap<int[], Integer>();
        lowestPoints.put(result, result[2]);
        
        LinkedHashSet<int[]> lowestLocations = new LinkedHashSet<int[]>();
        lowestLocations.add(result);
        
        result = moveLower(map, iRow, iColumn, travelled, lowestLocations);
        return result;
    }

    public static void printLowestPoint(Map map, int iRow, int iColumn) {
        // implement this function (and any necessary helper code);
        // replace the ??? with the correct information
        System.out.print("Start: "+iRow + " ");
        System.out.print(iColumn + " ");
        System.out.println(map.getAltitude(iRow, iColumn));

        int[] result = findLowest(map, iRow, iColumn);
        System.out.println("The lowest reachable point occurs at " + result[0] + ", " + result[1]
                + " with an altitude of " + result[2]);
    }

    public static void main(String args[]) {
        /*
        Map map = new Map(10, 10, 0);
        map.printMap();
        //printLowestPoint(map, 1, 9);
        //printLowestPoint(map, 6, 8);
        printLowestPoint(map, 5, 4);
        */

        Map map = new Map(5,5,0);
        int[][] testgrid = {{3,2,3,2,3},{2,3,4,3,2},{3,4,5,4,3},{2,3,4,3,2},{1,2,3,2,1}};
        map.setGrid(testgrid);
        map.printMap();
        printLowestPoint(map,1,1);

    }
}

    

    

    

    


    

    

    

    


    

    

    

    


    

    

    

    


    

    

    

    
