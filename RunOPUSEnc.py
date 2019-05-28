# Run OPUS Encoder
# Variables
#   Order
#   Audio type
#   Bitrate per channel
import subprocess

orders = [1,3,5] # Different ambisonic orders
sourceTypes = ["music","soundscape","speech"]
channels = orders # Makes array of number of channels same length array as orders
bitratesPerCh = [16, 32, 64]
# totalBitrate = ##### COMPLETE AFTER OR PUT INSIDE LOOP

for index, x in enumerate(orders):  # Creates a loop that indexes the values
                                    # into the numCh array.
    channels[index] = (x+1)**2
print(channels)

cmdList = []
baseDir = '.\'

for orderNum in range(0,len(orders)):
    order = orders[orderNum]
    numCh = channels[orderNum]
    for sourceType in sourceTypes:
        for bitratePerCh in bitratesPerCh:
            totalBitrate = numCh*bitratePerCh
            for x in range(1, 19):
                inputPath = baseDir + str(order) + 'oa_audio\\' + str(sourceType) + '\wave\original\\' + str(order) + 'oa_audio\\' + str(sourceType) + '_' + str(x) + '.wav'
                outputPath = baseDir + str(order) + 'oa_audio\\' + str(sourceType) + '\OPUS\\' + str(order) + 'oa_audio\\' + str(sourceType) + '_' + str(x) + '_OPUS_' + str(bitratePerCh) + '_.opus'
                cmd = 'opusenc --bitrate ' + str(totalBitrate) + ' ' + inputPath + ' ' + outputPath
                
                subprocess.call(cmd, shell=True)
    
    

    
