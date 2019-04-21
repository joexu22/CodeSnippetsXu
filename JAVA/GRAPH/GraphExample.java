import java.util.*;

public class GraphExample {
	public static class Edge {
		int source;
		int destination;
		int weight;
		Edge(int s, int d, int w) {
			this.source = s;
			this.destination = d;
			this.weight = w;
		}
	}

	public static class Graph {
		int V;
		int E;
		ArrayList<Edge> AdjacencyList = new ArrayList<Edge>();
		Graph(int V, int E) {
			this.V = V;
			this.E = V;
		}
	}

	public static boolean isNegativeCycleBF(Graph graph, int src) {
		int V = graph.V;
		int E = graph.E;
		int[] dist = new int[V];
		
		for (int i=0; i<V; i++) {
			dist[i] = Integer.MAX_VALUE;
		}
		dist[0] = 0;

		// relax edges |V|-1 times
		for (int i=1; i<=V-1; i++) {
			for (int j=0; j<E; j++) {
				int u = graph.AdjacencyList.get(j).source;
				int v = graph.AdjacencyList.get(j).destination;
				int w = graph.AdjacencyList.get(j).weight;
				if (dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
					dist[v] = dist[u] + w;
				}
			}
		}

		// check for negative weight cycles
		for(int i=0; i<E; i++) {
			int u = graph.AdjacencyList.get(i).source;
			int v = graph.AdjacencyList.get(i).destination;
			int w = graph.AdjacencyList.get(i).weight;
			if(dist[u] != Integer.MAX_VALUE && dist[u] + w < dist[v]) {
				return true;
			}
		}
		return false;

	}

	public static void main(String[] args) {
		System.out.println(Integer.MAX_VALUE);
		Graph graph = new Graph(4, 4);
		
		// A negative cycle example
		graph.AdjacencyList.add(new Edge(0,1,-1));
		graph.AdjacencyList.add(new Edge(1,2,-1));
		graph.AdjacencyList.add(new Edge(2,3,-1));
		graph.AdjacencyList.add(new Edge(3,0,-1));

		if (isNegativeCycleBF(graph, 0)) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}