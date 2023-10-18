"""
Example 1:
    # name_file = 'mbox-short.txt'
    #
    # try:
    #     open_file = open(name_file)
    # except:
    #     print('File is not exists')
    #     quit()
    # counts = dict()
    #
    # for line in open_file:
    #     words = line.split()
    #     for word in words:
    #         counts[word] = counts.get(word, 0) + 1
    # big_count = None
    # big_word = None
    # for word, count in counts.items():
    #     if big_count is None or count > big_count:
    #         big_word = word
    #         big_count = count
    # print(counts.get('From'))
    # print(big_count, big_word)
Example 2:
    # names = {
    #     "fname": "Mohamed",
    #     'lname':"khaled"
    # }
    #
    # # add in dic key = 0 and value = first name
    # names['long word'] = "first name"
    # print(names.values())
    # print(names.keys())
Example 3:
    This program count how much word repeat in the file
    # file_name = input('Enter File: ')
    # if len(file_name) < 1: file_name = 'mbox-short.txt'
    # try:
    #     open_file = open(file_name)
    # except:
    #     print('File is not exists')
    #     quit()
    # dic = dict()
    #
    # for line in open_file:
    #     # remove ant right white spaces
    #     line = line.rstrip()
    #     words = line.split()
    #     for word in words:
    #         if word in dic:
    #             dic[word] = dic[word] + 1
    #         else:
    #             dic[word] = 1
    #             print("New word")
    #         print(word, dic[word])


"""
name = input("Enter file: ")
dic = dict()
if len(name) > 1:
    name = "mbox-short.txt"
    try:
        handle = open(name)
    except:
        print("File is not exists")
        quit()
    for line in handle:
        if line.startswith('From '):
            int_line = line.find(" ")
            line = line[int_line:].strip()
            int_line = line.find(" ")
            line = line[:int_line].strip()
            line = line.split()
            for email in line:
                if email in dic:
                    dic[email] = dic[email] + 1
                else:
                    dic[email] = 1
    prolific_committer = -1
    prolific_committer_email = ''
    for k,v in dic.items():
        if v > prolific_committer:
            prolific_committer = v
            prolific_committer_email = k
    print(prolific_committer_email, prolific_committer)