# CHARMM 

- Mod function in CHARMM 
```
! To get c=MOD(a,b)
calc c @a - @b * INT( @a / @b )
```

- Traj-specific
```
traj-spec::= [FIRSt int] [NUNIts int] [NSKIp int] [BEGIn int] [STOP int]
````

- Array in CHARMM
```
A command line parameter token can now be a string rather than just one of the single characters 0-9,a-z,A-Z. For substitution a token is indicated by the use of the @ character as before. Arrays can be made by preceeding the array indices with '@@', e.g. @segid@@j can be used to loop over parameter tokens segid1, segid2, 
```
