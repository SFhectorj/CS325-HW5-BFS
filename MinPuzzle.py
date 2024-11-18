from collections import deque

def minEffort(puzzle):
    """
    :param puzzle:
    This function will use binary search and  breadth-first search to traverse a 2D matrix.
    The algorithm will reach the destination with minimal effort bu finding the lowest maximum difference of the column/row heights.
    """
    number_of_columns = len(puzzle[0])
    number_of_rows = len(puzzle)

    def reachDestination():
        """
        This is a helper function to check if reaching the bottom right corner is feasible using the given maximum effort.
        """
        # Start with a queue; top left corner (0,0)
        current_queue = deque([(0, 0)])
        # Using a set will automatically remove dupes
        already_visited = set()
        already_visited.add((0, 0))

        # BREADTH-FIRST SEARCH
        while current_queue:
            # popleft() method in Python is used to remove and return the first element (leftmost element) from a deque object.
            number_of_rows = current_queue.popleft()



    return
