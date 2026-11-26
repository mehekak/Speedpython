import time
import dis
import cProfile
import pstats
import io
from collections import Counter


class SpeedPython:

    def opcode_analyzer(self, func):
        instructions = dis.get_instructions(func)
        count = Counter(i.opname for i in instructions)

        print("\n--- Opcode Analysis ---")
        for op, total in count.items():
            print(op, ":", total)

    def execution_profiler(self, func, *args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()

        print("\nExecution Time:",
              round(end - start, 6), "seconds")
        return result

    def slow_function_detector(self, func, *args):
        profiler = cProfile.Profile()
        profiler.enable()
        func(*args)
        profiler.disable()

        output = io.StringIO()
        stats = pstats.Stats(profiler, stream=output)
        stats.sort_stats("cumtime")
        stats.print_stats(5)

        print("\n--- Slow Function Report ---")
        print(output.getvalue())

    def performance_report(self, func, *args):
        print("\n===== SPEEDPYTHON REPORT =====")

        self.opcode_analyzer(func)
        result = self.execution_profiler(func, *args)
        self.slow_function_detector(func, *args)

        print("Program Result:", result)
        print("===== REPORT COMPLETED =====")


def sample_program(n):
    total = 0
    for i in range(n):
        total += i
    return total


if __name__ == "__main__":
    speed = SpeedPython()
    speed.performance_report(sample_program, 10000)