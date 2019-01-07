import time

from networkx.algorithms.community import LFR_benchmark_graph
import networkx as nx

def dict_sortedlist(dic:dict):
    ls=[[x,dic[x]] for x in dic]
    ls.sort(key=lambda x:x[1],reverse=True)
    return ls
p=open("follower_followee.csv","r")
data=p.readlines()
nodes=[]
G=nx.DiGraph()
for i in data[:-1]:
    j=i.split(",")
    nodes.append(j[2])
    nodes.append(j[4])
    G.add_edge(j[2],j[4])
de=open("net.txt","w",encoding="utf-8")
print("网络密度是")
dens=nx.density(G)
print(dens)
de.write(f"网络密度：{dens}\n")
# print("网络直径是")
# print(nx.diameter(G))
# print("网络半径")
# print(nx.radius(G))
print("平均聚类系数")
ave=nx.algorithms.average_clustering(G)
print(nx.algorithms.average_clustering(G))
de.write(f"平均聚类系数：{ave}\n")
time.sleep(1)
print("点度中心性")
deg=nx.degree_centrality(G)
ls=dict_sortedlist(deg)
for i in ls:
    de.write(f"{i[0]} {i[1]}\n")
time.sleep(1)
print("接近中心性")
clo=nx.closeness_centrality(G)
print(clo)
de.write(f"接近中心性：{clo}\n")
time.sleep(1)
print("中介中心性")
bet=nx.betweenness_centrality(G)
print(bet)
de.write(f"中介中心性：{bet}\n")


