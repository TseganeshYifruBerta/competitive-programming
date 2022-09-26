class UnionFind:
    def __init__(self) -> None:
        self.parents = defaultdict(lambda: -1)
        
    def find(self, node):
        
        if self.parents[node] == -1:
            return node
        
        return self.find(self.parents[node])
    
    def union(self, node1, node2):
        
        p1, p2 = self.find(node1), self.find(node2)
        
        if p1 != p2:
            self.parents[p1] = p2


class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        
        uf = UnionFind()
        
        for equation in equations:
            if equation[1:-1] == "!=":
                continue

            uf.union(equation[0], equation[-1])
            
        return not any(
            uf.find(equation[0]) == uf.find(equation[-1])
            for equation in equations
            if equation[1:-1] == "!="
        )