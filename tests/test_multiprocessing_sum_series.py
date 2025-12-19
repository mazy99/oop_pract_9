#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

import pytest

from tasks.multiprocessing_sum_series import SeriesCalculator


@pytest.mark.parametrize(
    "x, eps",
    [
        (1.2, 1e-7),
        (0.5, 1e-8),
        (-0.7, 1e-7),
        (0.0, 1e-10),
    ],
)
def test_sequential_sum_close_to_analytic(x, eps):
    calc = SeriesCalculator(x=x, eps=eps)
    s = calc.series_sum_sequential()
    assert math.isclose(s, calc.analytic_value, rel_tol=1e-6)


@pytest.mark.parametrize(
    "x, eps",
    [
        (1.2, 1e-7),
        (0.5, 1e-8),
        (-0.7, 1e-7),
        (0.0, 1e-10),
    ],
)
def test_multiprocess_sum_close_to_analytic(x, eps):
    calc = SeriesCalculator(x=x, eps=eps)
    s = calc.multiprocess_series()
    assert math.isclose(s, calc.analytic_value, rel_tol=1e-6)


def test_absolute_error_after_calculation():
    calc = SeriesCalculator(x=1.2, eps=1e-7)
    calc.series_sum_sequential()
    error = calc.absolute_error()
    assert 0 <= error < 1e-6


def test_absolute_error_without_calculation_raises():
    calc = SeriesCalculator(x=1.2, eps=1e-7)
    with pytest.raises(ValueError):
        calc.absolute_error()


def test_str_contains_key_info():
    calc = SeriesCalculator(x=1.2, eps=1e-7)
    calc.series_sum_sequential()
    s = str(calc)
    assert "Сумма ряда" in s
    assert "Аналитическое значение" in s
    assert "Абсолютная погрешность" in s
