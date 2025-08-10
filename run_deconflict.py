import os
import json
from deconflict.io import load_primary, load_others
from deconflict.trajectory import Trajectory
from deconflict.detector import detect_conflicts
from deconflict.visualizer import visualize

def main():
    print("Loading mission data from JSON files...")
    primary_data = load_primary(os.path.join('scenarios', 'primary.json'))
    other_data = load_others(os.path.join('scenarios', 'others.json'))

    print("Creating trajectories...")
    primary_traj = Trajectory(
        waypoints=primary_data['waypoints'],
        t_start=primary_data['t_start'],
        t_end=primary_data['t_end']
    )
    other_trajs = [
        Trajectory(waypoints=d['waypoints'], times=d['times'])
        for d in other_data
    ]

    print("Detecting conflicts...")
    conflicts = detect_conflicts(primary_traj, other_trajs, threshold=5.0)
    print(f"Found {len(conflicts)} conflicts.")
    
    print("Generating animated visualization...")
    
    demo_dir = 'demo'
    os.makedirs(demo_dir, exist_ok=True)
    output_path = os.path.join(demo_dir, 'conflict_animation.gif')

    visualize(primary_traj, other_trajs, conflicts, filename=output_path)
    print("Visualization complete.")

if __name__ == "__main__":
    main()