file = open('xxx.vtt')
lines = file.readlines()

count = 1

# Manually remove any VTT header
with open('new.srt', 'w') as f:
    for line in lines:
        update = False
        # add missing section counter
        if line in ['\n', '\r\n']:
            f.write(line)
            f.write(str(count)+"\n")
            count += 1
            update = True
        # add missing hour stamp (00:25,123 into 00:00:25,123)
        if line.count(':') < 3 and line.count(':') > 1:
            update = True
            # add to start 00:
            line = "00:" + line
            # add after --> another 00:
            line = line.replace("--> ", "--> 00:")
            f.write(line)
        # replace '.' to ',' within timestamp
        if line.count(':') > 1:
            line = line.replace(".", ",")
            f.write(line)
        # other lines with text just propagate
        if update == False:
            f.write(line)

print("finished")
