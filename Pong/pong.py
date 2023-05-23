# Jogo Pong simples em python

import turtle

janela = turtle.Screen()
janela.title('Pong')
janela.bgcolor('black')
janela.setup(width=800, height=600)
janela.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
# t minúsculo = modulo, T maúsculo = classe
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball (bola)
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Jogador 1: 0  Jogador 2: 0', align='center', font=('Courier', 18, 'normal'))


# Funções
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
janela.listen()  # fala para ler a entrada do teclado
janela.onkeypress(paddle_a_up, 'w')
janela.onkeypress(paddle_a_down, 's')
janela.onkeypress(paddle_b_up, 'Up')  # subir na seta
janela.onkeypress(paddle_b_down, 'Down')  # descer na seta
# Main game loop
while True:
    janela.update()

    # Mover a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Borda
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverter a direção

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Jogador 1: {}  Jogador 2: {}'.format(score_a, score_b), align='center', font=('Courier', 18, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Jogador 1: {}  Jogador 2: {}'.format(score_a, score_b), align='center', font=('Courier', 18, 'normal'))

    # Colisôes entre os paddles e a bola
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Limite dos paddles
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
