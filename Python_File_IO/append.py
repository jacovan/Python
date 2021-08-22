message = input("Write a message to be appended to append.txt\n")
with open("append.txt","a") as sample:
    sample.write("\n"+message)
    