#Jake Shankman
#12/3/2012
#Senior Research Automatic Music Transcription
#Alternate Input File
#Utilize this on Windows Platform until Syslab fixes linking issues

import scipy
from scipy.io.wavfile import read
#from scipy.signal import hann
from scipy.fftpack import rfft
from scipy.fftpack import rfftfreq

#Method for picking out closest note
def closestNote(key, frequency):
  distance = abs(float(key.keys()[0]) - frequency)
  closest = key.keys()[0]
  i = 1
  while i < len(key.keys()):
    pitch = key.keys()[i]
    newDistance = abs(float(pitch) - frequency)
    if newDistance < distance:
      distance = newDistance
      closest = pitch
    i +=1
  return closest
  
#Read data from .wav file
input_data = read("click.wav")
print input_data
#Data to transform: REMOVE METADATA
audio = input_data[1]
print audio

#Filter with Hanning Window
#window = hann(len(audio) - 1)
#audioSample = audio[0:len(audio) - 1] * window

#Run Real FFT
#When hann works, switch audio w/ audioSample
spectrum = abs(rfft(audio))
print spectrum
#Get Frequency piece from FFT
frequency = rfftfreq(len(spectrum))
print frequency

#Set up Key
key = {}
notes = open('frequency.txt', 'r').read().split()
i = 0
while i < len(notes):
  key[notes[i + 1]] = notes[i]
  i += 2
#make outfile
outFile = open('data.txt', 'w')
#Put all Notes in Outfile  
for item in spectrum:
  closest= closestNote(key, abs(item)/1000)
  print "Closest note: ", key[closest], "\tGiven frequency: ", abs(item)/1000
  outFile.write(key[closest])
  outFile.write('\n')

outFile.close()
  