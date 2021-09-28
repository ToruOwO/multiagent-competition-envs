import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env
from gym import spaces
import os

class MultiAgentScene(mujoco_env.MujocoEnv, utils.EzPickle):

    def __init__(self, xml_path, n_agents):
        self.n_agents = n_agents
        self._mujoco_init = False
        mujoco_env.MujocoEnv.__init__(self, xml_path, 5)
        self._mujoco_init = True
        utils.EzPickle.__init__(self)

    def simulate(self, actions):
        a = np.concatenate(actions, axis=0)
        self.do_simulation(a, self.frame_skip)

    def step(self, actions):
        '''
        Just to satisfy mujoco_init, should not be used
        '''
        assert not self._mujoco_init, 'step should not be called on Scene'
        return self._get_obs(), 0, False, None

    def _get_obs(self):
        '''
        Just to satisfy mujoco_init, should not be used
        '''
        assert not self._mujoco_init, '_get_obs should not be called on Scene'
        obs = np.concatenate([
            self.sim.data.qpos.flat,
            self.sim.data.qvel.flat
        ])
        return obs

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-.1, high=.1)
        qvel = self.init_qvel + self.np_random.randn(self.model.nv) * .1
        self.set_state(qpos, qvel)
        return None

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 0
        self.viewer.cam.distance = self.model.stat.extent * 0.55
        # self.viewer.cam.distance = self.model.stat.extent * 0.65
        # self.viewer.cam.distance = self.model.stat.extent * 1.5
        self.viewer.cam.lookat[2] += .8
        self.viewer.cam.elevation = -10
        # self.viewer.cam.distance = self.model.stat.extent * 0.4
        # self.viewer.cam.lookat[2] += 1.0
        # self.viewer.cam.elevation = -25
        # self.viewer.cam.azimuth = 0 if np.random.random() > 0.5 else 180
        self.viewer.cam.azimuth = 90
        # self.viewer.vopt.flags[8] = True
        # self.viewer.vopt.flags[9] = True
        rand = np.random.random()
        if rand < 0.33:
            self.viewer.cam.azimuth = 0
        elif 0.33 <= rand < 0.66:
            self.viewer.cam.azimuth = 90
        else:
            self.viewer.cam.azimuth = 180

    def render(
        self,
        mode="human",
        width=500,
        height=500,
        camera_id=None,
        camera_name=None,
    ):
        if mode == "rgb_array" or mode == "depth_array":
            if camera_id is not None and camera_name is not None:
                raise ValueError(
                    "Both `camera_id` and `camera_name` cannot be"
                    " specified at the same time."
                )

            no_camera_specified = camera_name is None and camera_id is None
            if no_camera_specified:
                camera_name = "track"

            if camera_id is None and camera_name in self.model._camera_name2id:
                camera_id = self.model.camera_name2id(camera_name)

            self._get_viewer(mode).render(width, height, camera_id=camera_id)

        if mode == "rgb_array":
            # window size used for old mujoco-py:
            data = self._get_viewer(mode).read_pixels(width, height, depth=False)
            # original image is upside-down, so flip it
            return data[::-1, :, :]
        elif mode == "depth_array":
            self._get_viewer(mode).render(width, height)
            # window size used for old mujoco-py:
            # Extract depth part of the read_pixels() tuple
            data = self._get_viewer(mode).read_pixels(width, height, depth=True)[1]
            # original image is upside-down, so flip it
            return data[::-1, :]
        elif mode == "human":
            self._get_viewer(mode).render()
