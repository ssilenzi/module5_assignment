#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math

TOL = 1e-12

def plot_square(p1, p2):
    x = [p1[0], p2[0], p2[0], p1[0], p1[0]]
    y = [p1[1], p1[1], p2[1], p2[1], p1[1]]
    plt.plot(x, y, 'k-')

def plot_ray(p1, p2):
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    plt.plot(x, y, 'r-', linewidth=0.5)

def generate_random_pose(lower_point, upper_point, angle_range):
    x = np.random.uniform(lower_point[0], upper_point[0])
    y = np.random.uniform(lower_point[1], upper_point[1])
    theta = np.random.uniform(angle_range[0], angle_range[1])
    return (x, y, theta)

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def distance_from_borders(pose, rect_p1, rect_p2):
    if pose[0] > rect_p1[0] and pose[0] < rect_p2[0] and pose[1] > rect_p1[1] and pose[1] < rect_p2[1]:
        if abs(math.cos(pose[2])) < TOL:
            d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
            if d > 0:
                return d
            else:
                d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                return d
        elif abs(math.sin(pose[2])) < TOL:
            d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
            if d > 0:
                return d
            else:
                d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                return d
        else:
            if math.tan(pose[2]) > 0:
                eq1 = -math.sin(pose[2]) * (pose[0] - rect_p1[0]) + math.cos(pose[2]) * (pose[1] - rect_p1[1])
                eq2 = -math.sin(pose[2]) * (pose[0] - rect_p2[0]) + math.cos(pose[2]) * (pose[1] - rect_p2[1])
                if math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return d
                elif math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 < 0:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                        return d
                elif math.cos(pose[2]) * eq1 < 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return d
                else:
                    d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                        return d
            else:
                eq1 = -math.sin(pose[2]) * (pose[0] - rect_p1[0]) + math.cos(pose[2]) * (pose[1] - rect_p2[1])
                eq2 = -math.sin(pose[2]) * (pose[0] - rect_p2[0]) + math.cos(pose[2]) * (pose[1] - rect_p1[1])
                if math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return d
                elif math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 < 0:
                    d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return d
                elif math.cos(pose[2]) * eq1 < 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                        return d
                else:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return d
                    else:
                        d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                        return d
    else:
        raise Exception("Robot not inside the borders")

def distance_from_borders_full(pose, rect_p1, rect_p2):
    if pose[0] > rect_p1[0] and pose[0] < rect_p2[0] and pose[1] > rect_p1[1] and pose[1] < rect_p2[1]:
        if abs(math.cos(pose[2])) < TOL:
            d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
            if d > 0:
                return (d, (pose[0], rect_p1[1]))
            else:
                d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                return (d, (pose[0], rect_p2[1]))
        elif abs(math.sin(pose[2])) < TOL:
            d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
            if d > 0:
                return (d, (rect_p1[0], pose[1]))
            else:
                d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                return (d, (rect_p2[0], pose[1]))
        else:
            if math.tan(pose[2]) > 0:
                eq1 = -math.sin(pose[2]) * (pose[0] - rect_p1[0]) + math.cos(pose[2]) * (pose[1] - rect_p1[1])
                eq2 = -math.sin(pose[2]) * (pose[0] - rect_p2[0]) + math.cos(pose[2]) * (pose[1] - rect_p2[1])
                if math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return (d, (rect_p1[0], pose[1] + math.tan(pose[2]) * (rect_p1[0] - pose[0])))
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return (d, (pose[0] + (rect_p2[1] - pose[1]) / math.tan(pose[2]), rect_p2[1]))
                elif math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 < 0:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return (d, (rect_p1[0], pose[1] + math.tan(pose[2]) * (rect_p1[0] - pose[0])))
                    else:
                        d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                        return (d, (rect_p2[0], pose[1] + math.tan(pose[2]) * (rect_p2[0] - pose[0])))
                elif math.cos(pose[2]) * eq1 < 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                    if d > 0:
                        return (d, (pose[0] + (rect_p1[1] - pose[1]) / math.tan(pose[2]), rect_p1[1]))
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return (d, (pose[0] + (rect_p2[1] - pose[1]) / math.tan(pose[2]), rect_p2[1]))
                else:
                    d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return (d, (rect_p2[0], pose[1] + math.tan(pose[2]) * (rect_p2[0] - pose[0])))
                    else:
                        d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                        return (d, (pose[0] + (rect_p1[1] - pose[1]) / math.tan(pose[2]), rect_p1[1]))
            else:
                eq1 = -math.sin(pose[2]) * (pose[0] - rect_p1[0]) + math.cos(pose[2]) * (pose[1] - rect_p2[1])
                eq2 = -math.sin(pose[2]) * (pose[0] - rect_p2[0]) + math.cos(pose[2]) * (pose[1] - rect_p1[1])
                if math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return (d, (rect_p2[0], pose[1] + math.tan(pose[2]) * (rect_p2[0] - pose[0])))
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return (d, (pose[0] + (rect_p2[1] - pose[1]) / math.tan(pose[2]), rect_p2[1]))
                elif math.cos(pose[2]) * eq1 >= 0 and math.cos(pose[2]) * eq2 < 0:
                    d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                    if d > 0:
                        return (d, (pose[0] + (rect_p1[1] - pose[1]) / math.tan(pose[2]), rect_p1[1]))
                    else:
                        d = (rect_p2[1] - pose[1]) / math.sin(pose[2])
                        return (d, (pose[0] + (rect_p2[1] - pose[1]) / math.tan(pose[2]), rect_p2[1]))
                elif math.cos(pose[2]) * eq1 < 0 and math.cos(pose[2]) * eq2 >= 0:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return (d, (rect_p1[0], pose[1] + math.tan(pose[2]) * (rect_p1[0] - pose[0])))
                    else:
                        d = (rect_p2[0] - pose[0]) / math.cos(pose[2])
                        return (d, (rect_p2[0], pose[1] + math.tan(pose[2]) * (rect_p2[0] - pose[0])))
                else:
                    d = (rect_p1[0] - pose[0]) / math.cos(pose[2])
                    if d > 0:
                        return (d, (rect_p1[0], pose[1] + math.tan(pose[2]) * (rect_p1[0] - pose[0])))
                    else:
                        d = (rect_p1[1] - pose[1]) / math.sin(pose[2])
                        return (d, (pose[0] + (rect_p1[1] - pose[1]) / math.tan(pose[2]), rect_p1[1]))
    else:
        raise Exception("Robot not inside the borders")

if  __name__ == '__main__':
    pose = generate_random_pose((0,0), (1,1), (0, 2*math.pi))
    distance, intersection = distance_from_borders_full(pose, (0,0), (1,1))
    print(f"x: {pose[0]}, y: {pose[1]}, theta: {pose[2]}")
    print(f"x_inters: {intersection[0]}, y_inters: {intersection[1]}, distance: {distance}")
    print(f"error: {abs(distance - dist((pose[0], pose[1]), intersection)) + abs(distance - distance_from_borders(pose, (0,0), (1,1)))}")
    
    plot_square((0,0), (1,1))
    plot_ray(pose, intersection)
    plt.arrow(pose[0], pose[1], 0.1*math.cos(pose[2]), 0.1*math.sin(pose[2]), color='b', head_width=0.025, head_length=0.05)
    plt.plot(pose[0], pose[1], marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")
    plt.plot(intersection[0], intersection[1], marker="o", markersize=5, markeredgecolor="green", markerfacecolor="green")
    plt.gca().set_aspect('equal')
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(which='both')
    plt.show()
