import re
series="[EgyBest].Chernobyl.S01E01.WEB-DL.240p.x264.mp4"
season=re.compile("(?=.*)(S\d\d|s\d\d)(?=.*)")
episode=re.compile("(?=.*)(E\d\d|e\d\d)(?=.*)")
se=season.findall(series)
ep=episode.findall(series)
print(se[0])
print(ep[0])
