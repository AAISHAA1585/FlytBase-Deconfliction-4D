import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import os

def visualize(primary_traj, other_trajs, conflicts, filename='animation.gif'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')
    
    colors = ['green', 'red', 'cyan']
    
    line_primary, = ax.plot([], [], [], color=colors[0], linewidth=3, label='Drone 1 Path')
    lines_others = [ax.plot([], [], [], color=colors[i+1], linewidth=3, label=f'Drone {i+2} Path')[0] for i in range(len(other_trajs))]
    
    p_point, = ax.plot([], [], [], color=colors[0], marker='s', markersize=15, alpha=0.8, label='Drone 1')
    o_points = [ax.plot([], [], [], color=colors[i+1], marker='s', markersize=12, alpha=0.8, label=f'Drone {i+2}')[0] for i in range(len(other_trajs))]
    
    conflict_cross, = ax.plot([], [], [], 'rX', markersize=20, markeredgewidth=3, label='Conflict Point')
    
    # Initialize the scatter plot for the conflict region with empty data
    conflict_region_scatter = ax.scatter([], [], [], s=1000, color='red', alpha=0.2, label='Conflict Region')
    
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z (Altitude)', fontsize=12)
    ax.set_title('3D Drone Trajectories & Conflicts', fontsize=14, color='white')
    ax.legend(loc='upper right', fontsize=10, facecolor='black', edgecolor='white', labelcolor='white')
    ax.grid(True)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')
    
    all_trajs = [primary_traj] + other_trajs
    all_points = np.concatenate([t.waypoints for t in all_trajs])
    ax.set_xlim(np.min(all_points[:, 0]) - 10, np.max(all_points[:, 0]) + 10)
    ax.set_ylim(np.min(all_points[:, 1]) - 10, np.max(all_points[:, 1]) + 10)
    ax.set_zlim(np.min(all_points[:, 2]) - 10, np.max(all_points[:, 2]) + 10)
    
    t_min, t_max = primary_traj.times[0], primary_traj.times[-1]
    num_frames = 400
    times = np.linspace(t_min, t_max, num_frames)
    
    def update(frame):
        t = times[frame]
        ax.set_title(f'3D Drone Trajectories & Conflicts (Time: {t:.2f}s)', color='white')
        
        pos_p = primary_traj.position_at(t)
        if pos_p is not None:
            p_path_until_t = np.array([primary_traj.position_at(t_i) for t_i in times[:frame+1] if primary_traj.position_at(t_i) is not None])
            line_primary.set_data_3d(p_path_until_t[:, 0], p_path_until_t[:, 1], p_path_until_t[:, 2])
            p_point.set_data_3d([pos_p[0]], [pos_p[1]], [pos_p[2]])
        else:
            p_point.set_data_3d([], [], [])
        
        for i, traj in enumerate(other_trajs):
            pos_o = traj.position_at(t)
            if pos_o is not None:
                o_path_until_t = np.array([traj.position_at(t_i) for t_i in times[:frame+1] if traj.position_at(t_i) is not None])
                lines_others[i].set_data_3d(o_path_until_t[:, 0], o_path_until_t[:, 1], o_path_until_t[:, 2])
                o_points[i].set_data_3d([pos_o[0]], [pos_o[1]], [pos_o[2]])
            else:
                o_points[i].set_data_3d([], [], [])
        
        c_pos_list = [conf['location'] for conf in conflicts if abs(conf['time'] - t) < 5]
        
        if c_pos_list:
            c_pos = np.array(c_pos_list)
            # Use the correct method for updating scatter plot data
            conflict_region_scatter._offsets3d = (c_pos[:, 0], c_pos[:, 1], c_pos[:, 2])
            conflict_cross.set_data_3d(c_pos[:, 0], c_pos[:, 1], c_pos[:, 2])
        else:
            conflict_region_scatter._offsets3d = ([], [], [])
            conflict_cross.set_data_3d([], [], [])
        
        return [line_primary, *lines_others, p_point, *o_points, conflict_cross, conflict_region_scatter]
    
    ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)
    ani.save(filename, writer='pillow', fps=20, dpi=100)
    plt.close(fig)