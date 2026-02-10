import asyncio
import time


async def do_async_work(task_id: int, duration: float = 0.1) -> str:
    await asyncio.sleep(duration)
    return f"Task {task_id} completed"


async def run_asyncio(tasks: int = 5) -> list[str]:
    task_list = [do_async_work(i, 0.1) for i in range(tasks)]
    results: list[str] = await asyncio.gather(*task_list)

    return results


if __name__ == "__main__":
    start_time = time.perf_counter()
    results = asyncio.run(run_asyncio(tasks=5))
    elapsed_time = time.perf_counter() - start_time

    print("Asyncio Results:")
    for result in results:
        print(f" {result}")

    print(f"\nTotal time: {elapsed_time:.2f} seconds")
    print("Note: Tasks ran concurrently using asyncio (modern I/O-bound approach)")
