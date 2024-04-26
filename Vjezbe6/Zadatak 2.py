import harmonic_oscillator as harm
A=harm.HarmonicOscillator(2, 100, 0.1, 0)
B=harm.HarmonicOscillator(2, 100, 0.1, 0)
C=harm.HarmonicOscillator(2, 100, 0.1, 0)
D=harm.HarmonicOscillator(2, 100, 0.1, 0)
print(A.period(0.1))
print(B.period(0.01))
print(C.period(0.001))
print(D.period(0.0001))