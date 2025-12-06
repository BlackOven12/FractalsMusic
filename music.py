import numpy as np
from scipy.io.wavfile import write


def get_sine(
    sample_rate=44100,  # стандартная частота дискретизации CD-качества
    duration=0.3,  # длительность одной ноты в секундах
    frequency=440.0,  # частота звука в герцах (440 = ля первой октавы)
    amplitude=0.5,  # громкость от 0.0 до 1.0
) -> np.ndarray:
    if duration <= 0 or frequency <= 0:
        return np.zeros(0, dtype=np.float64)

    samples = round(duration * sample_rate)

    if samples <= 0:
        return np.zeros(0, dtype=np.float64)

    t = np.linspace(0, samples / sample_rate, samples, endpoint=False)

    return amplitude * np.sin(2 * np.pi * frequency * t)


def generate_sines_wav(sines: list[np.ndarray], sample_rate=44100):
    res = np.concatenate(sines)
    write("music.wav", sample_rate, np.int16(res * 32767))


def generate_random_wav(
    sample_rate: int = 44100, amplitude: float = 0.7, length: int = 10
):
    import fractal

    sines = []
    for _ in range(length):
        seq = fractal.generate_fractal_sequence(2, 100)
        sines.append(
            get_sine(sample_rate, 0.5 + seq[0] / 200, seq[1] * 5.2 + 80, amplitude)
        )
    generate_sines_wav(sines, sample_rate)
