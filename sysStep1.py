import os
filename=raw_input('please in put a raw file:')
COMMAND_LINE="/data/jiayuheng/score/SProV/spro-5.0/sfbcep -m -k 0.97 -p19 -n 24 -r 22 -e -D -A -F PCM16  "+ filename +".raw ./data/filename"+ ".tmp.prm"
print COMMAND_LINE
print "convert file to MFCC"
os.system(COMMAND_LINE)

print("\n\n\n\n\n\n\n\n")
CMD_NORM_E="/data/jiayuheng/score/ALIZE_file/LIA_RAL/bin/NormFeat --config NormFeat_energy_SPro.cfg --inputFeatureFilename filename --featureFilesPath  data/"
print CMD_NORM_E
print "Normalise energy:"
os.system(CMD_NORM_E)


print("\n\n\n\n\n\n\n\n")
CMD_ENERGY="/data/jiayuheng/score/ALIZE_file/LIA_RAL/bin/EnergyDetector  --config EnergyDetector_SPro.cfg --inputFeatureFilename filename --featureFilesPath  data/  --labelFilesPath  data/"
print CMD_ENERGY
print "Energy Detctor:"
os.system(CMD_ENERGY)


print("\n\n\n\n\n\n\n\n")
print "Normalise Features  Normalise Features Normalise Features Normalise Features Normalise Features Normalise Features Normalise Features Normalise Features"
CMD_NORM="/data/jiayuheng/score/ALIZE_file/LIA_RAL/bin/NormFeat --config NormFeat_SPro.cfg --inputFeatureFilename filename --featureFilesPath data/   --labelFilesPath  data/"
print CMD_NORM
print "Normalise Features:"
os.system(CMD_NORM)




print("\n\n\n\n\n\n\n\n:get score")
CMD="/data/jiayuheng/score/ALIZE_file_multithread/LIA_RAL/bin/ComputeTest --config ComputeTest.cfg  &> data/ComputeTest_noWarning_native.log"
print CMD
os.system(CMD)


print("\n\n\n\n\n\n\n\n:is he a native speaker?")

