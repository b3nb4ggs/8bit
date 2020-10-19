import math
import pyxel

BALL_SIZE = 2
BALL_SPEED = 2
BAT_SIZE = 8
SCREEN_WIDTH = 255
SCREEN_HEIGHT = 120


class Vec2:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Vec2_norm:
	def __init__(self, x, y):
		self.magnitude = math.sqrt(x * x + y * y)
		self.x = x / self.magnitude * BALL_SPEED
		self.y = y / self.magnitude * BALL_SPEED

class Bat:
	def __init__(self,px,py):
		self.position=Vec2(px,py)
		self.velocity=0

class Ball:
	def __init__(self, px, py, vx, vy):
		self.position = Vec2(px, py)
		self.velocity = Vec2_norm(vx, vy)

	def update(self):
		self.position.x += self.velocity.x
		self.position.y += self.velocity.y
		if self.position.y >= SCREEN_HEIGHT - BALL_SIZE:
			self.velocity.y = -self.velocity.y
		if self.position.y <= BALL_SIZE:
			self.velocity.y = -self.velocity.y
		if self.position.x >= SCREEN_WIDTH - BALL_SIZE:
			self.velocity.x = -self.velocity.x
		if self.position.x <= BALL_SIZE:
			self.velocity.x = -self.velocity.x


class App:
	def __init__(self):
		pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT)
		self.ball = Ball(20, 20, 2, 2)
		self.bats = [Bat(10,10), Bat(SCREEN_WIDTH -10,10)]
		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		self.ball.update()

	def draw(self):
		pyxel.cls(0)
		pyxel.circ(
			self.ball.position.x,
			self.ball.position.y,
			BALL_SIZE,
			7
		)
		#for bat in self.bats:
		#	pyxel.rect(
		#		bat.position.x - BAT_SIZE / 4, #X TOP LEFT
		#		bat.position.y - BAT_SIZE,		#Y TOP LEFT
		#		7,
		#	)
App()