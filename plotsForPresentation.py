



def threeDMethod(image1, image2):
    p = image1.transpose(2, 1, 0)
    p2 = image2.transpose(2, 1, 0)
    verts, faces = measure.marching_cubes(p, -500)
    verts2, faces2 = measure.marching_cubes(p2, -500)

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(121, projection='3d', axisbg='white')
    ax2 = fig.add_subplot(122, projection='3d', axisbg='white')
    # mesh = Poly3DCollection(verts[faces], facecolors='blue', linewidths=1, alpha=0.1)
    # ax.add_collection3d(mesh)
    ax.add_collection3d(Line3DCollection(verts[faces], colors='blue', linewidths=0.1, linestyles=':', alpha=0.1))
    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])
    ax.set_title('Segmentation 3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax2.add_collection3d(Line3DCollection(verts2[faces2], colors='blue', linewidths=0.1, linestyles=':', alpha=0.1))
    ax2.set_xlim(0, p2.shape[0])
    ax2.set_ylim(0, p2.shape[1])
    ax2.set_zlim(0, p2.shape[2])
    ax2.set_title('Segmentation Watershed')
    ax2.set_xlabel('X Label')
    ax2.set_ylabel('Y Label')
    ax2.set_zlabel('Z Label')

    plt.show()


def rangeReduce(images,interval_begin=-1000, interval_end=165):
    ii = np.where((images >= interval_begin) & (images <= interval_end))

    z_vals = ii[0]
    x_vals = ii[1]
    y_vals = ii[2]

    z_vals = np.delete(z_vals, np.arange(0,z_vals.size,2))
    x_vals = np.delete(x_vals, np.arange(0,x_vals.size,2))
    y_vals = np.delete(y_vals, np.arange(0,y_vals.size,2))

    z_vals = np.delete(z_vals, np.arange(0,z_vals.size,2))
    x_vals = np.delete(x_vals, np.arange(0,x_vals.size,2))
    y_vals = np.delete(y_vals, np.arange(0,y_vals.size,2))
    return z_vals, x_vals, y_vals

def print_pointcloud(images1, images2, interval_begin=-1000, interval_end=165):

    seg3dZ, seg3dX, seg3dY = rangeReduce(images1)
    segWaterZ, segWaterX, segWaterY = rangeReduce(images2)

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(121, projection='3d', axisbg='white')
    ax2 = fig.add_subplot(122, projection='3d', axisbg='white')

    ax.scatter(seg3dY, seg3dX, seg3dZ, c='blue', marker='.', alpha=0.5)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Segmentation 3d')
    ax2.scatter(segWaterY, segWaterX, segWaterZ, c='blue', marker='.', alpha=0.5)
    ax2.set_xlabel('X Label')
    ax2.set_ylabel('Y Label')
    ax2.set_zlabel('Z Label')
    ax2.set_title('Segmentation Watershed')

    plt.show()
