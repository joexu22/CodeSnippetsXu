
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
import java.util.concurrent.ConcurrentHashMap;

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

    public static boolean checkLegal(Map map, int iRow, int iColumn, boolean[][] travelled) {
        // Checks if current location is within the borders && if the current location has
        // already been visited
        return (iRow >= 0 && iColumn >= 0 && iRow < map.getNumRows() && iColumn < map.getNumColumns()
                && travelled[iRow][iColumn] == false);
    }

    public static void findPath(Map map, int iRow, int iColumn, boolean[][] travelled, Set<int[]> lowestLocations) {
        System.out.println("New Path");
        if (!checkLegal(map, iRow, iColumn, travelled)) {
            return;
        }
        travelled[iRow][iColumn] = true;
        int currentAltitude = map.getAltitude(iRow, iColumn);
        int lowestAltitude = Integer.MAX_VALUE;
        int[] locationValues = {iRow, iColumn, currentAltitude};
        for (int[] location : lowestLocations) {
            lowestAltitude = Math.min(lowestAltitude, location[2]);
            //if (currentAltitude < location[2]) {
            //    lowestLocations.remove(location);
            //}
        }

        if (currentAltitude <= lowestAltitude) {
            lowestLocations.add(locationValues);
        }

        for (int[] location : lowestLocations) {
            System.out.print("Lowest Now: " + location[0] + " ");
            System.out.print(location[1] + " ");
            System.out.print(location[2] + " ");
            System.out.println("|| Set Size: " + lowestLocations.size());
        }
        /*******************************
        //ACCOUNT FOR THE LOWEST ELEMENT
        *******************************/
    }

    public static int[] moveLower(Map map, boolean[][] travelled, Set<int[]> lowestLocations) {
        // number of possible branches to traverse
        int pathsToTake = lowestLocations.size();

        // flag to signal found lowest altitude (ends recursion)
        boolean hasLower = false;
        
        // flag to signal found more possible paths
        boolean hasMorePaths = false;
        int oldLocationNum = lowestLocations.size();
        System.out.println("OLD Location Number: "+oldLocationNum);

        // new HashSet, contains possible paths, to perform a breath-first search on paths
        HashSet<int[]> newLocations = new HashSet<int[]>();
        newLocations.addAll(lowestLocations);
        
        // checks each of the 4 directions for lower altitudes, appends to possible paths
        for (int[] item : newLocations) {
            System.out.println("ItemToIterate: "+ Arrays.toString(item));
            int nextRow = item[0];
            int nextCol = item[1];
            findPath(map, nextRow-1, nextCol, travelled, lowestLocations); //Check UP
            findPath(map, nextRow+1, nextCol, travelled, lowestLocations); //Check DOWN
            findPath(map, nextRow, nextCol-1, travelled, lowestLocations); //Check LEFT
            findPath(map, nextRow, nextCol+1, travelled, lowestLocations); //Check RIGHT
        }
        int newLocationNum = lowestLocations.size();
        if (oldLocationNum != newLocationNum) {
            hasMorePaths = true;
        }
        System.out.println("NEW Location Number: "+newLocationNum);
        
        // find that paths that are the lowest altitude
        // find lowests altitude
        int lowestAltitude = Integer.MAX_VALUE;
        for (int[] location : lowestLocations) {
            lowestAltitude = Math.min(lowestAltitude, location[2]);
        }
        System.out.println("-Skimming Set-");
        //eliminate paths that are not "steepest drop"
        for (int[] location : lowestLocations) {
            if (location[2] > lowestAltitude) {
                hasLower = true; //has lower altitude, can continue searching
                lowestLocations.remove(location);
            }
        }
        
        for (int[] item : lowestLocations) {
            System.out.println("InSet: "+ Arrays.toString(item));
        }

        // recursively finds lower altitudes
        if (hasLower || hasMorePaths) {
            moveLower(map, travelled, lowestLocations);
        } else {
            System.out.println("Ending");
            int[] output = lowestLocations.iterator().next();
            System.out.print("Final: " + output[0] + " ");
            System.out.print(output[1] + " ");
            System.out.print(output[2] + " ");
            System.out.println("|| Set Size: " + lowestLocations.size());
            //return lowestLocations.iterator().next();
        }

        // finds the location closest to R0 and C0 as specified
        int bestRow = Integer.MAX_VALUE;
        int bestColumn = Integer.MAX_VALUE;
        // closest to R0
        for (int[] location : lowestLocations) {
            bestRow = Math.min(bestRow, location[0]);
        }
        // closest to C0 on best R0
        for (int[] location : lowestLocations) {
            if (bestRow == location[0]) {
                bestColumn = Math.min(bestColumn, location[1]);
            }
        }
        int[] result = {bestRow, bestColumn, map.getAltitude(bestRow, bestColumn)};
        return result;
    }

    public static int[] findLowest(Map map, int iRow, int iColumn) {
        // table of locations checked, prevents backtracking and infinite loops
        // initilized to false
        boolean[][] travelled = new boolean[map.getNumRows()][map.getNumColumns()];

        // initial starting location
        int[] result = { iRow, iColumn, map.getAltitude(iRow, iColumn) };

        // uses concurrency to track diverging paths
        ConcurrentHashMap Locations = new ConcurrentHashMap<>();
        Set<int[]> lowestLocations = Locations.newKeySet();
        lowestLocations.add(result); // adds initial starting position
        
        // uses driver function
        result = moveLower(map, travelled, lowestLocations);
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
        int[][] testgrid = {{3,2,3,2,4},{2,3,4,3,2},{3,4,5,4,3},{2,3,4,3,2},{2,2,3,2,1}};
        //int[][] testgrid = {{1,2,3,2,1},{2,3,4,3,2},{3,4,5,4,3},{2,3,4,3,2},{1,2,3,2,1}};
        //int[][] testgrid = {{1,2,3,2,1},{2,3,4,3,2},{3,4,5,4,3},{2,3,4,3,2},{1,2,3,2,1}};
        //int[][] testgrid = {{1,2,3,4,5},{9,9,9,9,6},{3,2,1,9,7},{4,9,9,9,8},{5,6,7,8,9}}; // expect 0 0 1
        //int[][] testgrid = {{2,2,2,2,2},{2,2,2,2,2},{2,2,2,2,2},{2,2,2,2,2},{2,2,2,2,3}}; //expect 0 0 2
        map.setGrid(testgrid);
        map.printMap();
        //printLowestPoint(map,2,2);
        printLowestPoint(map,2,2);
    }
}

    

    

    

    


    

    

    

    


    

    

    

    


    

    

    

    


    

    

    

    
