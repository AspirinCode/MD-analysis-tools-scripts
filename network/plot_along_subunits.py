import pickle
import numpy as np
import matplotlib.pyplot as plt

i = 1
fig = plt.figure(figsize=(30,30))
for pickle_file in pickle_list:
    c_B = pickle.load(open(pickle_file, "rb"))
    #plot_c_B(c_B, f"bet_centrality_with_{pickle_file[19:-4]}.png")


    ax = fig.add_subplot(5,1,i)
    #label = figname[-6:-4].upper()
    cb, = ax.plot(c_B[:,0], c_B[:,1], label=f"frame-{i}") # Label: 3-Angs
    #break
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

    helix = ["S1", "S2", "S3", "S4", "S5", "S6"]
    auxillary_helix = ["PreS1-H1", "PreS1-H2", "Pore-H", "TRP-H"]
    ank_repeat = ["ANK-H1", "ANK-H2", "ANK-H3", "ANK-H4", "ANK-H5", "ANK-H6", "ANK-H7",
                  "ANK-H8", "ANK-H9", "ANK-H10"]
    beta_sheet = ["Beta-1", "Beta-2", "Beta-3"]

    for hel in helix:
        ax.axvspan(ss_range[hel][0], ss_range[hel][1], alpha=0.4, color='#8dd3c7')

    for hel in auxillary_helix:
        ax.axvspan(ss_range[hel][0], ss_range[hel][1], alpha=0.4, color='#ffffb3')

    for repeat in ank_repeat:
        ax.axvspan(ss_range[repeat][0], ss_range[repeat][1], alpha=0.4, color='#bebada')

    for beta in beta_sheet:
        ax.axvspan(ss_range[beta][0], ss_range[beta][1], alpha=0.4, color='#fb8072')

    ax.set_xlim(0, 654)
    ax.set_xlabel("Residue id of TRPV2", fontsize=20)
    ax.set_ylabel("Betweenness centrality", fontsize=20)
    plt.legend(fontsize="xx-large", handles=[cb], loc="upper right")
    #break
    i += 1
