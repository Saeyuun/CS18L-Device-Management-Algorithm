import argparse
from algo.fcfs import fcfs
from algo.sstf import sstf
from algo.fifo import fifo


def run_fcfs(requests, head):
    order, movement = fcfs(requests, head)
    print("\n[FCFS]")
    print("Order of execution:", order)
    print("Total head movement:", movement)
    return movement

def run_sstf(requests, head):
    order, movement = sstf(requests, head)
    print("\n[SSTF]")
    print("Order of execution:", order)
    print("Total head movement:", movement)
    return movement

def run_fifo(requests, frames):
    faults, steps = fifo(requests, frames)
    print("\n[FIFO Page Replacement]")
    for i, step in enumerate(steps, 1):
        print(f"Step {i}: {step}")
    print("Total page faults:", faults)
    return faults

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--requests", nargs="+", type=int, required=True,
                        help="Sequence of requests (I/O or pages)")
    parser.add_argument("--head", type=int, default=50, help="Initial head position")
    parser.add_argument("--frames", type=int, default=3, help="Number of frames for paging")
    parser.add_argument("--compare", action="store_true", help="Run all algorithms for comparison")
    parser.add_argument("algorithm", nargs="?", choices=["fcfs", "sstf", "fifo"],
                        help="Choose an algorithm to run")

    args = parser.parse_args()

    if args.compare:
        print("\n=== Running Comparison ===")
        run_fcfs(args.requests, args.head)
        run_sstf(args.requests, args.head)
        run_fifo(args.requests, args.frames)
    else:
        if args.algorithm == "fcfs":
            run_fcfs(args.requests, args.head)
        elif args.algorithm == "sstf":
            run_sstf(args.requests, args.head)
        elif args.algorithm == "fifo":
            run_fifo(args.requests, args.frames)
