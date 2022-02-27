def FiberLink(wl):
    (edges, component) = ([], {})

    for u in wl.keys():
        edges.extend([(d,u,v) for v, d in wl[u]])
        component[u] = u
    edges.sort()
    cost = 0
    for d,u,v in edges:
        if component[u] != component[v]:
            cost+=d
            c = component[u]
            for i in wl.keys():
                if component[i] == c:
                    component[i] = component[v]

    return cost
