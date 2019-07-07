#!/usr/bin/python
# -*- coding: utf-8 -*-

# play.py

import random

def plan_monday():
    print("Monday:")
    plan_functional_fitness()
    get_swim_interval(True)

def plan_tuesday():
    print("Tuesday:")
    get_bike_workout()

def plan_wednesday():
    print("Wednesday:")
    get_run_interval()

def plan_thursday():
    print("Thursday:")
    get_bike_workout()

def plan_friday():
    print("Friday:")
    get_swim_interval(False)

def plan_functional_fitness():
    print("\tFunctional Exercise")
    get_bench_press_variation()
    get_squat_variation()
    get_deadlift_variation()

def get_bench_press_variation():
    workouts = [
        'Bench Press', 
        'Incline Bench Press', 
        'Decline Bench Press'
        ]
    workout = random.choice(workouts)
    print("\t\t" + workout)

def get_squat_variation():
    workouts = [
        'Back Squat', 
        'Front Squat', 
        'Box Squat',
        'Overhead Squat'
        ]
    workout = random.choice(workouts)
    print("\t\t" + workout)

def get_deadlift_variation():
    workouts = [
        'Conventional Deadlift', 
        'Sumo Deadlift', 
        'Deficit Deadlift',
        'Block Deadlift',
        'Romanian Deadlift'
        ]
    workout = random.choice(workouts)
    print("\t\t" + workout)

def get_swim_interval(optional):
    if optional:
        print("\tOptional Swim")
    else:
        print("\tSwim")
    workouts = [
        '10 x 50y', 
        '20 x 25y', 
        '10 x 75y', 
        '4 x 100y', 
        '5 x 200y',
        '3 x 300y'
        ]
    workout = random.choice(workouts)
    print("\t\t" + workout)

def get_run_interval():
    print("\tRun Intervals")
    workouts = [
        '8 x 200m',
        '16 x 200m',
        '24 x 200m',
        '4 x 400m',
        '8 x 400m',
        '12 x 400m',
        '2 x 800m',
        '4 x 800m',
        '6 x 800m',
        '1 x 1 mile',
        '2 x 1 mile',
        '3 x 1 mile'
        ]
    workout = random.choice(workouts)
    print("\t\t" + workout)

def get_bike_workout():
    print("\tBike Intervals On Trainer")

if __name__ == "__main__":
    plan_monday()
    plan_tuesday()
    plan_wednesday()
    plan_thursday()
    plan_friday()
    