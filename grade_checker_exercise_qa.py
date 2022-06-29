def grades(hw_score, ass_score, fin_score):
    max_hw_score = 25
    max_ass_score = 50
    max_fin_score = 100
    
    max_total = max_hw_score + max_ass_score + max_fin_score
    user_total = hw_score + ass_score + fin_score

    if (hw_score > max_hw_score) or (ass_score > max_ass_score) or (fin_score > max_fin_score):
        return "Not Allowed"
    else:
        return round(100 * user_total / max_total, 1)
    
print(grades(25, 50, 100))
        
        
        
    
