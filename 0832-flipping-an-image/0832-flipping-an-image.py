class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] = 0 if(image[i][j]==1) else 1
            l, h = 0, len(image[i])-1
            while(l<h):
                image[i][l], image[i][h] = image[i][h], image[i][l]
                l += 1
                h -= 1
        return image