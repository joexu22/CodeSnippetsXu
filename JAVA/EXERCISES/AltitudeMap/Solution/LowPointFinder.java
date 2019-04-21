
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

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class LowPointFinder {
    public static class Map {
        // do not change anything in the Map class
        private int mGrid[][] = null;
        public int getNumRows() { return mGrid.length; }
        public int getNumColumns() { return mGrid[0].length; }
        public int getAltitude(int iRow, int iColumn) {
             return mGrid[iRow][iColumn];
        }

        // -----------------------------------------
        //Function added for testing purposes
        public void setGrid(int[][] grid) {
            mGrid = grid;
        }
        // -----------------------------------------

        public void printMap() {
            StringBuilder sbRow = new StringBuilder("    ");
            for (int i = 0; i < mGrid[0].length; i++) {
                String strCell = String.format("%4s", "C"+i);
                sbRow.append(strCell);
            }
            System.out.println(sbRow.toString());
            for (int i = 0; i < mGrid.length; i++) {
                String strCell = String.format("%4s", "R"+i);
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
                        if (j == 0) iSideAltitude = random.nextInt(101);
                        else iSideAltitude = getAltitude(i, j-1);
                        int iTopAltitude = getAltitude(i-1, j);
                        iAltitude = (changeAltitude(iSideAltitude, random)
                                     + changeAltitude(iTopAltitude, random))/2;
                        if (iAltitude < 0) iAltitude = 0;
                        else if (iAltitude > 100) iAltitude = 100;
                    }
                    mGrid[i][j] = iAltitude;
                }
            }
        }
    }

    public static boolean checkLegal(Map map, int iRow, int iColumn, boolean[][] travelled) {
        // a helper function that checks to see if the current location is within the borders of the array
        // also checks to see if the location has already been visited
        return (iRow >= 0 && iColumn >= 0 && iRow < map.getNumRows() && iColumn < map.getNumColumns()
                && travelled[iRow][iColumn] == false);
    }

    public static void findPath(Map map, boolean[][] travelled, HashSet<int[]> newLocations, int iRow, int iColumn, int Altitude, int steepestPath) {
        // verifies the neccessity to further check current location
        if (!checkLegal(map, iRow, iColumn, travelled)) {
            return;
        }
        
        // mark current location as travelled
        travelled[iRow][iColumn] = true;

        // calculates the values for current location
        int currentAltitude = map.getAltitude(iRow, iColumn);
        int[] locationValues = {iRow, iColumn, currentAltitude, steepestPath};

        // adds current path to possible solutions if the current path does indeed go lower/stay the same
        if (currentAltitude <= Altitude) {
            newLocations.add(locationValues);
        }
    }

    public static void expandPath(Map map, boolean[][] travelled, Set<int[]> possibleLocations, int[] currentLocation) {
        // calculates values for current location
        int nextRow = currentLocation[0];
        int nextCol = currentLocation[1];
        int currentAltitude = currentLocation[2];
        int steepestPath = currentLocation[3];

        // checks each of the 4 directions for lower altitudes, appends to possible paths
        HashSet<int[]> newLocations = new HashSet<int[]>();
        findPath(map, travelled, newLocations, nextRow-1, nextCol, currentAltitude, steepestPath); //Check UP
        findPath(map, travelled, newLocations, nextRow+1, nextCol, currentAltitude, steepestPath); //Check DOWN
        findPath(map, travelled, newLocations, nextRow, nextCol-1, currentAltitude, steepestPath); //Check LEFT
        findPath(map, travelled, newLocations, nextRow, nextCol+1, currentAltitude, steepestPath); //Check RIGHT

        // marks locations with the steepest drops
        int steepestAltitude = currentAltitude;
        for (int[] location : newLocations) {
            steepestAltitude = Math.min(steepestAltitude, location[2]);
        }
        for (int[] location : newLocations) {
            if (steepestAltitude == location[2]) {
                location[3] += 1;
            }
        }

        // add the locations to the possible paths of traversal
        possibleLocations.addAll(newLocations);
    }

    public static int[] moveLower(Map map, boolean[][] travelled, Set<int[]> possibleLocations) {
        // flag to signal found lowest altitude (used to ends recursion)
        boolean hasLower = false;
        
        // flag to signal found more possible paths (used to end recursion)
        boolean hasMorePaths = false;
        int oldLocationNum = possibleLocations.size();

        // new HashSet, contains possible paths, used to perform a breath-first search on possible paths
        HashSet<int[]> newPathsToTake = new HashSet<int[]>();
        newPathsToTake.addAll(possibleLocations);

        // uses helper function to check for lower altitudes, appends them to possible paths
        for (int[] location : newPathsToTake) {
            expandPath(map, travelled, possibleLocations, location);
        }

        /*
        // finds the lowest altitude so far
        int lowestAltitude = Integer.MAX_VALUE;
        for (int[] location : possibleLocations) {
            lowestAltitude = Math.min(lowestAltitude, location[2]);
        }
        */

        // test to see if new paths have been discovered
        int newLocationNum = possibleLocations.size();
        if (oldLocationNum != newLocationNum) {
            hasMorePaths = true;
        }
                
        // driver to recursively finds lower altitudes,
        // continues to do so if more paths are avaiable to traverse
        if (hasLower || hasMorePaths) {
            moveLower(map, travelled, possibleLocations);
        }

        // determine the lowest altitude reached after exploring each path
        int lowestAltitude = Integer.MAX_VALUE;
        for (int[] location : possibleLocations) {
            lowestAltitude = Math.min(lowestAltitude, location[2]);
        }
        //eliminate paths that are not "steepest drop"
        for (int[] location : possibleLocations) {
            if (location[2] > lowestAltitude) {
                hasLower = true; //has lower altitude, can continue searching
                possibleLocations.remove(location);
            }
        }

        // In the case of multiple possible lowest locations return the path with the steepest drop
        int steepestDrop = Integer.MIN_VALUE;
        for (int[] location : possibleLocations) {
            steepestDrop = Math.max(steepestDrop, location[3]);
        }
        int count = 0;
        for (int[] location : possibleLocations) {
            if (steepestDrop == location[3]) {
                count++;
            }
        }
        if (count == 1) {
            for (int[] location : possibleLocations) {
                if (steepestDrop == location[3]) {
                    return location;
                }
            }
        }

        // In the case where there is no "steepest drop"
        // finds the location closest to R0 and C0 as specified
        int bestRow = Integer.MAX_VALUE;
        int bestColumn = Integer.MAX_VALUE;
        // closest to R0
        for (int[] location : possibleLocations) {
            bestRow = Math.min(bestRow, location[0]);
        }
        // closest to C0, on closest to R0
        for (int[] location : possibleLocations) {
            if (bestRow == location[0]) {
                bestColumn = Math.min(bestColumn, location[1]);
            }
        }

        // builds an array with row, column, and altitude of the lowest altitude
        int[] result = {bestRow, bestColumn, map.getAltitude(bestRow, bestColumn)};
        return result;
    }

    public static int[] findLowest(Map map, int iRow, int iColumn) {
        // table of locations checked, prevents backtracking and infinite loops
        // initilized to false
        boolean[][] travelled = new boolean[map.getNumRows()][map.getNumColumns()];

        // initial starting location
        // {Row, Column, Altitude, "Marker To Indicate Steepest Drop"}
        int[] result = { iRow, iColumn, map.getAltitude(iRow, iColumn), 0 };

        // uses concurrency to track diverging paths
        ConcurrentHashMap Locations = new ConcurrentHashMap<>();
        Set<int[]> possibleLocations = Locations.newKeySet();
        possibleLocations.add(result); // adds initial starting position
        
        // uses driver function
        result = moveLower(map, travelled, possibleLocations);
        return result;
    }

    public static void printLowestPoint(Map map, int iRow, int iColumn) {
        // implement this function (and any necessary helper code);
        // replace the ??? with the correct information
        int[] result = findLowest(map, iRow, iColumn);
        System.out.println("The lowest reachable point occurs at " + result[0] + ", " + result[1]
                + " with an altitude of " + result[2]);
    }

    public static void main(String args[]) {
        Map map = new Map(10, 10, 0);
        map.printMap();
        printLowestPoint(map, 1, 9);
    }
}
