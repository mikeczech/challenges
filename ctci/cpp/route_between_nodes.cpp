#include <cassert>
#include <deque>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

template <typename Vertex> class DirectedGraph {
  using Vertices = std::vector<Vertex>;
  using Successors = std::unordered_map<Vertex, std::vector<Vertex>>;

private:
  Vertices vertices;
  Successors successors;

public:
  DirectedGraph();
  void add_vertex(const Vertex &vertex);
  void add_successor(const Vertex &vertex, const Vertex &successor);
  const std::vector<Vertex> &get_successors(const Vertex &vertex);
  bool is_reachable(const Vertex &source, const Vertex &target);
};

template <typename Vertex> DirectedGraph<Vertex>::DirectedGraph() {}

template <typename Vertex>
void DirectedGraph<Vertex>::add_vertex(const Vertex &vertex) {
  this->vertices.push_back(vertex);
  this->successors.insert(
      std::pair<Vertex, std::vector<Vertex>>(vertex, std::vector<Vertex>()));
}

template <typename Vertex>
void DirectedGraph<Vertex>::add_successor(const Vertex &vertex,
                                          const Vertex &successor) {
  this->successors[vertex].push_back(successor);
}

template <typename Vertex>
const std::vector<Vertex> &
DirectedGraph<Vertex>::get_successors(const Vertex &vertex) {
  return this->successors[vertex];
}

template <typename Vertex>
bool DirectedGraph<Vertex>::is_reachable(const Vertex &source,
                                         const Vertex &target) {
  std::deque<Vertex> queue;
  queue.push_back(source);
  std::unordered_set<Vertex> visited;
  visited.insert(source);

  while (!queue.empty()) {
    Vertex current = queue.front();
    queue.pop_front();
    if (target == current) {
      return true;
    }
    visited.insert(current);
    for (const auto &succ : this->successors[current]) {
      if (visited.count(succ) == 0) {
        queue.push_back(succ);
      }
    }
  }
  return false;
}

int main(int argc, char **args) {
  DirectedGraph<int> graph;
  graph.add_vertex(1);
  graph.add_vertex(2);
  graph.add_vertex(3);
  graph.add_vertex(4);

  graph.add_successor(1, 2);
  graph.add_successor(2, 3);
  graph.add_successor(4, 3);

  std::cout << "Evaluating test cases..." << std::endl;

  std::cout << (graph.is_reachable(1, 3) == true) << std::endl;
  std::cout << (graph.is_reachable(1, 4) == false) << std::endl;
  std::cout << (graph.is_reachable(2, 3) == true) << std::endl;

  std::cout << "Done" << std::endl;
}
