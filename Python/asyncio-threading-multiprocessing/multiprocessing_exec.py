import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def do_cpu_work(task_id: int, iterations: int = 1_000_000) -> str:
    result = 0
    for i in range(iterations):
        result += i * i

    return f"Task {task_id} completed (result: {result})"


def run_multiprocessing(tasks: int = 5, max_workers: int = 5) -> list[str]:
    results: list[str] = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_cpu_work, i, 1_000_000) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results


if __name__ == "__main__":
    start_time = time.perf_counter()
    results = run_multiprocessing(tasks=5, max_workers=5)
    elapsed_time = time.perf_counter() - start_time

    print("Multiprocessing Results:")
    for result in results:
        print(f" {result}")

    print(f"\nTotal time: {elapsed_time:.2f} seconds")
    print("Note: Tasks ran in parallel using separate processes (CPU-bound tasks)")
