class Solution:
    def dfs(self, node, parent, visited, adj_list):
        visited[node] = 1

        for neighbor in adj_list[node]:
            if visited[neighbor] == 0:
                if self.dfs(neighbor, node, visited, adj_list):
                    return True
            elif neighbor != parent:
                return True

        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False


        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0] * n

        if self.dfs(0, -1, visited, adj_list):
            return False

        return sum(visited) == n