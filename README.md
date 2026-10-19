# Duty Roster Rotation

## Problem
Rotate a list of names to the right by `k` places. Names that move past the end wrap around to the front.

## Approach
Let `n` be the number of names. First calculate `k % n` to remove complete rotations. Then use list slicing to move the final `k` names to the front.

## Run
Requires Python 3.

```bash
python main.py
```

Expected output:
```text
['D', 'E', 'A', 'B', 'C']
['D', 'E', 'A', 'B', 'C']
```

## Complexity
- Time: `O(n)` because slicing creates the rotated list.
- Extra space: `O(n)` for the returned list.
- Rotating one place at a time, `k` times can take `O(n * k)` time, which is too slow when `k` is very large.
