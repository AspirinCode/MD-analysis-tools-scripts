# Assemble the system

## Need to mutate K+ to Ca2+ ions
The intuition is to use text editing tools to mutate the ions. However, due to calcium ions are divalent while pottasium ions are monovalent, we need to delete some K+ ions at first. For example, if we want to mutate 4 K+ ions to 4 Ca2+ ions, we need to delete 4 K+ ions first to count for the extra valence in Ca2+ ions. Essentially we can do that by deleting 4 rows of K+ in Vim, yet that can cause the atom number to be not consecutive. So we delete the ions via CHARMM.

- Use CHARMM script to delete 4 K+ ions (assume want to mutate 4 K+ to 4 Ca2+)  
  See `step5.1_rename.inp`.
- Text-edit 'POT' to 'CAL', also change the mass and charge accordingly
