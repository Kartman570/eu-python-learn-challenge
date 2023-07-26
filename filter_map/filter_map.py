from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for obj in input_array:
            flag, value = func(obj)
            if flag:
                result.append(value)
        return result
