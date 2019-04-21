import java.util.*;

class TicTacToe {
    public void printGame(char[][] game) {
        System.out.println(game[0][0] + "|" + game[0][1] + "|" + game[0][2]);
        System.out.println(game[1][0] + "|" + game[1][1] + "|" + game[1][2]);
        System.out.println(game[2][0] + "|" + game[2][1] + "|" + game[2][2]);
    }

    public char[][] initializeBoard() {
        char[][] table = new char[3][3];
        Arrays.fill(table[0], '-');
        Arrays.fill(table[1], '-');
        Arrays.fill(table[2], '-');
        return table;
    }

    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        char[][] gameBoard = game.initializeBoard();
        game.printGame(gameBoard);
    }
}