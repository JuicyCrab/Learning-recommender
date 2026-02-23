
#create the knowledge graph data structure 
# Class should have init, add edge, shortest path with BFS, has cycle 
# has cycle will ensure that the prereq of A is B and B is not a prereq of A because this will continuously loop 
# useful functions is shortest path for generating learning paths and predecessors for checking what a user needs to know before reaching target concept(DAG validation [direct acyclic graph])

from collections import deque 

class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    
    def add_node(self, concept, difficulty=None, description=None) -> bool:
        self.nodes[concept] = {
            'difficulty': difficulty,
            'description': description
        }
        self.edges[concept] = []
        return True 
    
    def add_edge(self, concept, other_concept) -> bool:
        if concept not in self.nodes or other_concept not in self.nodes:
            return False
        self.edges[concept].append(other_concept)
        return True
    
    def has_cycle(self, start_node) -> bool:
        """_summary_
        Stack: responsible for what to explore 
        current_path: active route to the node 
        visited: all the nodes processed already 
        Args:
            start_node (_type_): _description_

        Returns:
            bool: _description_ 
        """
        if start_node not in self.nodes:
            return "Pass an actual value in the graph"
        visited = set()
        current_path = set()
        stack = deque([start_node])
        BACKTRACK = object() 

        while stack:
            current_node = stack.pop()
            if isinstance(current_node, tuple) and current_node[0] is BACKTRACK: 
                current_path.remove(current_node[1])
                continue 
            if current_node not in visited:
                visited.add(current_node)
                current_path.add(current_node)
                stack.append((BACKTRACK, current_node))
                for edge in self.edges[current_node]:
                    if edge in visited and edge in current_path:
                        return True 
                    stack.append(edge)

        return False 
    
    
    def get_learning_path(self):
        pass 
    