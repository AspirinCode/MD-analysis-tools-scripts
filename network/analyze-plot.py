import pickle
import numpy as np
import matplotlib.pyplot as plt

def high_C_B_nodes(c_B, cutoff=0.05):
    """
    Count the nodes with betweenness centrality higher than cutoff;
    argu: c_B   : an array containing (node, centrality value)
          cutoff: optional, default=0.05
    return:
          node_string   : string, node list of satisfying ones;
          node_count    : integer, number of nodes satisfying cutoff;
    """
    node_count  = 0
    node_string = ""
    for i in range(len(c_B)):
        if c_B[i, 1] > 0.02:
            node_string += f" {int(c_B[i, 0])}"
            node_count  += 1
    return node_string, node_count

def plot_C_B_profile(c_B, plt_show=True):
    """
    Plot the betweenness centrality for each nodes.
    argu:
        c-B     : an array containing (node, centrality value);
        plt_show: whether to show the plot(True) or to save it(False);
    return:    
    """

    # define the residue range for secondary structure elements
    ss_range = {
        "ANK-H1": (4, 13),
        "ANK-H2": (17, 27),
        "ANK-H3": (46, 53),
        "ANK-H4": (61, 71),
        "ANK-H5": (81, 86),
        "ANK-H6": (103, 111),
        "ANK-H7": (139, 146),
        "ANK-H8": (151, 157),
        "ANK-H9": (175, 181),
        "ANK-H10": (187, 208),
        "CP1": (223, 231),
        "CP2": (235, 242),
        "Beta-1": (255, 262),
        "Beta-2": (264, 271),
        "PreS1-H1": (282, 290),
        "PreS1-H2": (296, 299),
        "S1": (302, 336),
        "S2": (357, 384),
        "S3": (397, 418),
        "S4": (424, 443),
        "S5": (446, 485),
        "S6": (545, 575),
        "Turret": (486, 519),
        "Pore-H": (520, 530),
        "TRP-H": (579, 597),
        "Beta-3": (613, 636)
    }

    # Group secondary structure elements into helix, auxillary helix, 
    # ankyrin repeats, beta sheets. Later assign different colors;
    helix       = ["S1", "S2", "S3", "S4", "S5", "S6"]
    auxi_helix  = ["PreS1-H1", "PreS1-H2", "Pore-H", "TRP-H"]
    ank_repeat  = ["ANK-H1", "ANK-H2", "ANK-H3", "ANK-H4", "ANK-H5", "ANK-H6",
                   "ANK-H7", "ANK-H8", "ANK-H9", "ANK-H10"]
    beta_sheet  = ["Beta-1", "Beta-2", "Beta-3"]

    # Plot the curve of betweenness centrality
    fig, ax = plt.subplots(figsize=(30,10))
    ax.plot(c_B[:,0], c_B[:,1])

    # Plot helix
    for hel in helix:
        ax.axvspan(ss_range[hel][0], ss_range[hel][1], alpha=0.4, 
                   color='#8dd3c7')
    # Plot auxillary helix    
    for hel in auxi_helix:
        ax.axvspan(ss_range[hel][0], ss_range[hel][1], alpha=0.4, 
                   color='#ffffb3')
    # Plot Ankyrin repeats
    for repeat in ank_repeat:
        ax.axvspan(ss_range[repeat][0], ss_range[repeat][1], alpha=0.4, 
                   color='#bebada')
    # Plot beta sheets
    for beta in beta_sheet:
        ax.axvspan(ss_range[beta][0], ss_range[beta][1], alpha=0.4, 
                   color='#fb8072')    

    # Set up figure layout
    ax.set_xlim(0, 650)
    ax.set_xlabel("Residue id of TRPV2", fontsize=20)
    ax.set_ylabel("Betweenness centrality", fontsize=20)
    if plt_show:
        plt.show()
    else:
        fig.savefig("monomer-betweenness-centrality.png", dpi=100)

if __name__ == "__main__":
    c_B = pickle.load(open("node_between_central_mono.pkl", "rb"))
    print(high_C_B_nodes(c_B, 0.02))
    print(high_C_B_nodes(c_B, 0.05))
    plot_C_B_profile(c_B)

