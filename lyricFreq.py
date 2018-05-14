import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from sys import stdin
from collections import Counter
import re
regex = re.compile('[^a-zA-Z]')

NUMLYRICS = 10

#Break up the words in the text file
lyrics = [lyric for song in stdin for lyric in song.split()]

#Get rid of non alphabetic characters and convert to lowercase
for l in range(len(lyrics)):
   lyrics[l] = lyrics[l].lower()
   lyrics[l] = regex.sub('',lyrics[l])

#Check if the number of lyrics are less than the predefined number
if NUMLYRICS > len(Counter(lyrics).most_common()):
   NUMLYRICS = len(Counter(lyrics).most_common())

#Get the lyrics in order of frequency
lyricsKeys = [Counter(lyrics).most_common(NUMLYRICS)[i][0]
              for i in range(NUMLYRICS)]

#Get the frequency in descending order
lyricsValues = [Counter(lyrics).most_common(NUMLYRICS)[i][1]
              for i in range(NUMLYRICS)]

#Create and print the graph
plt.title('Lyric Frequency')
plt.xlabel('Lyrics')
plt.xticks(rotation=90)
plt.ylabel('Frequency')
plt.bar(lyricsKeys,lyricsValues)
plt.savefig('lyricFrequency.png')
