class Level:
    def __init__(self, file, coords, width):
        self.filename = file
        self.coords = coords
        self.width = width


l1 = Level("find1.jpg", "20,270,75,450", "800px")
l2 = Level("find2.jpg", "381,316,459,499", "700px")

l3 = Level("find3.jpg", "221,254,252,300", "700px")
l4 = Level("find4.jpg", "734,239,774,297", "800px")
l5 = Level("find5.jpg", "509,313,537,360", "700px")
l6 = Level("find6.jpg", "705,90,757,159", "800px")

l7 = Level("find7.jpg", "121,280,168,350", "800px")
l8 = Level("find8.jpg", "476,185,500,220", "700px")
l9 = Level("find9.jpg", "485,265,511,304", "700px")
l10 = Level("find10.jpg", "240,173,271,234", "800px")

l11 = Level("find11.jpg", "563,278,579,325", "700px")
l12 = Level("find12.jpg", "202,328,225,382", "700px")
l13 = Level("find13.jpg", "435,128,474,189", "700px")
l14 = Level("find14.jpg", "676,102,706,149", "800px")
l15 = Level("find15.jpg", "651,165,676,203", "700px")

l16 = Level("find16.jpg", "40,336,65,370", "700px")
l17 = Level("find17.jpg", "540,310,576,353", "700px")
l18 = Level("find18.jpg", "501,116,530,157", "700px")

l19 = Level("find19.jpg", "650,304,679,345", "800px")
l20 = Level("find20.jpg", "482,190,513,249", "750px")
l21 = Level("find21.jpg", "39,143,69,182", "800px")


Levels = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]
Levels.extend([l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21])
