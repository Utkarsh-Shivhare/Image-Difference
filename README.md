# Image-Difference

Steps involved in finding the differnce:
1.Converting the PDF to image , Used pdf2image library of python for that.
![result](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/938fe1f7-30fd-4146-b153-aa866ec878a5)
![result2](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/e719f058-1e00-4932-a026-032fb5819b82)
2.Resiging and processing the image to grayscale.
3.Finding the absolute difference between the images, which will give us the part of the images that are different from each other.
4.Then calculated the coutour our the image and and marked wherever the area is greater than the threshold.
5.Saved the final image.
![result_image](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/9023d8d2-af0a-43a6-9415-31f671823eec)


