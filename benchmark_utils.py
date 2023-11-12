import numpy as np
import timeit
import matplotlib.pyplot as plt
from typing import Callable, List, Any, Tuple

def benchmark_func(func: Callable, runs: int = 10, loops: int = 10, **kwargs) -> Tuple[float, float]:
    """
    Benchmark a function with attributes, loops times each run, each run makes statistics
    Returns mean and std
    """
    timer = timeit.Timer(lambda: func(**kwargs))
    times = timer.repeat(repeat=runs, number=loops)
    return np.mean(times), np.std(times)

def benchmark_comparison(func_list: List[Callable], var_iter: str, value_iter: List[Any], runs: int = 10, loops: int = 10, **kwargs) -> dict:
    """
    Benchmark several functions, iterating over a single attribute common to all functions
    Returns a dictionary with the name of the functions as keys, and a List of (mean, std) tuples
    """
    dict_benchmark = {}

    for func in func_list:
        benchmark_results = []
        
        for val in value_iter:
            kwargs_copy = kwargs.copy()
            kwargs_copy[var_iter] = val
            benchmark_results.append(
                benchmark_func(
                    func=func, 
                    runs=runs, 
                    loops=loops, 
                    **kwargs_copy,
                )
            )

        dict_benchmark[func.__name__] = benchmark_results
    return dict_benchmark

def plot_efficiencies(func_list: List[Callable], var_iter: str, value_iter: List[Any], runs: int = 10, loops: int = 10, **kwargs):
    """
    Plots the efficiencies compiled by benchmark_comparison
    """
    fig, ax = plt.subplots()

    dict_benchmarks = benchmark_comparison(
        func_list=func_list,
        var_iter=var_iter,
        value_iter=value_iter,
        runs=runs,
        loops=loops,
        **kwargs,
    )

    for func_name,benchmark in dict_benchmarks.items():
        mean_list, std_list = zip(*benchmark)
        ax.errorbar(value_iter, mean_list, yerr=std_list, marker='*', label=func_name)
    ax.set_xlabel(var_iter)
    ax.set_ylabel('Time (s)')
    ax.set_title(f'Benchmark: {runs} runs, {loops} loops each')
    ax.grid()
    ax.legend()
