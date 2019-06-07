# Assemble the system

## Need to mutate K<sup>+</sup> to Ca<sup>2+</sup> ions
The intuition is to use text editing tools to mutate the ions. However, due to calcium ions are divalent while pottasium ions are monovalent, we need to delete some K<sup>+</sup> ions at first. For example, if we want to mutate 4 K<sup>+</sup> ions to 4 Ca<sup>2+</sup> ions, we need to delete 4 K<sup>+</sup> ions first to count for the extra valence in Ca<sup>2+</sup> ions. Essentially we can do that by deleting 4 rows of K<sup>+</sup> in Vim, yet that can cause the atom number to be not consecutive. So we delete the ions via CHARMM.

- Use CHARMM script to delete 4 K<sup>+</sup> ions (assume want to mutate 4 K<sup>+</sup> to 4 Ca2+)  
  See `step5.1_rename.inp`.
- Text-edit **'POT'** to **'CAL'**, also change the mass and charge accordingly
