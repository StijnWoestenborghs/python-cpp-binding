from function import counting_stars_python
from function import counting_stars_cpp


def main():
    print("\n[PYTHON] Counting stars in Python ... ")
    value = 0
    n = 1000000000

    value_out, done = counting_stars_python(value, n)

    print(f"\t Done: {done}")
    print(f"\t Value out: {value_out}\n")
    print("-"*50)
    print("\n[CPP] Counting stars in C++ ... ")

    value_out, done = counting_stars_cpp(value, n)

    print(f"\t Done: {done}")
    print(f"\t Value out: {value_out}\n")


if __name__ == "__main__":
    main()