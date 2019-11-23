from collections import deque

def min_depth(root):
    queue = deque()
    depth = 0
    if not root:
        return depth

    queue.append(root)

    while queue:
        depth += 1
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()

            if not current_node.left and not current_node.right:
                return depth

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

    return depth
