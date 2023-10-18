# try:
#     xname = input("Enter file name: ")
#     print(xname)
#     fh = open(xname, 'r')
# except:
#     print("File format Badly")
#     quit()

# count_avg = 0
# all_num = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     int_line = line.find(' ')
#     line = line[int_line:]
#     count_avg += 1
#     line = float(line)
#     all_num += line
    
# print("Average spam confidence:", all_num/count_avg)

unike = []
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print("File is not exists")
    quit()
count = 0
for i in fh:  
    if i.startswith("From "):
        __lists = i.strip().split()
        for u in range(len(__lists)):
            if __lists[u] == "From":
                print(__lists[u+1])
                count += 1

print("There were", count, "lines in the file with From as the first word")
