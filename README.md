# Device Management Algorithms

This project implements and simulates common Operating System algorithms under **Device Management**:

* **FCFS (First Come First Serve) Disk Scheduling**
* **SSTF (Shortest Seek Time First) Disk Scheduling**
* **FIFO (First In First Out) Page Replacement**

It also includes a **comparison mode** to evaluate all algorithms on the same dataset.

---

## 📌 Algorithms Implemented

### 1. FCFS (First Come First Serve)

* Disk scheduling algorithm
* Requests are served in the order they arrive
* Metric: **Total Head Movement**

### 2. SSTF (Shortest Seek Time First)

* Disk scheduling algorithm
* Chooses the request closest to the current head
* Metric: **Total Head Movement**

### 3. FIFO (First In First Out) Page Replacement

* Memory management algorithm
* Oldest page is replaced when a frame is full
* Metric: **Total Page Faults**

---

## ⚙️ How to Run

### General Syntax

```bash
python main.py [algorithm] --requests <list> [--head <position>] [--frames <n>] [--compare]
```

* `algorithm`: One of `fcfs`, `sstf`, `fifo`
* `--requests`: Sequence of requests (I/O requests for FCFS & SSTF, page references for FIFO)
* `--head`: Initial disk head position (default = 50, for FCFS/SSTF only)
* `--frames`: Number of frames (default = 3, for FIFO only)
* `--compare`: Runs **all algorithms** on the same dataset

---

### 🔹 Example Runs

#### FCFS

```bash
python main.py fcfs --requests 82 170 43 140 24 16 190 --head 50
```

Output:

* Order of execution
* Total head movement

#### SSTF

```bash
python main.py sstf --requests 82 170 43 140 24 16 190 --head 50
```

Output:

* Order of execution
* Total head movement

#### FIFO Page Replacement

```bash
python main.py fifo --requests 7 0 1 2 0 3 0 4 2 3 --frames 3
```

Output:

* Step-by-step page table updates
* Total page faults

---

### 🔹 Comparison Mode

Run all algorithms together for side-by-side results:

```bash
python main.py --compare --requests 82 170 43 140 24 16 190 --head 50 --frames 3
```

Output:

* FCFS results
* SSTF results
* FIFO results

---

## 📊 Report

A detailed summary of results (head movements, page faults, etc.) can be written in **REPORT.md** after running tests.
This enables performance comparison across algorithms.

---

## 📂 Project Structure

```
CS18L-Device-Management-Algorithm/
│── algo/
│   ├── fcfs.py   # FCFS disk scheduling
│   ├── sstf.py   # SSTF disk scheduling
│   ├── fifo.py   # FIFO page replacement
│── main.py       # Entry point, CLI parser
│── REPORT.md     # Summary of results
│── README.md     # This file
```

---

## 👨‍💻 Things to improve

=> To run with more device management algorithm (LOOK, C-LOOK, SCAN, C-SCAN, etc)
=> To improve in a more interactive way where users can input without using CLI
=> Visualization of data by utilizing MatPlotLib, etc
