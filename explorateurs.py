import numpy as np
import pandas as pd

edges_df = pd.read_csv("./explorateurs/parcours_explorateurs.csv")



seq_starting_nodes = edges_df[edges_df ["type_aretes"] == "depart"]["noeud_amont"].values


seq_ending_nodes = edges_df[edges_df ["type_aretes" ] == "arrivee"]["noeud_aval"].values



dict_upstream_downstream = {}
for _ , row in edges_df.iterrows():
    dict_upstream_downstream[row["noeud_amont"]] = row ["noeud_aval"]

# dict_upstream_downstream = {[row["noeud_amont"]] : ["noeud_aval"] for _ , row in edges_df.iterrows()}

for upstream_node, downstream_node in dict_upstream_downstream.items():
    print(upstream_node, downstream_node)


# dict_amont_aval =     key : noeud amont | value : noeud aval associé

