import numpy as np
import cluster


def kmeans(x, K, σ):
    # Start with random cluster means
    # μ = np.random.normal(0.0, σ, K)
    μ = np.array([[8,8], [3,3]])
    # Initialization
    n = 0
    while True:

        # Update configuration
        Xnew = cluster.config(x, μ)

        # Update centroids
        μnew = cluster.means(x, Xnew)

        # Update centroids
        Fnew = cluster.Fobj(x, μnew, Xnew)
        print(f'\nIteration n={n}')
        print(f'Configuration X=\n{Xnew.T}')
        print(f'Centroids μ={μnew}')
        print(f'Objective F={Fnew}')

        # Convergence check
        if (n > 0) and np.array_equal(Xnew, X):
            return Xnew, μnew

        # Iteration
        n = n + 1
        X = Xnew
        μ = μnew


x = np.array([[7,8], [4,6],[9,6], [5,7], [8,5]])
print(f'Input data: x={x}')

K = 2
σ = 2.0
Xopt, μopt = kmeans(x,K,σ)
Fopt = cluster.Fobj(x, μopt, Xopt)
print(f'\nK-means clustering result: X*=\n{Xopt.T}, μ*={μopt}, F*={Fopt}')