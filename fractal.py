def mandelbrot_escape_iter(
    c: complex, max_iter: int = 300
) -> int:  # возвращает количество итераций до выхода за пределы множества Мандельброта
    z = 0j
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter


def random_complex() -> complex:
    import random

    return complex(random.uniform(-2.0, 1.0), random.uniform(-1.5, 1.5))


def generate_fractal_sequence(length: int = 15000, max_iter: int = 800) -> list[int]:
    # генерирует последовательность итераций для случайных комплексных чисел
    return [mandelbrot_escape_iter(random_complex(), max_iter) for _ in range(length)]


if __name__ == "__main__":
    seq = generate_fractal_sequence(5, 100)
    print(seq)
