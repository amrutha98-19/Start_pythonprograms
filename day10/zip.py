# zip() -> Combines two or more iterables and loops through them together.
names=['arun','anu','ammu','deepu']
marks=[85,90,70,60]

# Loop through both lists at the same time
for i,j in zip(names,marks):
    print(i,j)