def countBalls(lowLimit,highLimit):

    ball_count ={}

    if lowLimit < 0 or highLimit < 0:
        return 0
    for ball_number in range(lowLimit,highLimit+1):
        total = 0

        for box_number in str(ball_number):
            total +=str(box_number)

            if total not in ball_count:
                ball_count[total] =0

            ball_count[total] +=1

    
    return max([ball_count[key] for key in ball_count])

