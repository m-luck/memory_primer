from pygame_render import launch_graphics

filename = "line_separated_cues.txt"
file = open(filename, "r")

screen_w = 1000
screen_h = 500
row = 2
column = 3
cues_per_page = row*column

cues = []
pages = []
page_stats = {}
cue_stats = {}
for line in file:
	phrase = line.split("\n")
	phrase = phrase[0]
	cues.append(phrase)
print(cues)
i = 0
while i < len(cues):
	page = []
	for layout_index in range(0,cues_per_page):
		page.append("")
		if i < len(cues):
			page[layout_index] = cues[i]
		i += 1
	pages.append(page)
# for page in range(0, len(pages)):
# 	print("\nPage ",page+1,":")
# 	for cue in range(0,cues_per_page):
# 		if (cue+1)*(page+1) < len(cues):
# 			print(pages[page][cue])
launch_graphics(row,column,pages,screen_w,screen_h)
