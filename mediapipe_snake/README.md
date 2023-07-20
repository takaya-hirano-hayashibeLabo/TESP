# Environment Setup 

## Procedure

You can setup by following the steps below.

1. [Setup gym](https://github.com/takaya-hirano-hayashibeLabo/manipulator/blob/main/documents/gym_setting/README_ENG.md)
2. [Setup mujoco](https://github.com/takaya-hirano-hayashibeLabo/manipulator/blob/main/documents/mujoco_setting/README_ENG.md)

# Control snake robot by human pose detection

## Human pose detection
Pose detection by mediapipe

[mediapipe_test.py](mediapipe_test.py)

<img src="img/mediapipe.png" width=720>

```
python mediapipe_test.py
```

## Control snake in simulator
Control snake robot in simulator(gym,mujoco).

**set initial joint angle**

[snake.py](snake.py)

<img src="img/snake-py.png" width=720>


[snake_sim_test.py](snake_sim_test.py)

<img src="img/control_snake_sim.png" width=720>

```
python snake_sim_test.py
```

## Control snake robot by human pose detection (simulation)

[pose_snake_sim.py](pose_snake_sim.py)

<img src="img/pose_snake_sim.png" width=720>

```
python pose_snake_sim.py
```


## Control snake robot by human pose detection (real robot)

[pose_snake_real.py](pose_snake_real.py)

<img src="img/pose_snake_real.png" width=720>

```
python pose_snake_real.py
```
