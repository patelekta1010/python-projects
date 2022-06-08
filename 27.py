l1 = ["bringle", "aloo", "bread","ice cream"]
i=1
for item in l1:
    if i%2==0:
        print(f"plz buy {item}\n")
    i+=1

for index, item in enumerate(l1):
    if index%2==0:
        print(f"plz ekta buy {item}\n")