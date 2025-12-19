#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import ceil
from multiprocessing import Process, Queue, cpu_count


class SeriesCalculator:

    def __init__(self, x: float = 1.2, eps: float = 10**-7) -> None:

        self.x: float = x
        self.eps: float = eps

        self.series_sum: float | None = None
        self.analytic_value: float = self._analytic_function()

    def _series_term(self, n: int) -> float:
        return ((-1) ** n) * (self.x**n) / (2 ** (n + 1))

    def _analytic_function(self) -> float:
        return 1 / (2 + self.x)

    def series_sum_sequential(self) -> float:
        s = 0.0
        n = 0
        while True:
            term = self._series_term(n)
            if abs(term) < self.eps:
                break
            s += term
            n += 1
        self.series_sum = s
        return s

    @staticmethod
    def _part_sum(x: float, n_start: int, n_end: int, eps: float, queue: Queue) -> None:
        s: float = 0.0

        for n in range(n_start, n_end):
            term = ((-1) ** n) * (x**n) / (2 ** (n + 1))
            if abs(term) < eps:
                break
            s += term
        queue.put(s)

    def multiprocess_series(self) -> float:

        n_proc: int = cpu_count()
        queue: Queue = Queue()

        N: int = 1000
        chunk_size: int = ceil(N / n_proc)

        processes: list[Process] = []

        for i in range(n_proc):
            n_start: int = i * chunk_size
            n_end: int = (i + 1) * chunk_size
            p = Process(
                target=self._part_sum, args=(self.x, n_start, n_end, self.eps, queue)
            )
            processes.append(p)
            p.start()

        total_sum: float = 0.0
        for _ in processes:
            total_sum += queue.get()

        for p in processes:
            p.join()

        self.series_sum = total_sum
        return total_sum

    def absolute_error(self) -> float:

        if self.series_sum is None:
            raise ValueError("Сначала нужно вызвать multiprocess_series()")
        return abs(self.series_sum - self.analytic_value)

    def __str__(self) -> str:
        return (
            f"Ряд: S = Σ [(-1)^n * x^n / 2^(n+1)], n = 0..∞\n"
            f"x = {self.x}, eps = {self.eps}\n"
            f"Сумма ряда S = {self.series_sum}\n"
            f"Аналитическое значение y = {self.analytic_value}\n"
            f"Абсолютная погрешность |S - y| = "
            f"{self.absolute_error() if self.series_sum else 'N/A'}"
        )
