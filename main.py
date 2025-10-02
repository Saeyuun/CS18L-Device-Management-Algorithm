import argparse

# Import algorithms directly
from algo.fcfs import run as fcfs
from algo.sstf import run as sstf
from algo.fifo import run as fifo

algorithms = {
    "fcfs": fcfs,
    "sstf": sstf,
    "fifo": fifo
}

def main():
    parser = argparse.ArgumentParser(description="Scheduling / Paging Algorithms")
    parser.add_argument("algorithm", choices=algorithms.keys(), help="Algorithm to run")
    parser.add_argument("--requests", nargs="+", type=int, required=True, help="Disk requests or page sequence")
    parser.add_argument("--head", type=int, default=50, help="Initial head position (for FCFS/SSTF)")
    parser.add_argument("--frames", type=int, default=3, help="Number of frames (for FIFO page replacement)")
    args = parser.parse_args()

    if args.algorithm == "fifo":
        result = fifo(args.requests, args.frames)
        print(f"Algorithm: FIFO Page Replacement")
        print("Page sequence:", args.requests)
        print("Frames:", args.frames)
        for i, step in enumerate(result["sequence"]):
            print(f"Step {i+1}: {step}")
        print("Total Page Faults:", result["faults"])
    else:
        result = algorithms[args.algorithm](args.requests, args.head)
        print(f"Algorithm: {args.algorithm.upper()}")
        print("Requests:", args.requests)
        print("Initial Head Position:", args.head)
        print("Order:", result["sequence"])
        if result["movement"] is not None:
            print("Total Head Movement:", result["movement"])


if __name__ == "__main__":
    main()
