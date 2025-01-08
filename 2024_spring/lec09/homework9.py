import numpy as np

def fourier_synthesis(num_harmonics, X, T0):
    """
    Use Fourier synthesis to resynthesize speech from its Fourier transform.
    
    @param:
    num_harmonics (scalar): the number of harmonics to resynthesize
    X (np.ndarray(N)): a length-N Fourier transform
    T0 (scalar): the pitch period, in samples
        
    @result:
    x (np.ndarray(N)): a length-N waveform, resynthesized using Fourier synthesis
    """
    N = len(X)  # Length of the Fourier transform
    n = np.arange(N)  # Time indices
    x = np.zeros(N)  # Initialize the output waveform

    # Fourier synthesis
    for l in range(1, num_harmonics + 1):
        harmonic_idx = l * N // T0
        if harmonic_idx >= N:
            break  # Stop if the index exceeds the Fourier transform length
        magnitude = np.abs(X[harmonic_idx])  # Magnitude of the harmonic
        phase = np.angle(X[harmonic_idx])  # Phase of the harmonic
        x += magnitude * np.cos(2 * np.pi * l * n / T0 + phase)

    x *= 2 / N  # Normalize the waveform
    return x
