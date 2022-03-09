## Exercise 1

> ECNU CS2018 怀尚禹 10185102221

#### Mission 1: Find the car

1. Basic structure
   * Use `cv2.imread()` to read an image
   * use `matplotlib.pyplot` (commonly imported as 'plt') to show image
2. Solve the linear system
   * Use `numpy.linalg.solve()`
3. Image cropping
   * For an image read from `cv2.imread()`, use `image[a:b, c:d]` to crop



#### Mission 2: Scale and gray

1. Image scale

   * Use `cv2.resize()` to scale
     * Notice that scale can sometimes be complex because you can scale by axis or scale by proportion. 
     * Need to know height/width if you want to scale by proportion

2. Convert to gray version

   * Use `cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)` to convert

     * When showing the image using `plt`, pay attention to `cmap`

     ```python
     plt.imshow(gray, cmap='gray')
     ```

     * `cmap` is a coloring scheme



#### Mission 3: Improve Jarvis

1. Select Region Of Interest

   `cv2.selectROI()` will start an UI conversation to let user crop image by clicking mouse. It returns 4 parameters which correspond to `image[a:b, c:d]` while cropping in part 3. 

2. Use linear algebra (Inverse of determinant) to generate a new linear system. 

