import math
import numpy as np
import pygame
from typing import List, Any

# функции
def polar_vector(r: float, theta: float) -> List[float]:
    return [math.cosh(r),
            math.sinh(r) * math.cos(theta),
            math.sinh(r) * math.sin(theta)]


def project_on_to_poincare_disc(point: List[float]) -> List[float]:
    scale = min(WIDTH, HEIGHT) / 2 / (point[0] + 1)
    return [point[1] * scale,
            point[2] * scale,
            0]


def vector_mult_matrix(vector: List[float], matrix: List[list]) -> List[float]:
    vector_np = np.array(vector)
    matrix_np = np.array(matrix)
    mult = vector_np.dot(matrix_np)
    result = [mult[0], mult[1], mult[2]]
    return result


def draw_line(current_transform: List[list], angle: float, line_lenght: float):
    prev_point = [0, 0, 0]
    inc = 0.1
    i = 0
    whd = min(WIDTH, HEIGHT) / 2
    while i < line_lenght:
        next_point = polar_vector(i, angle)

        next_point = vector_mult_matrix(next_point, current_transform)
        next_point = project_on_to_poincare_disc(next_point)
        if i >= inc:
            pygame.draw.line(screen,
                             (255, 255, 255),
                             (prev_point[0] + whd, prev_point[1] + whd),
                             (next_point[0] + whd, next_point[1] + whd),
                             3)
        prev_point = next_point
        i += inc


def rotation_matrix(theta: float) -> List[list]:
    s = math.sin(theta)
    c = math.cos(theta)
    return [[1, 0, 0],
            [0, c, s],
            [0, -s, c]]


def translation_matrix_y(y_trans: float) -> List[list]:
    s = math.sinh(y_trans)
    c = math.cosh(y_trans)
    return [[c, 0, s],
            [0, 1, 0],
            [s, 0, c]]


def translation_matrix_z(z_trans: float) -> List[list]:
    s = math.sinh(z_trans)
    c = math.cosh(z_trans)
    return [[c, s, 0],
            [s, c, 0],
            [0, 0, 1]]


def matrix_mult_matrix(matrix_a: List[list], matrix_b: List[list]) -> List[list]:
    matrix_a_np = np.array(matrix_a)
    matrix_b_np = np.array(matrix_b)
    mult = matrix_a_np.dot(matrix_b_np)
    result = [[mult[0][0], mult[0][1], mult[0][2]],
              [mult[1][0], mult[1][1], mult[1][2]],
              [mult[2][0], mult[2][1], mult[2][2]]]
    return result





branch_lenght = 1.255
depth = 4
pi = math.pi


WIDTH = 500
HEIGHT = 500
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hyperbolica")
clock = pygame.time.Clock()

# Цикл игры
running = True
position = [0, 0]
speed = [0, 0]
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed[0] = -0.02
            elif event.key == pygame.K_d:
                speed[0] = 0.02
            elif event.key == pygame.K_s:
                speed[1] = 0.02
            elif event.key == pygame.K_w:
                speed[1] = -0.02
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed[0] = 0
            elif event.key == pygame.K_d:
                speed[0] = 0
            elif event.key == pygame.K_s:
                speed[1] = 0
            elif event.key == pygame.K_w:
                speed[1] = 0
    # Обновление
    position[0] += speed[0]
    position[1] += speed[1]
    # Рендеринг
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2), min(WIDTH, HEIGHT) / 2, 2)

    transform_y = translation_matrix_y(position[1])
    transform_z = translation_matrix_z(position[0])
    transform = matrix_mult_matrix(transform_z, transform_y)
    transform_copy = transform
    for a in range(4):
        transform_copy = matrix_mult_matrix(rotation_matrix(pi * a / 2), transform)
        transform_copy_2 = transform_copy
        for i in range(10):
            draw_line(transform_copy_2, 0, 0.5)
            transform_copy_2 = matrix_mult_matrix(translation_matrix_z(1), transform_copy_2)


    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
