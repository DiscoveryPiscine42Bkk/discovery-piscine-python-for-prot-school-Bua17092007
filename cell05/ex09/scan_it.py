import sys 
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    search_steing = sys.argv[2]
    count = search_steing.count(keyword)
    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")