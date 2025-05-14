def dice_chek(dice_01, return_01):

    '''
    제거하고자 하는 주사위 눈의 갯수와 기존에 있던 주사위 눈의 갯수를 확인 해주는 함수
    '''

    # dice_01       # 기존에 있던 주사위 눈 (1회차, 2회차, 3회차)
    # return_01     # 새롭게 받은 주사위 눈 (1회차 제거 주사위 눈, 2회차 제거 주사위 눈)

    dice_01_dict ={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}  # 기존에 있던 주사위 눈 저장
    return_01_dict = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0} # 새로 입력 받은 주사위 눈 저장

    # 기존에 있던 주사위 눈이 갯수를 해아림
    for i in dice_01:
        if str(i) in dice_01_dict:
            dice_01_dict[str(i)] += 1

    # 새롭게 받은 주사위 눈의 갯수를 해아림
    for i in return_01:
        if i in return_01_dict:
            return_01_dict[i] += 1
    # 기존 주사위 갯수와 새롭게 받은 주사위 갯수를 비교함
    # 기존에 가지고 있는 주사위의 숫자가 당연 커야함함
    for i in range(6):
        if list(dice_01_dict.values())[i] < list(return_01_dict.values())[i]:            
            return True
        
    return False 