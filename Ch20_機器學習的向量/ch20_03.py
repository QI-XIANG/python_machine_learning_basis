import numpy as np

def cosine_similarity(va, vb):
    norm_a = np.linalg.norm(va)
    norm_b = np.linalg.norm(vb)
    dot_ab = np.dot(va, vb)
    cos_angle = dot_ab / (norm_a * norm_b)
    return cos_angle

a = np.array([2, 1, 1, 1, 0, 0, 0, 0])
b = np.array([1, 1, 0, 0, 1, 1, 1, 0])
c = np.array([1, 1, 0, 0, 1, 1, 0, 1])

print("a和b的相似度 = {0:5.3f}".format(cosine_similarity(a, b)))
print("a和c的相似度 = {0:5.3f}".format(cosine_similarity(a, c)))
print("b和c的相似度 = {0:5.3f}".format(cosine_similarity(b, c)))