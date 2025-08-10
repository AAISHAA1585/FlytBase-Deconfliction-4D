import numpy as np

class Trajectory:
    def __init__(self, waypoints, times=None, t_start=None, t_end=None):
        self.waypoints = np.array(waypoints)
        if times is not None:
            self.times = np.array(times)
            if len(self.times) != len(self.waypoints):
                raise ValueError("Times must match waypoints count")
        elif t_start is not None and t_end is not None:
            if len(self.waypoints) < 2:
                raise ValueError("At least 2 waypoints needed")
            diffs = np.diff(self.waypoints, axis=0)
            dists = np.linalg.norm(diffs, axis=1)
            cum_dist = np.cumsum(dists)
            total_dist = cum_dist[-1] if cum_dist.size > 0 else 0
            if total_dist == 0:
                raise ValueError("Waypoints have zero distance")
            frac = cum_dist / total_dist
            self.times = np.array([t_start] + (t_start + frac * (t_end - t_start)).tolist())
        else:
            raise ValueError("Provide times or t_start/t_end")
        
        sort_idx = np.argsort(self.times)
        self.times = self.times[sort_idx]
        self.waypoints = self.waypoints[sort_idx]
    
    def position_at(self, t):
        if t < self.times[0] or t > self.times[-1]:
            return None
        idx = np.searchsorted(self.times, t) - 1
        if idx < 0 or idx >= len(self.times) - 1:
            return None
        frac = (t - self.times[idx]) / (self.times[idx + 1] - self.times[idx])
        pos = self.waypoints[idx] + frac * (self.waypoints[idx + 1] - self.waypoints[idx])
        return pos