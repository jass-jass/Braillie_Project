import louis

tableList = ["unicode.dis","braille-patterns.cti","en-ueb-g1.ctb"]
line=["abcd"]
for i in line:
	translation = louis.translateString(tableList,i)
	print(i + "=" + translation + "\n")

