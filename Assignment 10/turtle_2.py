import turtle

turtle.bgcolor("black")
galatic = turtle.Turtle()
galatic.speed(20)

colors = ["yellow", "blue", "red", "green", "red"]

galatic.color("white")

a = 5
b = 150
c = 10

for f in range(5):
    for i in range(10):
        size = b
        for j in range(10):
            galatic.circle(size)
            size -= a
        galatic.right(36)

    galatic.color(colors[f])
    a += 5
    b -= 20
    c = 4

turtle.done()