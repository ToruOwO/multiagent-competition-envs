# Competitive Multi-Agent Environments

This repository contains the *cleaned and updated* environments from the paper [Emergent Complexity via Multi-agent Competition](https://arxiv.org/abs/1710.03748).

## Dependencies
Use `pip install -r requirements.txt` to install dependencies. If you haven't used MuJoCo before, please refer to the [installation guide](https://github.com/openai/mujoco-py).
The code has been tested with the following dependencies:
* Python version 3.7
* [OpenAI GYM](https://github.com/openai/gym) version 0.20.0 with MuJoCo 2.00 support (use [mujoco-py version 2.0.2](https://github.com/openai/mujoco-py))
* [Tensorflow](https://www.tensorflow.org/versions/r1.1/install/) version 1.15.0
* [Numpy](https://scipy.org/install.html) version 1.20.0

## Installing Package
After installing all dependencies, make sure gym works with support for MuJoCo environments.
Next install `gym-compete` package as:
```bash
cd gym-compete
pip install -e .
```
Check install is successful by coming out of the directory and trying `import gym_compete` in python console. Some users might require a `sudo pip install`.

## Trying the environments
To see a demo of all environments (with untrained agents) do:
```bash
bash demo_tasks.sh all
```
To instead try a single environment use:
```bash
bash demo_tasks.sh <task>
```
where `<task>` is one of: `run-to-goal-humans`, `run-to-goal-ants`, `you-shall-not-pass`, `sumo-ants`, `sumo-humans` and `kick-and-defend`

## Demos

run-to-goal-humans 

![run-to-goal-humans](https://github.com/ToruOwO/multiagent-competition-envs/blob/main/demos/run-to-goal-humans.png)

run-to-goal-ants

![run-to-goal-ants](https://github.com/ToruOwO/multiagent-competition-envs/blob/main/demos/run-to-goal-ants.png)

you-shall-not-pass

![you-shall-not-pass](https://github.com/ToruOwO/multiagent-competition-envs/blob/main/demos/you-shall-not-pass.png)

sumo-ants

![sumo-ants](https://github.com/ToruOwO/multiagent-competition-envs/blob/main/demos/sumo-ants.png)

sumo-humans

![sumo-humans](https://github.com/ToruOwO/multiagent-competition-envs/blob/main/demos/sumo-humans.png)

kick-and-defend

![kick-and-defend](https://github.com/ToruOwO/multiagent-competition-envs/blob/main/demos/kick-and-defend.png)