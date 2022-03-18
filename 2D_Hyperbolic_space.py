# Python 3.7.5
import math
import numpy as np
import pygame
from typing import List


def polar_vector(r: float, theta: float) -> List[float]:
    return [math.cosh(r),
            math.sinh(r) * math.cos(theta),
            math.sinh(r) * math.sin(theta)]


def project_on_to_poincare_disc(point: List[float]) -> List[float]:
    scale = min(WIDTH - 1, HEIGHT - 1) / 2 / (point[0] + 1)
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
    inc = line_lenght / 10.0 - 0.0001
    if inc < 0.0999:
        inc = 0.0999
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


pi = math.pi


def draw_4_5_tiling(current_transform: List[list], depth: int):
    branch_length = 1.255

    def draw_3branch_sector(current_transform: List[list], current_depth: int):
        draw_line(current_transform, 0, branch_length)
        transform_copy = current_transform
        transform_copy = matrix_mult_matrix(translation_matrix_z(branch_length), transform_copy)
        transform_copy = matrix_mult_matrix(rotation_matrix(pi), transform_copy)
        if current_depth < depth:
            transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / 5), transform_copy)
            draw_2branch_sector(transform_copy, current_depth + 1)
            transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / 5), transform_copy)
            draw_3branch_sector(transform_copy, current_depth + 1)
            transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / 5), transform_copy)
            draw_3branch_sector(transform_copy, current_depth + 1)

    def draw_2branch_sector(current_transform: List[list], current_depth: int):
        draw_line(current_transform, 0, branch_length)
        transform_copy = current_transform
        transform_copy = matrix_mult_matrix(translation_matrix_z(branch_length), transform_copy)
        transform_copy = matrix_mult_matrix(rotation_matrix(pi), transform_copy)
        if current_depth < depth:
            transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / 5), transform_copy)
            draw_line(transform_copy, 0, branch_length)
            transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / 5), transform_copy)
            draw_2branch_sector(transform_copy, current_depth + 1)
            transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / 5), transform_copy)
            draw_3branch_sector(transform_copy, current_depth + 1)

    transform_copy = current_transform
    for i in range(5):
        transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / 5), transform_copy)
        draw_3branch_sector(transform_copy, 0)


def draw_inf_n_tiling(current_transform: List[list], n: int, depth: int):
    lenghts = [1, 1, 1.2, 1.8, 2.3, 2.7, 3, 3.3, 3.5]
    branch_length = lenghts[n - 1]

    def draw_2branch_sector(current_transform: List[list], current_depth: int):
        draw_line(current_transform, 0, branch_length)
        transform_copy = current_transform
        transform_copy = matrix_mult_matrix(translation_matrix_z(branch_length), transform_copy)
        transform_copy = matrix_mult_matrix(rotation_matrix(pi), transform_copy)
        if current_depth < depth:
            for i in range(n - 1):
                transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / n), transform_copy)
                draw_2branch_sector(transform_copy, current_depth + 1)

    transform_copy = current_transform
    for i in range(n):
        transform_copy = matrix_mult_matrix(rotation_matrix(2 * pi / n), transform_copy)
        draw_2branch_sector(transform_copy, 0)


def draw_collatz(current_transform: List[list], current_depth: int, number: int):
    draw_line(current_transform, 0, 0.34)
    transform_copy = current_transform
    transform_copy = matrix_mult_matrix(translation_matrix_z(0.34), transform_copy)
    transform_copy = matrix_mult_matrix(rotation_matrix(pi), transform_copy)
    transform_copy_2 = transform_copy
    num3 = (number - 1) / 3.0
    angle = pi
    if current_depth < 22:
        if (num3 % 2 == 1.0) & (num3 != 1):
            angle = pi - 0.5
            transform_copy_2 = matrix_mult_matrix(rotation_matrix(-angle), transform_copy_2)
            draw_collatz(transform_copy_2, current_depth + 1, int(num3))
        transform_copy = matrix_mult_matrix(rotation_matrix(angle), transform_copy)
        draw_collatz(transform_copy, current_depth + 1, number * 2)


def transform_matrix(current_transform: List[list], theta: float, choice: int) -> List[list]:
    if choice == 0:
        current_transform = matrix_mult_matrix(current_transform, translation_matrix_z(theta))
    elif choice == 1:
        current_transform = matrix_mult_matrix(current_transform, translation_matrix_y(theta))
    elif choice == 2:
        current_transform = matrix_mult_matrix(current_transform, rotation_matrix(theta))
    return current_transform


WIDTH = 500
HEIGHT = 500
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hyperbolica")
clock = pygame.time.Clock()

running = True
speed = [0, 0, 0]
transform = rotation_matrix(0)
press = 0
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed[0] = -1
            elif event.key == pygame.K_d:
                speed[0] = 1
            elif event.key == pygame.K_s:
                speed[1] = -1
            elif event.key == pygame.K_w:
                speed[1] = 1
            elif event.key == pygame.K_q:
                speed[2] = -1
            elif event.key == pygame.K_e:
                speed[2] = 1
            elif event.key == pygame.K_SPACE:
                press += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed[0] = 0
            elif event.key == pygame.K_d:
                speed[0] = 0
            elif event.key == pygame.K_s:
                speed[1] = 0
            elif event.key == pygame.K_w:
                speed[1] = 0
            elif event.key == pygame.K_q:
                speed[2] = 0
            elif event.key == pygame.K_e:
                speed[2] = 0

    speed_value = 0.06
    if speed[0] != 0:
        transform = transform_matrix(transform, -speed[0] * speed_value, 0)
    if speed[1] != 0:
        transform = transform_matrix(transform, speed[1] * speed_value, 1)
    if speed[2] != 0:
        transform = transform_matrix(transform, -speed[2] * speed_value * 2, 2)

    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2), min(WIDTH, HEIGHT) / 2, 1)
    transform_copy = transform
    # hrustyashiy
    choice = press % 7
    if choice == 0:
        for a in range(50):
            transform_copy = matrix_mult_matrix(rotation_matrix(pi * a / 25), transform)
            transform_copy_2 = transform_copy
            for i in range(5):
                draw_line(transform_copy_2, 0, 0.5)
                transform_copy_2 = matrix_mult_matrix(translation_matrix_z(1), transform_copy_2)
    elif choice == 1:
        draw_4_5_tiling(transform_copy, 3)
    elif choice == 2:
        draw_inf_n_tiling(transform_copy, 3, 6)
    elif choice == 3:
        draw_inf_n_tiling(transform_copy, 4, 3)
    elif choice == 4:
        draw_inf_n_tiling(transform_copy, 5, 2)
    elif choice == 5:
        draw_inf_n_tiling(transform_copy, 6, 2)
    elif choice == 6:
        draw_collatz(transform_copy, 0, 1)

    pygame.display.flip()

pygame.quit()
