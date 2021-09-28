#!/bin/bash

task=$1
max_episodes=1
correct=0

if [ $task == "run-to-goal-ants" ] || [ $task == "all" ]
then
  echo "Task 1: Run-to-Goal (Ants)"
  python test.py --env run-to-goal-ants --max-episodes $max_episodes
  correct=1
fi
if [ $task == "run-to-goal-humans" ] || [ $task == "all" ]
then
  echo "Task 1: Run-to-Goal (Humans)"
  python test.py --env run-to-goal-humans --max-episodes $max_episodes
  correct=1
fi
if [ $task == "you-shall-not-pass" ] || [ $task == "all" ]
then
  echo "Task 2: You-Shall-Not-Pass"
  python test.py --env you-shall-not-pass --max-episodes $max_episodes
fi
if [ $task == "sumo-ants" ] || [ $task == "all" ]
then
  echo "Task 3: Sumo (Ants)"
  python test.py --env sumo-ants --max-episodes $max_episodes
  correct=1
fi
if [ $task == "sumo-humans" ] || [ $task == "all" ]
then
  echo "Task 3: Sumo (Humans)"
  python test.py --env sumo-humans --max-episodes $max_episodes
  correct=1
fi
if [ $task == "kick-and-defend" ] || [ $task == "all" ]
then
  echo "Task 4: Kick-and-Defend"
  python test.py --env kick-and-defend --max-episodes $max_episodes
  correct=1
fi
if [ $correct == 0 ]
then
  echo "Usage: bash demo_tasks.sh <task>"
  echo "where <task> is all to demo all tasks or one of: run-to-goal-humans, run-to-goal-ants, you-shall-not-pass, sumo-humans, sumo-ants, kick-and-defend"
fi
