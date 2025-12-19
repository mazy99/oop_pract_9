#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from multiprocessing_sum_series import SeriesCalculator

if __name__ == "__main__":
    calculator = SeriesCalculator(x=1.2, eps=1e-7)

    start_time = time.time()
    calculator.series_sum_sequential()
    sequential_time = time.time() - start_time
    print(f"Последовательное вычисление: {sequential_time:.6f} с")
    print(calculator)

    start_time = time.time()
    calculator.multiprocess_series()
    multiprocess_time = time.time() - start_time
    print(f"\nМногопроцессное вычисление: {multiprocess_time:.6f} с")
    print(calculator)
