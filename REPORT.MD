# Comparison Report

## 1. Dataset

* Disk requests: `82, 170, 43, 140, 24, 16, 190`
* Initial head position: `50`
* Page sequence: `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`
* Number of frames: `3`

---

## 2. Results

### 2.1 Disk Scheduling Algorithms

| Algorithm | Sequence Processed              | Total Head Movement |
| --------- | ------------------------------- | ------------------- |
| FCFS      | [82, 170, 43, 140, 24, 16, 190] | 642                 |
| SSTF      | [43, 24, 16, 82, 140, 170, 190] | 208                 |

**Observation:**

* FCFS follows arrival order but results in long head movements.
* SSTF minimizes movement by always serving the nearest request, leading to better efficiency.

---

### 2.2 Paging (Memory Management)

| Algorithm | Total Page Faults | Step-by-Step Table (Frames)  |
| --------- | ----------------- | ---------------------------- |
| FIFO      | 9                 | (show frames state per step) |

**Observation:**

* FIFO is simple but may not minimize faults.
* Other algorithms like LRU/Optimal could improve performance.


## 3. Conclusion

* **Disk Scheduling:** SSTF outperforms FCFS in terms of head movement, showing the benefit of prioritizing nearest requests. But noticing the pattern, there will be a noticable starvation with SSTF. 
* **Paging:** FIFO resulted in 9 page faults. While simple, it is not always optimal.
* **CPU Scheduling (if included):** Waiting time and turnaround vary depending on algorithm.

Overall, performance depends on the chosen metric:

* CPU → Waiting/Turnaround times
* Disk → Total head movement
* Memory → Page faults
