def enQueue(queue, i):
  queue.append(i)
def deQueue(queue):
  return queue.pop(0)
def is_empty(queue):
  if len(queue) == 0:
    return True
  else:
    return False
def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = []
  enQueue(bfs_queue, vertex_and_path)
  visited = set()
  
  while is_empty(bfs_queue)==False:
    current_vertex, path = deQueue(bfs_queue)
    visited.add(current_vertex)
	
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor == target_value:
          return path + [neighbor]
		  
        else:
          enQueue(bfs_queue, [neighbor, path + [neighbor]])

# def dfs(graph, current_vertex, target_value, visited = None):
#   if visited is None:
#     visited = []
	
#   visited.append(current_vertex)
  
#   if current_vertex == target_value:
#     return visited
	
#   for neighbor in graph[current_vertex]:
#     if neighbor not in visited:
#       path = dfs(graph, neighbor, target_value, visited)
	  
#       if path:
#         return path

def push(stack, x):
    stack.append(x)
def pop(stack):
    return stack.pop()
def is_empty(stack):
    if len(stack) == 0:
      return True
    else:
      return False
def dfs(graph, start_vertex, target_value):
    stack=[]
    visited = []
    push(stack, start_vertex)

    while is_empty(stack) == False:
        current_vertex = pop(stack)
        if current_vertex == target_value:
            return visited
        visited.append(current_vertex)

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                push(stack, neighbor)
    return None