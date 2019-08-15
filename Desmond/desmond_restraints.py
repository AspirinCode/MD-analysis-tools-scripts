#!/bin/python
# Sample of 'raw-res-omm4-534-544.str':
# A 631 N 109.707733 95.6012115 87.3311005
# A 631 CA 110.181793 96.1428757 86.0887527
# A 631 C 110.370567 95.1250153 84.9113541
# A 631 O 109.836243 95.2783356 83.8277283
# A 632 N 111.019066 93.9858932 85.1694946
# A 632 CA 111.136856 92.8180695 84.3220444
# A 632 C 109.787491 92.2381973 83.9545441


# For proteins
with open('raw-res-omm4-534-544.str', 'r') as f:
    lines = f.readlines()

with open('restraint-def1.out','w') as wf1:
    with open('restraint-pos1.out','w') as wf2:
        for line in lines:
            str = line.split()
            #print(str)
            wf1.write('{\n')
            wf1.write('    name   = {}{}{}\n'.format(str[0],str[1],str[2]))
            wf1.write('    center = mass\n')
            wf1.write('    query  = "segname PRO{} and resid {} and name {}"\n'\
                      .format(str[0],str[1],str[2]))
            wf1.write('}\n')
            wf2.write('{\n')
            wf2.write('    type            = position\n')
            wf2.write('    groups          = [{}{}{}]\n'.format(str[0],str[1],str[2]))
            wf2.write('    position        = [ {} {} {} ]\n'.format(str[3], \
                                                                    str[4],str[5]))
            wf2.write('    form            = simple_harmonic\n')
            wf2.write('    spring_constant = 100\n')
            wf2.write('    equilibria      = [0]\n')
            wf2.write('}\n')

# For hetero atoms
with open('het-res-omm4.str', 'r') as f:
    lines = f.readlines()

with open('hete-res-omm4-def.out','w') as wf1:
    with open('hete-res-omm4-pos.out','w') as wf2:
        for line in lines:
            str = line.split()
            #print(str)
            wf1.write('{\n')
            wf1.write('    name   = {}{}\n'.format(str[0],str[1]))
            wf1.write('    center = mass\n')
            wf1.write('    query  = "segname HET{} and name {}"\n'\
                      .format(str[0],str[1]))
            wf1.write('}\n')
            wf2.write('{\n')
            wf2.write('    type            = position\n')
            wf2.write('    groups          = [{}{}]\n'.format(str[0],str[1]))
            wf2.write('    position        = [ {} {} {} ]\n'.format(str[2], \
                                                                    str[3],str[4]))
            wf2.write('    form            = simple_harmonic\n')
            wf2.write('    spring_constant = 100\n')
            wf2.write('    equilibria      = [0]\n')
            wf2.write('}\n')
