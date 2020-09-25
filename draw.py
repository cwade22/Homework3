import turtle

TEXT_FONT = ('Arial', 18, 'normal')

pen = turtle.Pen()


#blue line
postion = pen.position()
pen.width(5)
pen.color('blue')
#move 1
pen.goto(50, 50)
#move 2
pen.goto(125, -50)
#move3
pen.goto(80, -95)

pen.up()

#reset pen
pen.home()

#red line
pen.down()
pen.color('red')
#move 1
pen.goto(-50, 50)
#move 2
pen.goto(-125, -50)
#move 3
pen.goto(-80, -95)

pen.up()

# To make the graphics stay in a non-ineractive execution
turtle.done()