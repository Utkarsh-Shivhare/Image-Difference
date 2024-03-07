# Image-Difference

Steps involved in finding the differnce:
1.Converting the PDF to image , Used pdf2image library of python for that.
![Differences1](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/1ecee659-3c85-4569-a6d1-c11da1707d97)
![Differences2](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/d29a0497-6e1b-4689-a841-f46e907ed3cf)
2.Resiging and processing the image to grayscale.
3.Finding the absolute difference between the images, which will give us the part of the images that are different from each other.
4.Then calculated the coutour our the image and and marked wherever the area is greater than the threshold.
5.Saved the final image.
![result_image](https://github.com/Utkarsh-Shivhare/Image-Difference/assets/109977467/9023d8d2-af0a-43a6-9415-31f671823eec)


