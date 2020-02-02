# -*- coding:utf-8 -*-


class Solution(object):
    row_start,col_start,row_index, col_index=0,0,0,0
    row_end,col_end=0,0
    res_list = []
    dir = 3
    isEnd = False

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.row_end = len(matrix)-1
        self.col_end = len(matrix[0])-1

        directions={
            0:'UP',
            1:'DOWN',
            2:'LEFT',
            3:'RIGHT'
        }



        def move(dir):
            if directions.get(dir)=='RIGHT':
                self.moveRight()
                self.turnDown()
                return
            if directions.get(dir)=='DOWN':
                self.moveDown()
                self.turnLeft()
                return
            if directions.get(dir)=='LEFT':
                self.moveLeft()
                self.turnUp()
                return
            if directions.get(dir)=='UP':
                self.moveUp()
                self.turnRight()
                return
        while(not self.isEnd):
            move(self.dir)
        return self.res_list

    def moveRight(self):
        while (self.col_index <= self.col_end):
            self.res_list.append(matrix[self.row_index][self.col_index])
            self.col_index += 1
        self.col_index -= 1
        self.row_start += 1

    def moveDown(self):
        while (self.row_index <= self.row_end):
            self.res_list.append(matrix[self.row_index][self.col_index])
            self.row_index += 1

        self.row_index -= 1
        self.col_end -= 1

    def moveLeft(self):
        while (self.col_index >= self.col_start):
            self.res_list.append(matrix[self.row_index][self.col_index])
            self.col_index -= 1

        self.col_index += 1
        self.row_end -= 1

    def moveUp(self):
        while (self.row_index >= self.row_start):
            self.res_list.append(matrix[self.row_index][self.col_index])
            self.row_index -= 1

        self.row_index += 1
        self.col_start += 1

    def turnDown(self):
        self.dir = 1
        self.row_index += 1
        if self.row_index > self.row_end:
            self.isEnd = True

    def turnLeft(self):
        self.dir = 2
        self.col_index -= 1
        if self.col_index < self.col_end:
            self.isEnd = True

    def turnUp(self):
        self.dir = 0
        self.row_index -= 1
        if self.row_index < self.row_start:
            self.isEnd = True

    def turnRight(self):
        self.dir = 3
        self.col_index += 1
        if self.col_index > self.col_end:
            self.isEnd = True


if __name__ == "__main__":

    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    r = Solution().spiralOrder(matrix)
    print r




