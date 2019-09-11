# CHARMM 

- Mod function in CHARMM 
```
! To get c=MOD(a,b)
calc c @a - @b * INT( @a / @b )
```

- Traj-specific
`
traj-spec::= [FIRSt int] [NUNIts int] [NSKIp int] [BEGIn int] [STOP int]
`
