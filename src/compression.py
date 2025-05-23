import numpy as np

def split_by_channels(img: np.ndarray):
    n_channels = img.shape[2]
    channels = tuple()
    for i in range(n_channels):
        channels += (img[:, :, i],)
    
    return channels

def compress(data: np.ndarray, threshold: int):
    U, S, V = np.linalg.svd(data)
    S = np.diag(S)
    return np.clip(U[:, :threshold] @ S[:threshold, :threshold] @ V[:threshold, :], 0, 255)
