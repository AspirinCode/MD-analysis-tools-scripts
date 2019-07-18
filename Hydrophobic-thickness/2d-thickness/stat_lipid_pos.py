#!/usr/bin/python
import os,sys,math

filename = sys.argv[1]
simlen = int(sys.argv[2])
bsize=10 # int(sys.argv[4]) # block size -------------------------------

# number of blocks
nblck = int(simlen/bsize)

# set bin width...
xmin,xmax=(-90.0,90.0)
# dx=0.5 # 0.5 A bin
dx=1.0
# dx=0.4
nbin=int((xmax-xmin)/dx+1)

zmin=-45.0; zmax=45; dz=1.0 # dz=0.5; # z
nbinz=int((zmax-zmin)/dz+1)

#---------------------------
# INITIALIZE HISTOGRAM
#---------------------------
# th_t     : z-position (top)
# th_b     : z-position (bottom)
# th_bi    : hydrophobic thickness (bilayer)
# hist_prot: prot density
# histz    : z-distribution of lipids
#
def init_histogram():
  th_t,sth_t,hist_t=([],[],[])
  th_b,sth_b,hist_b=([],[],[])
  th_bi,sth_bi,hist_bi=([],[],[])
  hist_prot=[]
  histz=[]

  for i in range(0,nbin):
    th_t.append([]); sth_t.append([]); hist_t.append([]);
    th_b.append([]); sth_b.append([]); hist_b.append([]);
    th_bi.append([]); sth_bi.append([]); hist_bi.append([]);
    hist_prot.append([])
    for j in range(0,nbin):
      th_t[i].append(0.0); sth_t[i].append(0.0); hist_t[i].append(0.0);
      th_b[i].append(0.0); sth_b[i].append(0.0); hist_b[i].append(0.0);
      th_bi[i].append(0.0); sth_bi[i].append(0.0); hist_bi[i].append(0.0);
      hist_prot[i].append(0.0);

  [histz.append(0.0) for i in range(0,nbinz)];

  return (th_t,sth_t,hist_t,th_b,sth_b,hist_b,th_bi,sth_bi,hist_bi,hist_prot,histz)

#-----------------------------------------
# READ DATA
#-----------------------------------------
# Set the ranges for each frame to read from raw data:
#	(ist[frame],ied[frame])
#
# Each line of raw data has a format:
#	time	lipid_resid	x	y	z
#
# Returns the input lines, number of frame (nframe), (ist,ied)
#
def read_data(fin):
  tmpl=open(fin,'r').readlines()
  ist,ied=[],[]
  nline=len(tmpl)
  tist="-1.0" # garbage value of time
  for i in range(0,nline):
    tmpi=tmpl[i].split()[0] # time
    if (tmpi != tist):
      if (len(ist)==0): pass
      else: ied.append(i) # end range+1 of the previous frame
      ist.append(i); tist=tmpi;
  # put final frame range+1
  ied.append(nline)

  # check size
  if (len(ist) != len(ied)):
      print("frame ranges were not correctly calculated")
      sys.exit(0)
  nframe=len(ist)

  return (tmpl,nframe,ist,ied)

#-------------------------------------
# READ FRAME DATA & UPDATE HISTOGRAM
#
# assume hist2d is setup
#-------------------------------------
# inx  : frame number
# th   : thickness
# sth  : for standard deviation
# hist : histogram (xy) 
# histz: z-histrogram
# ist  : starting lines for each frame
# ied  : (end line -1) for each frame
#
def update_thick_hist(inx,th,sth,hist,histz,ist,ied,tmpl):
  for i in range(ist[inx],ied[inx]):
    tmps=tmpl[i].split()
    # time ilip x y z
    tmp1,tmp2=(float(tmps[2]),float(tmps[3]))
    tmpz=float(tmps[4])
    inx1=int((tmp1-xmin)/dx+0.5)
    inx2=int((tmp2-xmin)/dx+0.5)
    # print "inx1=%d inx2=%d nbin=%d icl=%d nclust=%d" % (inx1,inx2,nbin,icl,nclust)
    th[inx1][inx2]+=tmpz;
    sth[inx1][inx2]+=tmpz**2;
    hist[inx1][inx2]+=1.0

    inxz=int((tmpz-zmin)/dz+0.5)
    histz[inxz]+=1.0

  return (th,sth,hist,histz)

