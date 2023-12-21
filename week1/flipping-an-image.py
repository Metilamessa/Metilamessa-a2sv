class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            img.reverse()
        for img in image:
            for i in range(len(img)):
                if img[i] == 0:
                    img[i] = 1
                else:
                    img[i] = 0
        return image
        