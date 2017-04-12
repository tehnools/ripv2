routes = [(1, 2, 1),(1,7, 8), (1,6, 5), (2,3, 3),
(3,4, 4), (6,5, 1), (5,4, 2),(7, 4, 6)] #(current_router, next_router, metric)


def bellman_ford(routes):
    infinity = 16
    routing_table = dict()
    nodes = set()
    router_id = 1
    iteration = 0
    visited = set()

    for rid,hop,metric in routes:
        if rid not in nodes:
            nodes.add(rid)

    for node in nodes:
        routing_table[node] = [None, infinity]

    while iteration < len(nodes):
        for rid, hop, metric in sorted(routes):
            if rid == router_id:
                routing_table[0][2] = 0
            elif rid not in visited:
                iteration += 1

    return routing_table

print(bellman_ford(routes))
