try:
    xname = input("Enter file name: ")
    print(xname)
    fh = open(xname, 'r')
except:
    print("File format Badly")
    quit()

count_avg = 0
all_num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    int_line = line.find(' ')
    line = line[int_line:]
    count_avg += 1
    line = float(line)
    all_num += line
    
print("Average spam confidence:", all_num/count_avg)
