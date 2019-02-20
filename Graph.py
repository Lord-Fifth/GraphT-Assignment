import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
color_map=[]
g.add_node("a")
color_map.append('blue')
g.add_node("b")
color_map.append('yellow')
g.add_node("c")
color_map.append('magenta')
g.add_node("d")
color_map.append('cyan')
g.add_node("g")
color_map.append('green')
g.add_node("h")
color_map.append('orange')
g.add_node("i")
color_map.append('red')
g.add_node("j")
color_map.append('purple')
g.add_edges_from([("a","h"),("a","i"),("a","g"),("b","g"),("b","h"),("b","j"),("c","g"),("c","i"),("c","j"),("d","h"),("d","i"),("d","j")])
pos = {"a":(0,6),
       "b":(0,4),
       "c":(0,2),
       "d":(0,0),
       "g":(2,6),
       "h":(2,4),
       "i":(2,2),
       "j":(2,0)}
print nx.info(g)
if(nx.is_eulerian(g)):
    print("Graph is Eulerian")
else:
    print("Graph is not Eulerian")
fh=open("name.txt",'wb')
nx.write_edgelist(g,fh)
nx.draw(g,pos,node_color=color_map,with_labels=True)
plt.savefig('label.png')
plt.show()