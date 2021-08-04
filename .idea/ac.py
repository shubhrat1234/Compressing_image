import os
import sys

from PIL import Image
import numpy as np

def initialize_K_centroids(X, K):
    """ Choose K points from X at random """
    m = len(X)
    return X[np.random.choice(m, K, replace=False), :]
def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    print(m)
    for i in range(m):
        # Find distances
        distances = np.linalg.norm(X[i] - centroids, axis=1)

        # Assign closest cluster to c[i]
        c[i] = np.argmin(distances)
        if i % 10000 == 0:
            print(i)

    return c
def compute_means(X, idx, K):
    _, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        examples = X[np.where(idx == k)]
        mean = [np.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids
def find_k_means(X, K, max_iters=10):
    centroids = initialize_K_centroids(X, K)
    previous_centroids = centroids
    for _ in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        print("K==1")
        centroids = compute_means(X, idx, K)
        if (centroids == previous_centroids).all():
            # The centroids aren't moving anymore.
            return centroids
        else:
            previous_centroids = centroids

    return centroids, idx
def load_image(path):
    """ Load image from path. Return a numpy array """
    image = Image.open(path)
    return np.asarray(image) / 255

def compress():
    image_path = "/Users/shubhrat/Downloads/i4.jpg"
    assert os.path.isfile(image_path)
    image = load_image(image_path)
    w, h, d = image.shape
    print('Image found with width: {}, height: {}, depth: {}'.format(w, h, d))
    X = image.reshape((w * h, d))
    K = 3
    colors, _ = find_k_means(X, K, max_iters=3)
    x1=2
    print(x1)
    idx = find_closest_centroids(X, colors)
    idx = np.array(idx, dtype=np.uint8)
    X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
    compressed_image = Image.fromarray(X_reconstructed)
    compressed_image.save('out.png')

if __name__ == '__main__':
    compress()
