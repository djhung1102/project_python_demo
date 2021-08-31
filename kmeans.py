import pygame 
from random import randint	#random ra 1 so int so nguyen s
import math
from sklearn.cluster import KMeans

def distance(p1, p2):
	return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("kmeans")

BACKGROUND = (150, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)

RED = (240, 10, 10)
GREEN = (9, 255, 0)
BLUE = (10, 65, 245)
PINK = (245, 10, 206)

COLORS = [RED, GREEN, BLUE, PINK]


font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 20)

text_plus = font.render('+', True, WHITE)
text_plus1 = font.render('-', True, WHITE)
text_plus2 = font.render('RUN', True, WHITE)
text_plus3 = font.render("RANDOM", True, WHITE)
text_plus4 = font.render('Algorithm', True, WHITE)
text_plus5 = font.render('RESET', True, WHITE)

K = 0
Error = 0
points = []
clusters = []
labels = []

clock = pygame.time.Clock()
running = True

while running:
	clock.tick(60)
	screen.fill(BACKGROUND)

	pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
	pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))

	pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
	pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
	pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
	pygame.draw.rect(screen, BLACK, (850, 250, 150,50))
	pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
	pygame.draw.rect(screen, BLACK, (850, 550, 150, 50))


	screen.blit(text_plus, (860, 50))
	screen.blit(text_plus1, (960, 50))
	screen.blit(text_plus2, (900, 150))
	screen.blit(text_plus3, (850, 250))
	screen.blit(text_plus4, (850, 450))
	screen.blit(text_plus5, (860, 550))

	text_k = font.render("K = " + str(K), True, BLACK)
	screen.blit(text_k, (1050, 50))


	mouse_x, mouse_y = pygame.mouse.get_pos()
	
	if 50< mouse_x <750 and 50< mouse_y <550:
		text_mouse = font_small.render('('+ str(mouse_x - 50) + ';'+ str(mouse_y - 50) + ')', True, BLACK)
		screen.blit(text_mouse, (mouse_x + 10, mouse_y))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("ket thuc")
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if 50< mouse_x <750 and 50< mouse_y <550:
				labels = [] 
				point = [mouse_x - 50, mouse_y - 50]
				points.append(point)
				print(points)

		#mouse
			if 850< mouse_x <900 and 50< mouse_y <100 and K<4:
				K = K+1
		
			if 950< mouse_x <1000 and 50< mouse_y <100 and K>0:
				K = K-1
		
		#run
			if 850< mouse_x <1000 and 150< mouse_y <200:
				labels = []

				if clusters == []:
					continue


				#gán điểm vào cluster gần nhất

				for p in points:
					distances_to_cluster = []
					for c in clusters:
						dis = distance(p,c)
						distances_to_cluster.append(dis)

					min_distance = min(distances_to_cluster)  #ham min tinh gia tri nho nhat
					label = distances_to_cluster.index(min_distance)  #ham index tim vi tri nho nhat
					labels.append(label)

			# thay đổi vị trí cluster để vào giữa cụm points
				for i in range(K):
					sum_x = 0
					sum_y = 0
					count = 0	#số điểm points
					for j in range(len(points)):
						if labels[j] == i:
							sum_x += points[j][0]
							sum_y += points[j][1]
							count += 1
					if count != 0:			
						new_clusters_x = sum_x/count
						new_clusters_y = sum_y/count
						clusters[i] = [new_clusters_x, new_clusters_y]


				print("run")
		
		#random
			if 850< mouse_x <1000 and 250< mouse_y <300:
				labels = []
				clusters = []
				for i in range(K):
					random_point = [randint(0,700), randint(0,500)] 
					clusters.append(random_point)
				print("random")
		
		#algorithm
			if 850< mouse_x <1000 and 450< mouse_y <500:
				if points == []:
					continue
				if clusters ==[]:
					continue
				kmeans = KMeans(n_clusters=K).fit(points)
				labels = kmeans.predict(points)
				clusters = kmeans.cluster_centers_

				print("algorithm")
		
		#reset
			if 850< mouse_x <1000 and 550< mouse_y <600:
				K = 0
				labels = []
				points = []
				clusters = []
				print("reset")

		#draw points
	for i in range(len(points)):
		pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6)

		if labels == []:
			pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
		else:
			pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5)

		#draw cluster points
	for i in range(len(clusters)):
		pygame.draw.circle(screen, COLORS[i], (clusters[i][0] + 50, clusters[i][1] +50 ), 10)

	#tính toán và in ra error
	error = 0
	if clusters != [] and labels != []:
		for i in range(len(points)):
			error += distance(points[i], clusters[labels[i]])
	text_error = font.render("Error = " + str(int(error)), True, BLACK)
	screen.blit(text_error, (850, 350))

	pygame.display.flip()

pygame.quit()
pygame.quit()