#-------------------------------------
# UPDATE CAV1 density profile
#-------------------------------------
def update_prot_hist_frame(inx,hist,ist,ied,tmpl):
  for i in range(ist[inx],ied[inx]):
    tmps=tmpl[i].split()
    # time iprot x y z
    tmp1,tmp2=(float(tmps[2]),float(tmps[3]))
    inx1=int((tmp1-xmin)/dx+0.5)
    inx2=int((tmp2-xmin)/dx+0.5)
    hist[inx1][inx2]+=1.0
  return hist

#-------------------------------------
# DO STATISTICS
#------------------------------------
# update average & standard deviation
#
# th  : sum of thickness   -> average
# sth : sum of thickness^2 -> standard deviation
# hist: number of data for a given bin
#
def do_stat(th,sth,hist):
  # update th,sth
  for i in range(0,nbin):
    for j in range(0,nbin):
      tth=th[i][j]; tsth=sth[i][j]; thist=hist[i][j];
      if (int(thist)==0): continue # skip
      th[i][j]/=thist # average
      tsth=tsth/thist-(tth/thist)**2;
      sth[i][j]=math.sqrt(abs(tsth))

  return (th,sth)

#-------------------------------------
# PRINT OUTPUT
#-------------------------------------
# print leaflet thickness
def write_leaflet(fout,th,sth,hist):
  th_max,th_min=(-1000.0,1000.0)

  # get total histogram
  tsum=0
  for i in range(0,nbin):
    for j in range(0,nbin): tsum+=hist[i][j]

  sout=""
  # write the histogram only when tsum > 0: i.e., there is a least one data point.
  if (tsum > 0):
    for i in range(0,nbin):
      cx=xmin+i*dx
      for j in range(0,nbin):
        cy=xmin+j*dx
        thist=hist[i][j];tth=th[i][j];

        if (int(thist) != 0):
          if (tth>th_max): th_max=tth
          if (tth<th_min): th_min=tth

        sout+="%g %g %g %g %g\n" % (cx,cy,tth,thist,sth[i][j])

  stmp="# max_th= %g min_th= %g\n" % (th_max,th_min)
  sout+=stmp
  print(stmp)
  open(fout,'w').write(sout)
  return

# print bilayer thickness
def write_bilayer(fout,th,hist):
  th_max,th_min=(-1000.0,1000.0)

  # get total histogram
  tsum=0
  for i in range(0,nbin):
    for j in range(0,nbin): tsum+=hist[i][j]

  sout=""
  # write the histogram only when tsum > 0
  if (tsum > 0):
    for i in range(0,nbin):
      cx=xmin+i*dx
      for j in range(0,nbin):
        cy=xmin+j*dx
        thist=hist[i][j];tth=th[i][j];

        if (int(thist) != 0):
          if (tth>th_max): th_max=tth
          if (tth<th_min): th_min=tth

        sout+="%g %g %g %g\n" % (cx,cy,tth,thist)
    
  stmp="# max_th= %g min_th= %g\n" % (th_max,th_min)
  sout+=stmp
  # print stmp
  open(fout,'w').write(sout)
  return

# print prot density
def write_prot(fout,hist):
  cxmin,cxmax=(xmax,xmin)
  cymin,cymax=(xmax,xmin)
  max_hist=0

  # get total histogram
  tsum=0
  for i in range(0,nbin):
    for j in range(0,nbin): tsum+=hist[i][j]

  sout=""
  # write the histogram only when tsum > 0
  if (tsum > 0):
    for i in range(0,nbin):
      cx=xmin+i*dx
      for j in range(0,nbin):
        cy=xmin+j*dx
        thist=hist[i][j];

        if (int(thist) != 0):
          if (cx>cxmax): cxmax=cx
          if (cx<cxmin): cxmin=cx
          if (cy>cymax): cymax=cy
          if (cy<cymin): cymin=cy
          if (thist>max_hist): max_hist=thist

    for i in range(0,nbin):
      cx=xmin+i*dx
      for j in range(0,nbin):
        cy=xmin+j*dx
        thist=hist[i][j];
        sout+="%g %g %g %g\n" % (cx,cy,thist,max_hist)

  stmp ="# xmin= %g xmax= %g\n" % (cxmin,cxmax)
  stmp+="# ymin= %g ymax= %g\n" % (cymin,cymax)

  sout+=stmp

  ## print stmp
  open(fout,'w').write(sout)
  return

