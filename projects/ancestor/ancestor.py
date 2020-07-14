from util import Stack


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('that vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack
        dfs_path = Stack()
        # path to starting vertex
        dfs_path.push([starting_vertex])
        # set for visited vetices
        visited_vertices = set()
        # while path is not empty
        while dfs_path.size() > 0:
            # pop the first path
            curr_path = dfs_path.pop()
            # take last vertex in path
            curr_path_last_vertex = curr_path[-1]
            # if we havent been there yet
            if curr_path_last_vertex not in visited_vertices:
                # check if current is the destination
                if curr_path_last_vertex == destination_vertex:
                    # return the path if it is
                    return curr_path
                # mark as visited if it is not
                else:
                    # get the neighbors / make new versions on the path
                    visited_vertices.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)
                    for neighbor in neighbors:
                        # duplicate the path
                        curr_path_copy = curr_path[:]
                        # add the neighbor
                        curr_path_copy.append(neighbor)
                        # add the new path
                        dfs_path.push(curr_path_copy)


def earliest_ancestor(ancestors, starting_node):
    pass