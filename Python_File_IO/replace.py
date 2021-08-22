message = input("Enter text to overwrite sample2.txt\n")
with open ("replace.txt","w") as sample:
    sample.write(message)