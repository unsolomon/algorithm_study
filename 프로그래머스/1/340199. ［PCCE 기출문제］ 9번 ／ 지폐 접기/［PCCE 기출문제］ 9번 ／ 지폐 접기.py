def solution(wallet, bill):
    def fold(bill,wallet):
        couint = 0
        bw, bh = bill
        ww, wh = wallet
        
        while True:
            if (bw <= ww and bh <= wh) or (bh <=ww and bw <= wh):
                break
                
            if bw > bh:
                    bw //= 2
            else:
                    bh //= 2

            couint += 1
        return couint
    
    return fold(bill, wallet)
    
    
    
