#/bin/sh

cmsDriver.py WE_7TeV.cfi -s GEN,SIM,DIGI,L1,DIGI2RAW,RAW2DIGI,RECO -n 10 --geometry DB --conditions auto:startup \
  --relval 9000,100 --datatier 'GEN-SIM-DIGI-RAW-RECO' --eventcontent FEVTSIM --no_exec


