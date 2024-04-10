import turtle as tr

tr.color('forest green')
tr.fillcolor("seagreen1")
tr.width(10)
tr.begin_fill()

for i in range(3):
    tr.right(120)
    tr.forward(100)
for i in range(3):
    tr.left(120)
    tr.forward(100)

tr.left(60)
tr.forward(100)

for i in range(2):
    tr.right(120)
    tr.forward(100)
for i in range(2):
    tr.left(120)
    tr.forward(100)

tr.right(60)
tr.forward(100)

for i in range(2):
    tr.right(120)
    tr.forward(100)
tr.end_fill()

tr.fillcolor("seagreen1")
tr.begin_fill()

tr.right(60)
tr.forward(100)

for i in range(2):
    tr.right(120)
    tr.forward(100)

tr.left(0)
tr.forward(300)

for i in range(3):
    tr.right(120)
    tr.forward(100)
for i in range(3):
    tr.left(120)
    tr.forward(100)

tr.end_fill()

tr.done()
