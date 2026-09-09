"""Example usage for LUP Factorization Skill."""
from client import LUPFactorization

def main():
    print("Executing LUP Factorization with Partial Pivoting...")
    A = [[2.0, 4.0, -2.0], [4.0, 9.0, -3.0], [-2.0, -3.0, 7.0]]
    L, U, P = LUPFactorization.factorize(A)
    print("L:", L)
    print("U:", U)
    print("Permutation P:", P)

    # Verify PA = LU
    PA = [A[P[i]] for i in range(3)]
    LU = [[sum(L[i][k] * U[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            assert abs(PA[i][j] - LU[i][j]) < 1e-3
    print("LUP Factorization verified successfully!")

if __name__ == "__main__":
    main()
