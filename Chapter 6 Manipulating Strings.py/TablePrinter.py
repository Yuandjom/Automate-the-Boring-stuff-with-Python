tableData = [['apple','oranges','cherries','banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs','cats','moose','goose']
]

def printTable(datafromtable):
    colwidth = [0]*len(tableData)
    print(colwidth)
    for listfound in datafromtable:
        for items in listfound :
            print(items)

printTable(tableData)