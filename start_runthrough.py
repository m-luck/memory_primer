from pygame_render import launch_graphics

filename = "line_separated_cues.txt"
file = open(filename, "r")

cues_per_page = 6

cues = []
pages = []
page_stats = {}
cue_stats = {}
for line in file:
	phrase = line.split("\n")
	phrase = phrase
i = 0
print(len(cues))
while i < len(cues):
	page = []
	for layout_index in range(0,cues_per_page):
		page.append("")
		if i < len(cues):
			page[layout_index] = cues[i]
		i += 1
	pages.append(page)

for page in range(0, len(pages)):
	print("\nPage ",page+1,":")
	for cue in range(0,cues_per_page):
		if (cue+1)*(page+1) < len(cues):
			print(pages[page][cue])

launch_graphics
