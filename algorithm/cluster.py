import numpy as np

# Update configuration (cluster assignment indicator matrix)
def config(x,μ):
    K = len(μ)
    N = len(x)
    X = np.zeros((N,K))
    for i in range(N):
        dopt = np.inf
        kopt = K + 1
        for k in range(K):
            # todo: 多维计算 np.sum
            print('x[i]-μ[k]', x[i]-μ[k])
            print('x[i]-μ[k] sum is', np.sum((x[i]-μ[k])**2.0))
            d = np.sum((x[i]-μ[k])**2.0)
            # print(d)
            # if d less than dopt
            if d < dopt:
                dopt = d
                kopt = k
        X[i,kopt] = 1
    return X

# Update centroids (cluster means)
import numpy as np


def means(x, X):
    """
    计算每个簇的均值（质心）。

    参数:
    x: 每个数据点的特征值（形状为 (n_samples, n_features)）
    X: 每个数据点所属簇的指示矩阵（形状为 (n_samples, n_clusters)）

    返回:
    μ: 每个簇的均值（质心），形状为 (n_clusters, n_features)
    """
    # 计算每个簇的成员数量
    Nk = X.sum(axis=0)  # 每个簇的成员数量

    # 计算每个簇的特征总和
    Σk = (X.T @ x)  # 矩阵乘法，得到每个簇的特征总和

    # 计算均值（质心）
    μ = Σk / Nk[:, np.newaxis]  # 添加新轴以支持多维

    return μ

# Update objective (sum-of-squared errors)
def Fobj(x,μ,X):
    F = 0
    N = len(x)
    K = len(μ)
    for i in range(N):
        for k in range(K):
            F = F + X[i,k]*(x[i]-μ[k])**2.0
    return F