# print z-distribution of lipid position
def write_zlip(fout,hist):
  czmin,czmax=(zmax,zmin)
  max_hist=0; imax=-1;
  # get total histogram & max_hist
  tsum=0
  sout=""
  for i in range(0,nbinz):
    cz=zmin+i*dz; thist=hist[i];
    sout+="%g %g\n" % (cz,thist)
    tsum+=thist
    if (thist>max_hist): (imax,max_hist)=(i,thist)
  # additional data
  cz=zmin+dz*(imax+0.5)
  sout+="# zmax imax histmax tot_hist\n"
  sout+="# %g %d %d %d\n" % (cz,imax,max_hist,tsum)

  open(fout,'w').write(sout)
  ## print sout
  return

#--------------------------------------------
# MAIN
#--------------------------------------------
print("# JOB STARTS")

print("# INITIALIZE HISTOGRAM ARRAYS")
#
# initialize_histogram arrays
# 
# th_t,sth_t : top leaflet thickness & standard deviation
# hist_t     : histogram of lipid xy position in 2D (number of samples)
#
# histz      : histogram of z-position of lipids
#
# hist_prot  : histogram of prot density
#
th_t,sth_t,hist_t,th_b,sth_b,hist_b,th_bi,sth_bi,hist_bi,hist_prot,histz=init_histogram()

# loop over blocks
for iblck in range(0,nblck):
  print("# BLOCK %d / %d" % (iblck+1,nblck))

  fin_top = filename+'_top.plo'
  fin_bot = filename+'_bot.plo'
  fin_hapos = filename+'_hapos.plo'

  print("# BLOCK%d: READING RAW DATA" % (iblck+1))
  # read leaflet data
  print("# BLOCK%d:	TOP LEAFLET" % (iblck+1))
  tmpl_t,nframe_t,ist_t,ied_t=read_data(fin_top)
  print("# BLOCK%d:	BOT LEAFLET" % (iblck+1))
  tmpl_b,nframe_b,ist_b,ied_b=read_data(fin_bot)
  print("# BLOCK%d:	PROT DENISTY" % (iblck+1))
  tmpl_c,nframe_c,ist_c,ied_c=read_data(fin_hapos)
  # check nframes
  if (nframe_t != nframe_b):
    print("frame numbers between top and bottom leaflets are different!")
    sys.exit(0)
  
  print("# BLOCK%d: UPDATE HISTOGRAMS" % (iblck+1))
  # loop over frames
  for iframe in range(0,nframe_t):
    # update thickness & histograms
    th_t,sth_t,hist_t,histz=update_thick_hist(iframe,th_t,sth_t,hist_t,histz,ist_t,ied_t,tmpl_t)
    th_b,sth_b,hist_b,histz=update_thick_hist(iframe,th_b,sth_b,hist_b,histz,ist_b,ied_b,tmpl_b)
    # update prot density 
    hist_cav=update_prot_hist_frame(iframe,hist_prot,ist_c,ied_c,tmpl_c)

print("# CALCULATE PROFILES")
#
# update z-positions of each leaflet to get average & standard deviation
#
th_t,sth_t=do_stat(th_t,sth_t,hist_t)
th_b,sth_b=do_stat(th_b,sth_b,hist_b)
# update bilayer thickness (hydrophobic)
for i in range(0,nbin):
  for j in range(0,nbin):
    thist1,thist2=(hist_t[i][j],hist_b[i][j])
    if ( int(thist1) !=0 and int(thist2) != 0): # if both leaflet have thickness data
      th_bi[i][j]=th_t[i][j]-th_b[i][j] # avearge bilayer thickness (hydrophobic)
      hist_bi[i][j]+=1.0                # if hist_bi[i][j]=0, there is no data point in the bin (i,j)


print("# WRITE OUTPUTS")
# write output 
# output files
fout_top  = filename+"_top.prof"      # z-position profile (top)
fout_bot  = filename+"_bot.prof"      # z-position profile (bot)
fout_bi   = filename+"_bilayer.prof"  # hydrophobic thickness profile (bilayer)
fout_prot = filename+"_prot.density"  # protein density profile
fout_zlip = filename+"_zlip.hist"     # z-distribution profile (lipids)

# print output
write_leaflet(fout_top,th_t,sth_t,hist_t)  
write_leaflet(fout_bot,th_b,sth_b,hist_b)  
write_bilayer(fout_bi,th_bi,hist_bi)       
write_prot(fout_prot,hist_prot)            
write_zlip(fout_zlip,histz)                

print("# JOB DONE")
