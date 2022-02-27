"""
Created on Sun Feb 27 01:02:59 2022

@author: NIKHIL
"""

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

size = 7
edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))
