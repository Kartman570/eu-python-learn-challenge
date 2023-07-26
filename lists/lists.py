class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        max_val = 0
        result = []
        for val in input_list:
            max_val = val if val > max_val else max_val
        for val in input_list:
            val = max_val if val > 0 else val
            result.append(val)
        return result

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        min_val = 0
        max_val = len(input_list) - 1
        while min_val <= max_val:
            middle = (max_val - min_val) // 2 + min_val
            checked_num = input_list[middle]
            if checked_num == query:
                return middle
            if checked_num < query:
                min_val = middle + 1
            if checked_num > query:
                max_val = middle - 1
        return -1
