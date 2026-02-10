import time


def do_work(task_id: int, duration: float = 0.1) -> str:
    time.sleep(duration)
    return f"Task {task_id} completed"


def run_sync(tasks: int = 5) -> list[str]:
    results: list[str] = []

    for i in range(tasks):
        result = do_work(i, duration=0.1)
        results.append(result)

    return results


if __name__ == "__main__":
    start_time = time.perf_counter()
    results = run_sync(tasks=5)
    elapsed_time = time.perf_counter() - start_time

    print("Synchronous Results:")
    for result in results:
        print(f" {result}")

    print(f"\nTotal time: {elapsed_time:.2f} seconds")
    print("Note: Tasks ran one after another (synchronous execution)")
