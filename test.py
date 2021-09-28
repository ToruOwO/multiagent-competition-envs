import gym
import gym_compete
import sys
import argparse
import numpy as np

import moviepy.editor as mpy
from PIL import Image


def export_video(frames, video_path, fps=30):
    frames = np.stack(frames)
    def make_frame(i):
        out = frames[i]
        return out
    clip = mpy.VideoClip(
    	lambda t: make_frame(min(int(t * fps), len(frames) - 1)),
    	duration=len(frames) / fps)
    clip.write_videofile(video_path, fps=fps)


def run(config):
    if config.env == "kick-and-defend":
        env = gym.make("kick-and-defend-v0")
        policy_type = "lstm"
    elif config.env == "run-to-goal-humans":
        env = gym.make("run-to-goal-humans-v0")
        policy_type = "mlp"
    elif config.env == "run-to-goal-ants":
        env = gym.make("run-to-goal-ants-v0")
        policy_type = "mlp"
    elif config.env == "you-shall-not-pass":
        env = gym.make("you-shall-not-pass-humans-v0")
        policy_type = "mlp"
    elif config.env == "sumo-humans":
        env = gym.make("sumo-humans-v0")
        policy_type = "lstm"
    elif config.env == "sumo-ants":
        env = gym.make("sumo-ants-v0")
        policy_type = "lstm"
    else:
        print("unsupported environment")
        print(
            "choose from: run-to-goal-humans, run-to-goal-ants,"
            "you-shall-not-pass, sumo-humans, sumo-ants, kick-and-defend")
        sys.exit()

    max_episodes = config.max_episodes
    num_episodes = 0
    nstep = 0
    total_reward = [0.0 for _ in range(env.n_agents)]
    total_scores = [0 for _ in range(env.n_agents)]
    observation = env.reset()
    print("-" * 5 + " Episode %d " % (num_episodes + 1) + "-" * 5)
    frames = []
    while num_episodes < max_episodes:
        # env.render()
        img = env.render(mode="rgb_array")
        img = Image.fromarray(img)

        frames.append(img)

        action = env.action_space.sample()
        observation, reward, done, infos = env.step(action)
        nstep += 1
        for i in range(env.n_agents):
            total_reward[i] += reward[i]
        if done[0]:
            num_episodes += 1
            draw = True
            print(f"Episode {num_episodes}, Step {nstep}")
            for i in range(env.n_agents):
                if "winner" in infos[i]:
                    draw = False
                    total_scores[i] += 1
                    print(
                        "Winner: Agent {}, Scores: {}, Total Episodes: {}".format(
                        	i, total_scores, num_episodes))
            if draw:
                print(
                    "Game Tied: Agent {}, Scores: {}, Total Episodes: {}".format(
                        i, total_scores, num_episodes))
            observation = env.reset()
            nstep = 0
            total_reward = [0.0 for _ in range(env.n_agents)]

            if num_episodes < max_episodes:
                print("-" * 5 + "Episode %d" % (num_episodes + 1) + "-" * 5)
                export_video(frames, f"{config.env}_{num_episodes}.mp4")
                frames = []
    export_video(frames, f"{config.env}.mp4")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Environments for Multi-agent competition")
    p.add_argument("--env", default="sumo-humans", type=str,
                   help=("competitive environment: run-to-goal-humans, "
                   	"run-to-goal-ants, you-shall-not-pass, sumo-humans, "
                   	"sumo-ants, kick-and-defend"))
    p.add_argument("--max-episodes", default=10, help="max number of matches",
                   type=int)

    config = p.parse_args()
    run(config)