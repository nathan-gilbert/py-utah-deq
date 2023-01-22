"""
Examples of how to use this library.
"""
from src.py_utah_deq.utah_deq import UtahDEQ


if __name__ == "__main__":
    deq = UtahDEQ()
    print(deq.get_latest_aqi())
