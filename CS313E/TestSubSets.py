  
def main():
    #OG SUBSETS
    a=['A', 'B', 'C', 'D']
    b=[]
    def sub_sets (a, b, idx):
        if (idx == len(a)):
            print (b)
            return
        else:
            c = b[:]
            b.append(a[idx])
            sub_sets (a, b, idx + 1)
            sub_sets (a, c, idx + 1)
    #sub_sets(a, b, 0)
    print()

    #MODIFIED SUBSETS 1
    a=['A', 'B', 'C', 'D']
    b=[]
    d=[]
    def sub_sets_d (a, b, idx, d):
        
        if (idx == len(a)): 
            d.append(b)
            print (b)
            return d
        else:
            c = b[:]
            b.append(a[idx])
            sub_sets_d (a, b, idx + 1, d)
            sub_sets_d (a, c, idx + 1, d)
            return d

    e = []
    #e = sub_sets_d(a, b, 0, d)
    #print(d)
    #print(e)
    

    

    #PERMUTE
    def permute (a, idx):
        hi = len(a)
        if (idx == hi):
            print (a)
            d.append(a[:])
        else:
            for i in range (idx, hi):
                a[idx], a[i] = a[i], a[idx]
                permute(a, idx + 1)
                a[idx], a[i] = a[i], a[idx]

    a=['A', 'B', 'C']
    d = []
    permute(a, 0)
    print (d)

    # returns True if box1 fits inside box2
    def does_fit (box1, box2):
        return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])
        
    def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):

        #REACHED END OF BOX LIST; LAST COMPARISON
        # CHECK IF LAST ITEM IN BOX_LIST FITS WITH SUB_SET
        # APPEND SUB_SET TO ALL_BOX_SUBSETS
        if idx+1 == len(box_list)-1:
            if does_fit(sub_set[-1], box_list[idx+1]):
                sub_set.append(box_list[idx+1])
            all_box_subsets.append(sub_set)
            return all_box_subsets

        #IDX IS 0
        if idx == 0:
            if does_fit(box_list[idx], box_list[idx+1]):
                sub_set.append(box_list[idx])
                sub_set.append(box_list[idx+1])
            return sub_sets_boxes(box_list, sub_set, idx+1, all_box_subsets)

        #IDX IS < LEN(box_list) and > 0
        else:
            if does_fit(sub_set[-1], box_list[idx+1]):
                sub_set.append(box_list[idx+1])
            return sub_sets_boxes(box_list, sub_set, idx+1, all_box_subsets)


if __name__ == "__main__":
  main()