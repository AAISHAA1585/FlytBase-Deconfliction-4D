import numpy as np

def detect_conflicts(primary_traj, other_trajs, threshold=5.0, dt=1.0):
    conflicts = []
    t_min = primary_traj.times[0]
    t_max = primary_traj.times[-1]
    times = np.arange(t_min, t_max + dt / 2, dt)
    
    for t in times:
        pos_p = primary_traj.position_at(t)
        if pos_p is None:
            continue
        
        for i, other in enumerate(other_trajs):
            pos_o = other.position_at(t)
            if pos_o is None:
                continue
            
            dist = np.linalg.norm(pos_p - pos_o)
            if dist < threshold:
                mid_loc = ((pos_p + pos_o) / 2).tolist()
                conflicts.append({
                    'time': t,
                    'location': mid_loc,
                    'drone_id': i,
                    'dist': dist
                })
    return conflicts