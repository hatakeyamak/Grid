Grid
====
This is where I store all grid related packages.

source ~cmssoft/shrc
cmsrel CMSSW_9_2_5_patch2
cd CMSSW_9_2_5_patch2/src
cmsenv
git clone git@github.com:hatakeyamak/Grid.git
cd Grid/
cd CrabTestPackage/
source cmsDriver_commands.sh 

source /cvmfs/cms.cern.ch/crab3/crab.sh
crab submit crab3Config_WE_7TeV.py
crab submit crab3Config_slurp.py
