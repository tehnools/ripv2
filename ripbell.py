routes = [(1, 2, 1),(1,7, 8), (1,6, 5), (2,3, 3),
(3,4, 4), (6,5, 1), (5,4, 2),(7, 4, 6)] #(current_router, next_router, metric)

def bellman_ford(routes):
    infinity = 16
    routing_table = []
    nodes = set()
    router-id = 1

    for rid,hop,metric in routes:
        if rid not in nodes:
            nodes.add(rid)


    for node in nodes:
        rounting_table.append([node, None, infinity])

    # while(iteration < len(nodes)):

    return routing_table

print(bellman_ford(routes))
