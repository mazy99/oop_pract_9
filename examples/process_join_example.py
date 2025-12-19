#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process


def func() -> None:
    print("Hello from child Process")


if __name__ == "__main__":
    print("Hello from main Process")
    proc: Process = Process(target=func)
    proc.start()
    proc.join()
    print("Goodbye")
