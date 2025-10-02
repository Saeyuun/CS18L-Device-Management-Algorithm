import argparse

# Import algorithms directly
from algo.fcfs import run as fcfs
from algo.sstf import run as sstf
from algo.fifo import run as fifo

# Map algorithm names to functions
algorithms = {
    "fcfs": fcfs,
    "sstf": sstf,
    "fifo": fifo
}

def main():
    parser = argparse.ArgumentParser(description="Device Scheduling Algorithms")
    parser.add_argument("algorithm", choices=algorithms.keys(), help="Algorithm to run")
    parser.add_argument("--requests", nargs="+", type=int, required=True, help="Disk requests")
    parser.add_argument("--head", type=int, default=50, help="Initial head position")
    args = parser.parse_args()

    # Run the chosen algorithm
    result = algorithms[args.algorithm](args.requests, args.head)

    print(f"Algorithm: {args.algorithm.upper()}")
    print("Requests:", args.requests)
    print("Initial Head Position:", args.head)
    print("Order:", result["sequence"])
    if result["movement"] is not None:
        print("Total Head Movement:", result["movement"])


if __name__ == "__main__":
    main()