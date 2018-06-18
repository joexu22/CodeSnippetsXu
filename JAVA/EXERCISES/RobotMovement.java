import java.util.*;

class RobotMovement {
    //checks if this would be a valid place to move
    public static boolean canMove(int r, int c, int row, int col, int[][] layout) {
        return (r >= 0 && c >= 0 && r < row && c < col && layout[r][c]>0);
    }

    public static boolean isHere(int r, int c, int row, int col, int[][] layout) {
        //reached package
        if (layout[r][c] == 9) {
            return true;
        }

        //prevents looping
        layout[r][c] = 0;

        //down
        if (canMove(r+1, c, row, col, layout) == true) {
            if (isHere(r+1, c, row, col, layout)) {
                return true;
            }
        }
        //right
        if (canMove(r, c+1, row, col, layout) == true) {
            if (isHere(r, c+1, row, col, layout)) {
                return true;
            }
        }
        //up
        if (canMove(r-1, c, row, col, layout) == true) {
            if (isHere(r-1, c, row, col, layout)) {
                return true;
            }
        }
        //left
        if (canMove(r, c-1, row, col, layout) == true) {
            if (isHere(r, c-1, row, col, layout)) {
                return true;
            }
        }
        return false;
    }

    public static int isPath(int row, int col, int[][] layout) {
        if (isHere(0, 0, row, col, layout) == true) {
            return 1;
        }
        return 0;
    }

    public static void main(String[] args) {
        //should return 1
        int[][] warehouse1 = { { 1 }, { 9 } };
        System.out.println(Arrays.deepToString(warehouse1));
        System.out.println(isPath(2, 1, warehouse1));

        //should return 1
        int[][] warehouse2 = { { 1, 1, 1, 1, 1, 1, 1, 9 } };
        System.out.println(Arrays.deepToString(warehouse2));
        System.out.println(isPath(1, 8, warehouse2));

        //should return 1
        int[][] warehouse3 = { { 1, 0, 9 }, { 1, 0, 1 }, { 1, 1, 1, } };
        System.out.println(Arrays.deepToString(warehouse3));
        System.out.println(isPath(3, 3, warehouse3));

        //should return 0
        int[][] warehouse4 = { { 1, 0, 9 }, { 1, 0, 1 }, { 1, 0, 1, } };
        System.out.println(Arrays.deepToString(warehouse4));
        System.out.println(isPath(3, 3, warehouse4));

        //should return 1
        int[][] warehouse5 = { { 1, 1, 9 }, { 1, 1, 1 }, { 1, 1, 1, } };
        System.out.println(Arrays.deepToString(warehouse5));
        System.out.println(isPath(3, 3, warehouse5));

        //should return 1
        int[][] warehouse6 = {{1,0,1,1,1},{1,0,1,0,1},{1,0,9,0,1},{1,0,0,0,1},{1,1,1,1,1}};
        System.out.println(Arrays.deepToString(warehouse6));
        System.out.println(isPath(5, 5, warehouse6));
    }
}

