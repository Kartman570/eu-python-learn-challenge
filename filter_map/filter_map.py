from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for obj in input_array:
            tmp = func(obj)
            if tmp[0]:
                result.append(tmp[1])
        return result
