import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
from sys import stdin
from collections import Counter

NUMLYRICS = 10

#Break up the words in the text file
lyrics = [lyric for song in stdin for lyric in song.split()]

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
