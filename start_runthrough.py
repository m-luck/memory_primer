# Author: Michael Lukiman
from pygame_render import launch_graphics
import re
import time
import ast
import random
screen_w = 1367
screen_h = 919
row = 8
column = 3
cues_per_page = row*column
cues = []
pages = []
filename = "line_separated_cues.txt"
file = open(filename, "r")
for line in file:
	phrase = line.split("\n")
	phrase = phrase[0]
	cues.append(phrase)
random.shuffle(cues)
filename = "cue_stats.txt"
file = open(filename, "r")
cue_stats = {}
string = file.readline()
cue_stats = ast.literal_eval(string)
i = 0
while i < len(cues):
	page = []
	for layout_index in range(0,cues_per_page):
		page.append("")
		if i < len(cues):
			page[layout_index] = cues[i]
		i += 1
	pages.append(page)
cue_stats_add, block_ended = launch_graphics(row,column,pages,screen_w,screen_h)
for cue in cue_stats_add:
	new_info = [block_ended,cue_stats_add[cue]]
	if cue in cue_stats:
		cue_stats[cue].append(new_info)
	else:
		cue_stats[cue] = [new_info]
# for cue in cue_stats:
# 	print(cue)
# 	for info_set in cue_stats[cue]:
# 		print("\t",info_set[0])
# 		for pause in info_set[1]:
# 			print("\t\t",pause)
file.close()
file = open("cue_stats.txt","w")
file.write(str(cue_stats))
file.close()
