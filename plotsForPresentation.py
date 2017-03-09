def 3dMethod(p, p2):
    p = segmentedlung_student_pat0.transpose(2, 1, 0)
    p2 = segmentedlung_watershed_pat0.transpose(2, 1, 0)
    verts, faces = measure.marching_cubes(p, -500)
    verts2, faces2 = measure.marching_cubes(p2, -500)

    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot(121, projection='3d', axisbg='white')
    ax2 = fig.add_subplot(122, projection='3d', axisbg='white')
    # mesh = Poly3DCollection(verts[faces], facecolors='blue', linewidths=1, alpha=0.1)
    # ax.add_collection3d(mesh)
    ax.add_collection3d(Line3DCollection(verts[faces], colors='blue', linewidths=0.1, linestyles=':', alpha=0.1))
    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])
    ax.set_title('Segmentation 3d')
    ax2.add_collection3d(Line3DCollection(verts2[faces2], colors='blue', linewidths=0.1, linestyles=':', alpha=0.1))
    ax2.set_xlim(0, p2.shape[0])
    ax2.set_ylim(0, p2.shape[1])
    ax2.set_zlim(0, p2.shape[2])
    ax2.set_title('Segmentation Watershed')

    plt.show()


def print_pointcloud(images1, images2, interval_begin=-1000, interval_end=165):

    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot(121, projection='3d', axisbg='white')
    ax2 = fig.add_subplot(122, projection='3d', axisbg='white')


    #Get Coordinates where HU values are between a certain interval
    ii = np.where((images1 >= interval_begin) & (images1 <= interval_end))
    ii = np.where((images1 >= interval_begin) & (images1 <= interval_end))
    # ii = (array([0,0,0, ..., 334, 334, 334], dtype=int64),
    #       array([ 84,  84,  84, ..., 170, 170, 170], dtype=int64),
    #       array([233, 234, 235, ...,  99, 100, 101], dtype=int64))

    z_vals = ii[0]
    x_vals = ii[1]
    y_vals = ii[2]

    print("Number of points:", len(y_vals))

    #Remove every second point from list (because of performance issues)
    z_vals = np.delete(z_vals, np.arange(0,z_vals.size,2))
    x_vals = np.delete(x_vals, np.arange(0,x_vals.size,2))
    y_vals = np.delete(y_vals, np.arange(0,y_vals.size,2))

    z_vals = np.delete(z_vals, np.arange(0,z_vals.size,2))
    x_vals = np.delete(x_vals, np.arange(0,x_vals.size,2))
    y_vals = np.delete(y_vals, np.arange(0,y_vals.size,2))

    #Plot all points:
    ax.scatter(y_vals, x_vals, z_vals)
    pyplot.show()
