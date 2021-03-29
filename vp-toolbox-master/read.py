import scipy.io
print("Eurasian")
mat = scipy.io.loadmat("/Users/harrybeggs/Desktop/Datasets/EurasianCitiesBase-3/001.mat")
print(mat)

mat2 = scipy.io.loadmat("/Users/harrybeggs/Desktop/Datasets/EurasianCitiesBase-3/001hor.mat")
print(mat2)

mat3 = scipy.io.loadmat("/Users/harrybeggs/Desktop/Datasets/EurasianCitiesBase-3/001VP.mat")
print(mat3)

print("York")
mat = scipy.io.loadmat("YorkUrbanDB/P1020177/P1020177GroundTruthVP_CamParams.mat")
print(mat)

mat2 = scipy.io.loadmat("YorkUrbanDB/P1020177/P1020177GroundTruthVP_Orthogonal_CamParams.mat")
print(mat2)

mat3 = scipy.io.loadmat("YorkUrbanDB/P1020177/P1020177LinesAndVP.mat")
print(mat3)

print("Toulouse")
mat = scipy.io.loadmat("toulouse_dataset/tvpd_dataset/img_1284.mat")
print(mat)
