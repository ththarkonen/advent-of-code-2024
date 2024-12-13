import numpy as np

def get():

    kernelDims = ( 3, 3)
    kernel0 = np.zeros( kernelDims )
    kernel1 = np.zeros( kernelDims )
    kernel2 = np.zeros( kernelDims )
    kernel3 = np.zeros( kernelDims )

    kernel4 = np.zeros( kernelDims )
    kernel5 = np.zeros( kernelDims )
    kernel6 = np.zeros( kernelDims )
    kernel7 = np.zeros( kernelDims )

    kernel8 = np.zeros( kernelDims )
    kernel9 = np.zeros( kernelDims )
    kernel10 = np.zeros( kernelDims )
    kernel11 = np.zeros( kernelDims )

    kernel12 = np.zeros( kernelDims )

    kernel0[ 1, 1] = 1
    kernel0[ 1, 0] = 1
    kernel0[ 0, 1] = 1

    kernel0[ 1, 2] = -1
    kernel0[ 2, 1] = -1

    kernel1[ 1, 1] = 1
    kernel1[ 0, 1] = 1
    kernel1[ 1, 2] = 1

    kernel1[ 2, 1] = -1
    kernel1[ 1, 0] = -1

    kernel2[ 1, 1] = 1
    kernel2[ 2, 1] = 1
    kernel2[ 1, 2] = 1

    kernel2[ 0, 1] = -1
    kernel2[ 1, 0] = -1

    kernel3[ 1, 1] = 1
    kernel3[ 2, 1] = 1
    kernel3[ 1, 0] = 1

    kernel3[ 0, 1] = -1
    kernel3[ 1, 2] = -1

    kernel4[ 1, 1] = 1
    kernel4[ 1, 0] = 1
    kernel4[ 0, 0] = 1
    kernel4[ 0, 1] = -1

    kernel5[ 1, 1] = 1
    kernel5[ 0, 1] = 1
    kernel5[ 0, 2] = 1
    kernel5[ 1, 2] = -1

    kernel6[ 1, 1] = 1
    kernel6[ 1, 2] = 1
    kernel6[ 2, 2] = 1
    kernel6[ 2, 1] = -1

    kernel7[ 1, 1] = 1
    kernel7[ 2, 1] = 1
    kernel7[ 2, 0] = 1
    kernel7[ 1, 0] = -1

    kernel8[ 1, 1] = 1
    kernel8[ 1, 0] = 1

    kernel8[ 1, 2] = -1
    kernel8[ 0, 1] = -1
    kernel8[ 2, 1] = -1

    kernel9[ 1, 1] = 1
    kernel9[ 0, 1] = 1

    kernel9[ 1, 0] = -1
    kernel9[ 1, 2] = -1
    kernel9[ 2, 1] = -1

    kernel10[ 1, 1] = 1
    kernel10[ 1, 2] = 1

    kernel10[ 0, 1] = -1
    kernel10[ 1, 0] = -1
    kernel10[ 2, 1] = -1

    kernel11[ 1, 1] = 1
    kernel11[ 2, 1] = 1

    kernel11[ 0, 1] = -1
    kernel11[ 1, 0] = -1
    kernel11[ 1, 2] = -1

    kernel12[ 1, 1] = 1
    kernel12[ 0, 1] = -1
    kernel12[ 2, 1] = -1
    kernel12[ 1, 0] = -1
    kernel12[ 1, 2] = -1

    neighbours = np.ones( kernelDims )
    neighbours[ 1, 1] = 0

    kernelsOuterCorner = [ kernel0, kernel1, kernel2, kernel3]
    kernelsInnerCorner = [ kernel4, kernel5, kernel6, kernel7]
    pointKernels = [ kernel8, kernel9, kernel10, kernel11]

    kernels = []

    for kernel in kernelsOuterCorner:

        kernelValuePair = ( kernel, 3, 1)
        kernels.append( kernelValuePair )

    for kernel in kernelsInnerCorner:

        kernelValuePair = ( kernel, 3, 1)
        kernels.append( kernelValuePair )

    for kernel in pointKernels:

        kernelValuePair = ( kernel, 2, 2)
        kernels.append( kernelValuePair )

    kernelValuePair = ( kernel12, 1, 4)
    kernels.append( kernelValuePair )

    return kernels