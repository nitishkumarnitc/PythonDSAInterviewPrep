from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target.

    TC: O(n), SC: O(n) for the hash map.
    """
    index = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in index:
            return [index[need], i]
        index[x] = i
    return []


def max_subarray(nums: List[int]) -> int:
    """Kadane's algorithm for maximum subarray sum.

    TC: O(n), SC: O(1).
    """
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def product_except_self(nums: List[int]) -> List[int]:
    """Return array where each element is product of all others.

    TC: O(n), SC: O(1) extra (output not counted).
    """
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res


def length_of_longest_substring_no_repeat(s: str) -> int:
    """Length of longest substring without repeating characters.

    TC: O(n), SC: O(min(n, alphabet)).
    """
    last = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best


def min_window_substring(s: str, t: str) -> str:
    """Smallest window in s containing all chars of t (with multiplicity).

    TC: O(|s| + |t|), SC: O(alphabet).
    """
    if not s or not t:
        return ""
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    required = len(need)
    formed = 0
    have = {}
    left = 0
    best_len = float("inf")
    best = (0, 0)
    for right, ch in enumerate(s):
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            formed += 1
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best = (left, right)
            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1
    if best_len == float("inf"):
        return ""
    l, r = best
    return s[l : r + 1]


def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return node where cycle begins, or None if no cycle.

    Floyd's cycle detection.
    TC: O(n), SC: O(1).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow


def num_islands(grid: List[List[str]]) -> int:
    """Count connected components of '1's in a 2D grid.

    TC: O(m * n), SC: O(m * n) recursion/stack in worst case.
    """
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


def coin_change(coins: List[int], amount: int) -> int:
    """Minimum number of coins to make up amount, or -1 if impossible.

    TC: O(amount * len(coins)), SC: O(amount).
    """
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == INF else dp[amount]


def length_of_LIS(nums: List[int]) -> int:
    """Length of LIS using patience sorting / binary search.

    TC: O(n log n), SC: O(n).
    """
    import bisect

    tails: List[int] = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

