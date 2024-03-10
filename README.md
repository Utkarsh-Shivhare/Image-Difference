# Image-Difference

Video Link:- (https://www.loom.com/share/9d912a6a98ce40869d140f04a9495913?sid=c4bd524d-1423-4e92-a3b8-0fb33b41016f)


Steps involved in finding the differnce:

1.Converting the PDF to image , Used pdf2image library of python for that.

![Differences1](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/b0ce2cd5-f8af-476a-8e85-bd9d691491ec)

![Differences2](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/c733e5cd-3d06-49e6-8718-3fa5fb32d866)

2.Resiging and processing the image to grayscale.

3.Finding the absolute difference between the images, which will give us the part of the images that are different from each other.

4.Then calculated the coutour over the image and and marked wherever the area is greater than the threshold.

5.Saved the final image.

![result_image](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/9023d8d2-af0a-43a6-9415-31f671823eec)


