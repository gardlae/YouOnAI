# Minimizing z in optimization problems

Source: [Granola note](https://notes.granola.ai/d/c7bcef48-7a15-43ed-83a4-0985d545bd1b)  
Date: 2026-10-19

## Depth Estimation via Least Squares
- Goal: recover Z from image coordinates using minimization
- Minimize over Z: the squared distance between observed and predicted projections
  - Expand: ||x_dot||² + ||y_dot||² − 2(x·x_dot + y·y_dot)/Z + (x² + y²)/Z²
  - Take dZ derivative, set to zero
  - Multiply through by Z³ to isolate Z
- Closed-form solution:
  - Z = (x² + y²) / (x·x_dot + y·y_dot)
- Equivalent least squares framing:
  - Cast as ||K_min − AP||², where A = [x, y]ᵀ, K = [x_dot, y_dot]ᵀ
  - P = (AᵀA)⁻¹ Aᵀ K
  - AᵀA = x² + y² (scalar), so (AᵀA)⁻¹ = 1/(x² + y²)
  - AᵀK = x·x_dot + y·y_dot
  - P = 1/Z, confirming the same solution
## Essential Matrix Decomposition (Exercise 3)
- Given E = [[0, −1, 1], [1, 0, 0], [−1, 0, 0]]
- Task: decompose E = T× · R, find T and R up to scale
- Key observation: E is already antisymmetric
  - T× is antisymmetric by construction
  - For E = T× · R to hold with E already antisymmetric, R must be the identity
- Solution:
  - R = I (identity matrix)
  - T = [0, −1, 1]ᵀ (extracted directly from the antisymmetric structure of E)
## Midterm Reminder
- Next session is the midterm
