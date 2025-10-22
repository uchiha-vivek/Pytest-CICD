class BinarySearch:
    def binary_search(self, nums: list[int], target: int) -> int:
        try:
            if not isinstance(nums, list):
                raise TypeError("Nums should be list")
            if not all(isinstance(x, int) for x in nums):
                raise ValueError("All elements must be integer")
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1
        except Exception as e:
            print(f"Error in binary search: {e}")
            return -1
