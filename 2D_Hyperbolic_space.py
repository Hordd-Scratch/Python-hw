# Python 3.7.5
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
    inc = 0.2
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


branch_length = 1.255
depth = 5
pi = math.pi
rot_pi = rotation_matrix(pi)
rot_2_pi_div_5 = rotation_matrix(2 * pi / 5)
translate = translation_matrix_z(branch_length)

def draw_4_5_tiling(current_transform: List[list]):
    transform_copy = current_transform
    for i in range(5):
        transform_copy = matrix_mult_matrix(rot_2_pi_div_5, transform_copy)
        draw_3branch_sector(transform_copy, 0)


def draw_3branch_sector(current_transform: List[list], current_depth: int):
    draw_line(current_transform, 0, branch_length)
    transform_copy = current_transform
    transform_copy = matrix_mult_matrix(translate, transform_copy)
    transform_copy = matrix_mult_matrix(rot_pi, transform_copy)
    if current_depth < depth:
        transform_copy = matrix_mult_matrix(rot_2_pi_div_5, transform_copy)
        draw_2branch_sector(transform_copy, current_depth + 1)
        transform_copy = matrix_mult_matrix(rot_2_pi_div_5, transform_copy)
        draw_3branch_sector(transform_copy, current_depth + 1)
        transform_copy = matrix_mult_matrix(rot_2_pi_div_5, transform_copy)
        draw_3branch_sector(transform_copy, current_depth + 1)


def draw_2branch_sector(current_transform: List[list], current_depth: int):
    draw_line(current_transform, 0, branch_length)
    transform_copy = current_transform
    transform_copy = matrix_mult_matrix(translate, transform_copy)
    transform_copy = matrix_mult_matrix(rot_pi, transform_copy)
    if current_depth < depth:
        transform_copy = matrix_mult_matrix(rot_2_pi_div_5, transform_copy)
        draw_line(transform_copy, 0, branch_length)
        transform_copy = matrix_mult_matrix(rot_2_pi_div_5, transform_copy)
        draw_2branch_sector(transform_copy, current_depth + 1)
        transform_copy = matrix_mult_matrix(rot_2_pi_div_5, transform_copy)
        draw_3branch_sector(transform_copy, current_depth + 1)


# void drawCollatz(Matrix4x4 currentTransform, int depth, long number, Color Clr)
#         {
#             byte[] coord = StrConvert(number);
#             float branchLength = 0.34f;
#             HyperbolicLine(coord, currentTransform, 0, branchLength, branchLength-0.0001f, Clr);
#             Matrix4x4 transformCopy = currentTransform;
#
#             transformCopy = PolarTransform.TranslationMatrixY(branchLength) * transformCopy;
#             transformCopy = PolarTransform.RotationMatrix(pi) * transformCopy;
#
#             Matrix4x4 transformCopy2 = transformCopy;
#             float Num3 = (number - 1) / 3f;
#             float angle = pi;
#             if (depth < 35)
#             {
#                 if (Num3 % 2 == 1 && Num3 != 1)
#                 {
#                     angle = pi-0.5f;
#                     transformCopy2 = PolarTransform.RotationMatrix(-angle) * transformCopy2;
#                     drawCollatz(transformCopy2, depth + 1, (int)Num3, Clr);
#                 }
#                 transformCopy = PolarTransform.RotationMatrix(angle) * transformCopy;
#                 drawCollatz(transformCopy, depth + 1, number * 2, Clr);
#             }
#         }


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
speed = [0, 0, 0]
transform = rotation_matrix(0)
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
    # Обновление
    speed_value = 0.04
    if speed[0] != 0:
        transform = transform_matrix(transform, -speed[0] * speed_value, 0)
    if speed[1] != 0:
        transform = transform_matrix(transform, speed[1] * speed_value, 1)
    if speed[2] != 0:
        transform = transform_matrix(transform, -speed[2] * speed_value * 2, 2)
    # Рендеринг
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (WIDTH / 2, HEIGHT / 2), min(WIDTH, HEIGHT) / 2, 2)

    transform_copy = transform

    # for a in range(200):
    #     transform_copy = matrix_mult_matrix(rotation_matrix(pi * a / 100), transform)
    #     transform_copy_2 = transform_copy
    #     for i in range(5):
    #         draw_line(transform_copy_2, 0, 0.3)
    #         transform_copy_2 = matrix_mult_matrix(translation_matrix_z(1), transform_copy_2)

    draw_4_5_tiling(transform_copy)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
