import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def do_work(task_id: int, duration: float = 0.1) -> str:
    time.sleep(duration)
    return f"Task {task_id} completed"


def run_treading(tasks: int = 5, max_workers: int = 5) -> list[str]:
    results: list[str] = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_work, i, 0.1) for i in range(tasks)]

        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results


if __name__ == "__main__":
    start_time = time.perf_counter()
    results = run_treading(tasks=5)
    elapsed_time = time.perf_counter() - start_time

    print("Threading Results:")
    for result in results:
        print(f" {result}")

    print(f"\nTotal time: {elapsed_time:.2f} seconds")
    print("Note: Tasks ran concurrently using threads (I/O-bound tasks)")
