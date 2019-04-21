import java.util.*;

class Vertex {
	int value;
	Vertex(int val) { this.value = val; }
}

class Edge {}

class MatrixRepresentation {
	// -21, -5, -1, 0 , 1, 3, 11
	int[] numbers = new int[] {-21, -5, -1, 0, 1, 3, 11};
	int[][] graph = new int[7][7];
	public void printNums() { System.out.println(Arrays.toString(numbers)); }
	public void printGraph() {
		for (int i = 0; i < 7; i++) {
			System.out.println(Arrays.toString(graph[i]));
		}
	}
	
	public int[][] buildGraph() {
		for (int i = 0; i < 7; i++) {
			for (int j = 0; j < 7; j++) {
				graph[i][j] = Math.abs(numbers[i] - numbers[j]);
			}
		}
		return graph;
	}
	
	public int dumbCalculation() {
		int distanceA = graph[3][4] + graph[4][2] + graph[2][5] + graph[5][1] +
		graph[1][6] + graph[6][0] + graph[0][3];
		
		int distanceB = graph[0][1] + graph[1][2] + graph[2][3] + graph[3][4] +
		graph[4][5] + graph[5][6] + graph[6][0];
		System.out.println(distanceA);
		System.out.println(distanceB);
		return 0;
	}
}

class CalculatorCalculation {
	public static void main(String[] args) {
		MatrixRepresentation Test = new MatrixRepresentation();
		Test.printNums();
		Test.buildGraph();
		Test.printGraph();
		Test.dumbCalculation();
	}
}