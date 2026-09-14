class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # check overlap
        
        # if rec2 x1 < rec1 x2 AND rec2 y1 < rec1 y2
        if (
            (
                (rec2[0] < rec1[2] and rec2[1] < rec1[3])
                # AND if rec2 x2 > rec1 x1 and rec2 y1 < rec1 y2
                and (rec2[2] > rec1[0] and rec2[1] < rec1[3])
                # rec1 y1 < rec2 y2
                and (rec1[1] < rec2[3])
            ) or (
                # if rec1 x1 < rec2 x2 AND rec1 y1 < rec2 y2
                (rec1[0] < rec2[2] and rec1[1] < rec2[3])
                # AND if rec1 x2 > rec2 x1 and rec1 y1 < rec2 y2
                and (rec1[2] > rec2[0] and rec1[1] < rec2[3])
                # rec2 y1 < rec1 y2
                and (rec2[1] < rec1[3])
            )
        ):
            # intersect = true
            return True
        else: 
            return False


        