import matplotlib.pyplot as plt
import mdtraj as md
from contact_map import ContactMap

pdb_list = [ "../pdb_dir_1_500ns/frame0.pdb",
            "../pdb_dir_5001_6000ns/frame4164.pdb"]

# Program takes about several minutes to finish
# It is a bit slow;
for i in range(len(pdb_list)):
    pdb = md.load_pdb(pdb_list[i])
    frame_contacts = ContactMap(pdb[0], cutoff=1.5)
    (fig, ax) = frame_contacts.residue_contacts.plot(cmap='seismic', vmin=-1, vmax=1)
    plt.xlabel("Residue")
    plt.ylabel("Residue")
    fig.savefig(f'cont-map-{i}.pdf', format='pdf', dpi=500)
    plt.close()

# Calculate the difference between two contact maps
diff = contacts[1] - contacts[0]
(fig, ax) = diff.residue_contacts.plot(cmap='seismic', vmin=-1, vmax=1)
plt.xlabel("Residue")
plt.ylabel("Residue")
fig.savefig(f'cont-map-diff.pdf', format='pdf', dpi=500)
plt.close()
