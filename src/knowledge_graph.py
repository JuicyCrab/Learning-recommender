
"""
File is responsible for creating the knowledge graph, which abstracts the 
prerequisites and the path for learning topics. A graph data structure is 
implemented with the nodes as the concepts and the edges represent the 
relationship between concepts. 
"""


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
        """
        Checks for a cycle and ensures that the prerequisite of A is B 
        and B is not a prerequisite of A. This continuous loop could influence 
        the learning path computation and will be the direct acyclic validation(DAG).
        """
        
        if start_node not in self.nodes:
            return "Pass an actual value in the graph"
        visited = set()
        current_path = set()
        stack = deque([start_node])
        BACKTRACK = object() # identifier when to remove node from current path, when all its neighbors have been visited 

        while stack:
            concept = stack.pop()
            if isinstance(concept, tuple) and concept[0] is BACKTRACK: 
                current_path.remove(concept[1])
                continue 
            if concept not in visited:
                visited.add(concept)
                current_path.add(concept)
                stack.append((BACKTRACK, concept)) # before adding edges, since it should be removed after all its neighbors(follows stack LIFO)
                for edge in self.edges[concept]:
                    if edge in visited and edge in current_path: 
                        return True 
                    stack.append(edge)

        return False 
    
    
    def get_learning_path(self, start_concept, goal_concept, already_known_concepts = []) -> list: # user wants to instruct what they want to know
        """
        Finds the optimal path for generating learning paths given what the user 
        wants to know and predecessors for verifying what a user needs to know
        before reaching target concept. Utilizes the direct acyclic graph to 
        perform properly. The already known concepts parameter is the initial
        knowledge the user already has which can be skipped. Used a dictionary 
        for memory purposes and efficiency when scale increases.
        """
        if start_concept not in self.add_node or goal_concept not in self.nodes:
            print("Need a start concept and final concept")
            return []
        
        queue = deque([start_concept])
        visited = {start_concept} #needed since concepts can be already seen/cycle 
        parent = {start_concept: None} # tuple approach stores every journey while the dict only stores who introduces you to each node 
        while queue:
            concept = queue.popleft()
        
            for edge in self.edges[concept]:
                if edge not in visited:
                    parent[edge] = concept
                    queue.append(edge)
                    visited.add(edge)
        
        # if goal concept is not in the path 
        if goal_concept not in parent:
            print("No path exists between these concepts")
            return []
        
        #path reconstruction 
        learning_path = []
        current_node = goal_concept
        while current_node is not None:
            if current_node not in already_known_concepts:
                learning_path.append(current_node)
            current_node = parent[current_node]
        
        return learning_path.reverse() #does it in place  