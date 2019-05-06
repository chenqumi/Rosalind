from LinearStruc import Queue


class rabbit(object):
    """docstring for rabbit"""
    def __init__(self, maturity=0, survival_month=1):
        self.maturity = maturity
        self.survival_month = survival_month

    def is_mature(self):
        return self.maturity == 1

    def add_month(self):
        self.survival_month += 1
        self.maturity = 1


class rabbit2(object):
    """docstring for rabbit2"""
    def __init__(self, maturity, survival_month):
        self.maturity = maturity
        self.survival_month = survival_month
        self.leftchild = None
        self.rightchild = None

    def insert_left(self, maturity, survival_month):
        subtree = rabbit2(maturity, survival_month)
        if self.leftchild == None:
            self.leftchild = subtree
        else:
            subtree.leftchild = self.leftchild
            self.leftchild = subtree

    def insert_right(self, maturity, survival_month):
        subtree = rabbit2(maturity, survival_month)
        if self.rightchild == None:
            self.rightchild = subtree
        else:
            subtree.rightchild = self.rightchild
            self.rightchild = subtree

    # def set_maturity(self, maturity_):
    #     self.maturity = maturity_

    # def set_month(self, month_):
    #     self.month = month_



def FIBD(n, m):
    """
    mature set to leftchild, baby set to rightchild
    """
    r = rabbit2(0, 1)
    q = Queue()
    q.enQ(r)
    # current_tree = r
    for i in range(2, n+1):
        while q.size() > 0:
            current_tree = q.deQ()
            # baby rabbit
            if current_tree.maturity == 0:
                month = current_tree.survival_month + 1
                current_tree.insert_left(1, month)

                q.enQ(current_tree.leftchild)
                # current_tree = current_tree.leftchild
            # mature rabbit
            else:
                # survival_month is max, produce a baby
                if current_tree.survival_month == m:
                    current_tree.insert_right(0, 1)

                    q.enQ(current_tree.rightchild)
                    # current_tree = current_tree.rightchild
                
                # continue grow, and produce a baby
                else:
                    month = current_tree.survival_month + 1
                    current_tree.insert_left(1, month)
                    current_tree.insert_right(0, 1)

                    q.enQ(current_tree.leftchild)
                    q.enQ(current_tree.rightchild)
