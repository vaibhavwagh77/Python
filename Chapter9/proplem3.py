def genrateTable(n):
    table=""
    for i in range(1, 11):
        table+=f"{n} X {i} = {n*i}\n"
    with open(f"Tables/Table_{n}","w") as f:
        f.write(table)


for i in range(2,21):
    genrateTable(i)
        