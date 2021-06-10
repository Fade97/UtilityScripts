import imageio

filenames = ['scanImage' + str(f) + '.jpg' for f in range(70)]

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('video.gif', images)
