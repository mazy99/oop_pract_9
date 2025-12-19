#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from multiprocessing import Process


class CustomProcess(Process):
    def __init__(self, limit: int) -> None:
        super().__init__()
        self._limit = limit

    def run(self) -> None:
        for i in range(self._limit):
            print(f"From CustomProcess: {i}")


if __name__ == "__main__":
    cpr: CustomProcess = CustomProcess(5)
    cpr.start()
