import turtle
import random

window = turtle.Screen()
window.bgcolor("black")
window.title("Bouncing ball Simulation")
window.tracer(0)

balls = []
for _ in range(15):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "green", "white", "yellow", "purple"]

for ball in balls:
    ball.shape("circle")
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    ball.goto(x, y)
    ball.dy = random.randint(-4, 5)
    ball.dx = random.randint(-4, 5)

while True:
    for ball in balls:
        window.update()
        # lets make the floor
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy = ball.dy * -1
        if ball.ycor() > 250:
            ball.sety(250)
            ball.dy = ball.dy * -1

        # lets make the wall detection
        if ball.xcor() > 300:
            ball.setx(300)
            ball.dx = ball.dx * -1
        if ball.xcor() < -300:
            ball.setx(-300)
            ball.dx *= -1

        # check for the collision between the balls
        for i in range(0, len(balls)):
            for j in range(i + 1, len(balls)):
                # check for the collision
                if balls[i].distance(balls[j]) < 20:
                    m1 = 1  # mass of ball 1
                    m2 = 1  # mass of ball 2
                    v1 = balls[i].dx, balls[i].dy  # velocity of ball 1
                    v2 = balls[j].dx, balls[j].dy  # velocity of ball 2
                    x1 = balls[i].xcor(), balls[i].ycor()  # position of ball 1
                    x2 = balls[j].xcor(), balls[j].ycor()  # position of ball 2

                    # calculate the normal vector and tangential vector
                    n = (x2[0] - x1[0], x2[1] - x1[1])
                    n_mag = (n[0]**2 + n[1]**2)**0.5
                    n = (n[0] / n_mag, n[1] / n_mag)
                    t = (-n[1], n[0])

                    # calculate the scalar projection of v1 and v2 onto the normal vector
                    v1n = n[0] * v1[0] + n[1] * v1[1]
                    v2n = n[0] * v2[0] + n[1] * v2[1]

                    # calculate the scalar projection of v1 and v2 onto the tangential vector
                    v1t = t[0] * v1[0] + t[1] * v1[1]
                    v2t = t[0] * v2[0] + t[1] * v2[1]

                    # calculate the new velocities after collision in the normal direction
                    v1n_new = ((m1 - m2) * v1n + 2 * m2 * v2n) / (m1 + m2)
                    v2n_new = ((m2 - m1) * v2n + 2 * m1 * v1n) / (m1 + m2)

                    # calculate the new velocities after collision in the tangential direction
                    v1t_new = v1t
                    v2t_new = v2t

                    # calculate the new velocities in x and y direction
                    v1n_new_x = v1n_new * n[0]
                    v1n_new_y = v1n_new * n[1]
                    v2n_new_x = v2n_new * n[0]
                    v2n_new_y = v2n_new * n[1]
                    v1t_new_x = v1t_new * t[0]
                    v1t_new_y = v1t_new * t[1]
                    v2t_new_x = v2t_new * t[0]
                    v2t_new_y = v2t_new * t[1]

                    # update the velocities of the balls
                    balls[i].dx = v1n_new_x + v1t_new_x
                    balls[i].dy = v1n_new_y + v1t_new_y
                    balls[j].dx = v2n_new_x + v2t_new_x
                    balls[j].dy = v2n_new_y + v2t_new_y

        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

turtle.mainloop()
