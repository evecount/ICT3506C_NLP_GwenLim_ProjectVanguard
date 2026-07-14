import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure the assets directory exists
os.makedirs('assets', exist_ok=True)

def generate_topology_anomaly():
    """Generates a graph showing intense asymmetrical targeting (Axiom B)"""
    G = nx.DiGraph()
    
    # Generate background ambient nodes
    ambient_nodes = range(20)
    for _ in range(30):
        u, v = np.random.choice(ambient_nodes, 2, replace=False)
        G.add_edge(u, v, weight=np.random.uniform(0.1, 0.5))

    # Add the anomaly (Shark isolating the Lamb)
    shark = 20
    lamb = 21
    rescuer = 22
    
    # Shark targets lamb heavily
    for _ in range(8):
        G.add_edge(shark, lamb, weight=np.random.uniform(2.0, 3.5))
        
    # Lamb has weak links to outside, Shark has NO links to outside except Lamb
    G.add_edge(lamb, rescuer, weight=0.5)
    G.add_edge(rescuer, lamb, weight=0.5)
    
    # Plotting
    plt.figure(figsize=(10, 8), facecolor='white')
    pos = nx.spring_layout(G, seed=42, k=0.5)
    
    # Draw ambient nodes
    nx.draw_networkx_nodes(G, pos, nodelist=ambient_nodes, node_color='#cbd5e1', node_size=100, alpha=0.6)
    nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v in G.edges() if u < 20 and v < 20], alpha=0.2, edge_color='#94a3b8')
    
    # Draw actors
    nx.draw_networkx_nodes(G, pos, nodelist=[shark], node_color='#ef4444', node_size=300, label="Isolator (Shark)")
    nx.draw_networkx_nodes(G, pos, nodelist=[lamb], node_color='#38bdf8', node_size=300, label="Target (Lamb)")
    nx.draw_networkx_nodes(G, pos, nodelist=[rescuer], node_color='#22c55e', node_size=200, label="Rescuer (Star)")
    
    # Draw intense anomalous edges
    anomalous_edges = [(shark, lamb)]
    nx.draw_networkx_edges(G, pos, edgelist=anomalous_edges, edge_color='#ef4444', width=2.5, arrowsize=20, connectionstyle='arc3,rad=0.1')
    
    # Draw rescuer edges
    nx.draw_networkx_edges(G, pos, edgelist=[(rescuer, lamb), (lamb, rescuer)], edge_color='#22c55e', width=1.5)
    
    plt.title("Axiom B: Targeting Asymmetry ($I_\\alpha$)", fontsize=16, pad=20)
    plt.legend(scatterpoints=1, frameon=True, loc='upper left')
    plt.axis('off')
    
    plt.savefig('assets/topology_anomaly.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def generate_cross_platform_stylometry():
    """Generates a graph showing multi-channel linkage"""
    plt.figure(figsize=(12, 6), facecolor='white')
    
    platforms = ['Telegram (Node A)', 'Discord (Node B)', 'WhatsApp (Node C)']
    colors = ['#0088cc', '#5865F2', '#25D366']
    
    # Generate random stylized vectors
    t = np.linspace(0, 10, 100)
    
    for i, (plat, color) in enumerate(zip(platforms, colors)):
        # Base vector signature (the "Authorial DNA")
        base_signature = np.sin(t) + np.sin(2.5 * t) * 0.5
        
        # Add platform-specific noise
        noise = np.random.normal(0, 0.15, 100)
        
        # Shift slightly for visual separation
        y_offset = (2 - i) * 3
        
        plt.plot(t, base_signature + noise + y_offset, color=color, alpha=0.7, linewidth=2, label=plat)
        
        # Add a "centroid" line showing the perfect alignment
        plt.plot(t, base_signature + y_offset, color='#1e293b', linestyle='--', alpha=0.8, linewidth=1.5)
    
    # Add vertical mapping lines to show vector alignment
    for x_val in [2, 5, 8]:
        plt.axvline(x=x_val, color='#ef4444', linestyle=':', alpha=0.6, linewidth=2)
        
    plt.title("Stylometric Inter-Identity Vector Mapping ($D_{ST}$)", fontsize=16, pad=20)
    plt.xlabel("Temporal Operation Window ($t$)", fontsize=12)
    plt.ylabel("Semantic Vector ($v \\in \mathbb{R}^d$)", fontsize=12)
    
    plt.yticks([])
    plt.xticks([])
    plt.legend(loc='upper right', frameon=True)
    
    plt.savefig('assets/cross_platform_stylometry.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    print("Generating topological graphs...")
    generate_topology_anomaly()
    generate_cross_platform_stylometry()
    print("Successfully generated graphs in /assets/")
