def traverse(node, visited):
    visited.append(node)
    for neighbour in paths_graph[node]:
        if neighbour not in visited or neighbour.isupper():
            traverse(neighbour, visited.copy())
    all_paths.append(visited)
    
def traverse2(node, visited):    
    visited.append(node)
    for neighbour in paths_graph[node]:
        lower_nodes = [neighbour for neighbour in visited if neighbour.islower()]
        num_dups = len(lower_nodes) - len(set(lower_nodes))
        if (num_dups == 0 and neighbour != 'start' and neighbour != 'end' and neighbour.islower()) or (neighbour not in visited or neighbour.isupper()):
            traverse2(neighbour, visited.copy())
    all_paths.append(visited)

if __name__ == "__main__":
    with open('data/input12.txt', 'r') as f:
        paths = [path.split('-') for path in f.read().split('\n')[:-1]]
    paths_graph = {}
    for a, b in paths:
        paths_graph[a] = paths_graph.get(a, set()).union({b})
        paths_graph[b] = paths_graph.get(b, set()).union({a})
        
    all_paths = []
    traverse('start', [])
    print(f'Part 1: {len([path for path in all_paths if path[-1] == "end"])}')
    
    all_paths = []
    traverse2('start', [])
    print(f'Part 2: {len([path for path in all_paths if path[-1] == "end"])}')