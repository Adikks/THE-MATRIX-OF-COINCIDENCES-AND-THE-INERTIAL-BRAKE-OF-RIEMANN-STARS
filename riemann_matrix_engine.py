import mpmath
import pandas as pd

# Research-Grade Precision Setup
mpmath.mp.dps = 25 

def riemann_matrix_engine(n_stars):
    data = []
    for i in range(n_stars):
        # Capturing the location of the Star
        t_val = mpmath.zetazero(i + 1).imag
        t_prev = float(mpmath.zetazero(i).imag) if i > 0 else 0
        
        # Calculating Tension (Delta t) and Pressure (Psi)
        delta = float(t_val) - t_prev
        psi = sum(int(d) for d in str(int(t_val)) if d.isdigit())
        
        # The Kappa Constant
        kappa = delta * psi
        data.append({'n': i+1, 't': float(t_val), 'delta': delta, 'psi': psi, 'kappa': kappa})
    return pd.DataFrame(data)
