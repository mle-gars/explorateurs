import pandas

def prepare_data(edges_df):

	seq_starting_nodes = edges_df[edges_df["type_aretes"] == "depart"]["noeud_amont"].values

	seq_ending_nodes = edges_df[edges_df["type_aretes"] == "arrivee"]["noeud_aval"].values

	dict_upstream_downstream = {} # key : noeud_amont => value : noeud_aval
	for _, row in edges_df.iterrows():
		dict_upstream_downstream[row["noeud_amont"]] = row["noeud_aval"]

	# proposition alternative 1
	# dict_upstream_downstream = {row["noeud_amont"] : row["noeud_aval"] for _, row in edges_df.iterrows()} 


	# proposition alternative 2
	# for upstream_node, downstream_node in zip(edges_df["noeud_amont"].values, edges_df["noeud_aval"].values):
	# 	dict_upstream_downstream[upstream_node] = downstream_node

	return seq_starting_nodes, seq_ending_nodes, dict_upstream_downstream


def get_explorators_paths(seq_starting_nodes, seq_ending_nodes, dict_upstream_downstream, edges_df):
    for starting_node in seq_starting_nodes:
        explorator_path = [starting_node]
        
        total_distance = 0
        while explorator_path[-1] not in seq_ending_nodes:
            
            current_node = explorator_path[-1]
            next_node = dict_upstream_downstream[current_node]
            
            edge = edges_df[(edges_df["noeud_amont"] == current_node) & (edges_df["noeud_aval"] == next_node)]
            
            if not edge.empty:
               
                total_distance += edge["distance"].values[0]
                
                explorator_path.append(next_node)
                
            else:
                
                print(f"No edge found between {current_node} and {next_node}")
                break
        
        print("Explorator Path:", explorator_path)
        print(f"Total Distance: {total_distance:.2f} km")

if __name__ == "__main__":
    edges_df = pandas.read_csv("./parcours_explorateurs.csv")
    starting_nodes, ending_nodes, dict_upstream_downstream = prepare_data(edges_df)
    get_explorators_paths(starting_nodes, ending_nodes, dict_upstream_downstream, edges_df)

