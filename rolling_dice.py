import random as r
from score import result_score 
from dice_check import dice_chek

def Yoht_Dice(choice_score):
    '''
    요트다이스의 룰에 맞추어 회차를 진행해 주는 코드
    '''
    rolling_dice = []           # 1회차에서 받은 주사위 눈
    rolling_dice_sec = []       # 2회차에서 받은 주사위 눈
    rolling_dice_thrd = []      # 3회차에서 받은 주사위 눈
    rolling_dice_result = []    # 최종적으로 player가 선택한 주사위 눈

    for dice in range(5):       # 1회차의 주사위 눈 5개를 추출하기 위한 반복문문
        rolling_dice.append(r.randint(1,6))

    print()
    print(f'1회차에서 나온 주사위의 눈 입니다'.center(100))
    print(f'{rolling_dice}'.center(100)) # 뽑은 주사위의 눈을 보여줌
    print()
 
    # 1회차에 주사위를 족보에 등록할것인가 아닌가
    while True:
        print('주사위 숫자가 마음에 드시나요??'.center(100))
        print()
        print('y: 마음에 들어 족보에 등록할것이다.'.center(100))
        print('n: 마음에 들지 않아 다시 굴릴것이다.'.center(100))
        choice = input('입력:'.center(100)).lower()
        print()

        if choice =='y':               # 1회차의 주사위 눈을 바로 족보에 등록함
            rolling_dice_result.extend(rolling_dice)    # 플레이어가 볼 최종 스코어에 1회차 주사위 결과를 등록함
            
            while True:
                result = input('점수를 입력하실 족보를 선택해주세요')   # result 점수를 저장할 족보 번호
                if result.isdigit():    # 입력반은 문자열이 숫자만 있는 것인지 확인
                    if 1<= int(result) < 13:        # 족보의 번호에 해당하는 숫자인지 확인 
                        if result in choice_score:  # choice_score : 해당 플레이어에게 등록된 족보 목록 // 값이 중복 되는지 확인
                            print('이미 입력된 족보입니다. 다시 선택해주세요')
                            continue    # 이미 입력된 경우 선택되지 않는 족보를 선택하기 전까지 계속 실행 되게 함함
                        else:
                            # 조건에 아무 이상이 없을 경우
                            # 입력된 족보에 따른 점수를 계산하여 결과를 반환함
                            # result : 선택한 족보 번호 
                            # choice_key : 선택한 족보 번호와 이름
                            # roeund_score : 해당 족보에 해당하는 점수
                            choice_key, roeund_score = result_score(result,rolling_dice_result)
                    
                            return choice_key, roeund_score, result     
                    else:
                        print('족보에 있는 숫자만을 입력해주세요')               
                else:
                    print('숫자만을 입력해주세요')
        # 다음 회차의 주사위를 다시 돌릴 시    
        # 해당 반복문을 부수고 다음으로 넘어감
        elif choice =='n':
            break
        
        # 입력값 오류시 다시 입력할 수 있게끔 함
        else:
            print('y와 n 둘 중 하나만을 입력해주세요')
            print()


    # 1회차에서 뽑은 주사위의 눈 중 지울 주사위를 선택함
    while True:
        remove_dice = input(f'''{rolling_dice}에서 지우고 싶은 숫자를 입력하시오 예)2,3,1>>''').strip().split(',')  

        # 2회차 주사위

        if all([remove_dice[i].isdigit() for i in range(len(remove_dice))]) == True:                # remove_dice의 요소가 숫자인지 아닌지 판별
            if all([int(remove_dice[i]) in rolling_dice for i in range(len(remove_dice))]) == True: # remove_dice의 요소가 rolling_dice(1회차 받은 주사위 눈)에 있는지 판별
                if dice_chek(rolling_dice, remove_dice) != True:                                    # remove_dice의 요소가 rolling_dice의 요소의 갯수 만큼 들어 있나 확인
                    print(f'해당 {remove_dice} 숫자를 다시 돌립니다.')       # 위 조건에 문제가 없을 시 제거를 선택한 주사위의 눈을 보여 주고 안내 문구 출력
                    print()
                    
                    for dice_sec in range(len(remove_dice)):                # 제거하고자 한 주사위의 수 만큼 새로운 주사위를 뽑는다
                        remove_dice[dice_sec] = int(remove_dice[dice_sec])   #  => 숫자임을 확인하고 int로 바꾸어야함
                        rolling_dice.remove(remove_dice[dice_sec])      # rolling_dice에 있는 값 중  remove_dice 있는 값들을 제거한다.
                        rolling_dice_sec.append(r.randint(1,6))         # rolling_dice_sec에 없어진 만큼의 새로운 주사위 눈을 추가한다.
                    
                    # 2회차에 추출된 값을 보여줌
                    print( f'\t{len(remove_dice)}개를 다시 돌린 후 나온 값\n\t\t{rolling_dice_sec}\n\t1회차 주사위 값\n\t\t{rolling_dice}') 
                    break
                else:
                    print('1회차의 주사위 눈만 입력해주십시오')
                    continue
            else:
                print('1회차의 주사위 눈만 입력해주십시오')
                continue                            
        else:
            print('숫자만 입력홰주십시오')

    # 2회차에 주사위를 족보에 등록할것인가 아닌가
    while True:
        print('주사위 숫자가 마음에 드시나요??'.center(100))
        print()
        print('y: 마음에 들어 족보에 등록할것이다.'.center(100))
        print('n: 마음에 들지 않아 다시 굴릴것이다.'.center(100))
        choice = input('입력:'.center(100)).lower()
        print()

        if choice =='y':
            rolling_dice_result.extend(rolling_dice)            # 1회차에서 'n'을 할 시 rolling_dice_result에 저장되지 않기 때문에 2회차에서 저장
            rolling_dice_result.extend(rolling_dice_sec)        # 2회차에서 새롭게 나온 주사위의 눈을 rolling_dice_result에 추가
            while True:
                print()
                result_sec = input('점수를 입력하실 족보를 선택해주세요')   # 점수를 등록할 족보의 번호 입력
                if result_sec.isdigit():                                 # 입력 받은 족보의 문자열이 숫자인지 확인
                    if 1 <= int(result_sec) < 13:                        # 족보에 해당되는 숫자인지 확인 
                        if result_sec in choice_score:                   # result_sec가 이미 입력된 족보인지 아닌지 확인 
                            print('이미 입력된 족보입니다. 다시 입력해주세요')
                            continue
                        else:     
                            # 조건에 아무 이상이 없을 경우
                            # 입력된 족보에 따른 점수를 계산하여 결과를 반환함
                            # result_sec : 선택한 족보 번호 
                            # choice_key : 선택한 족보 번호와 이름
                            # roeund_score : 해당 족보에 해당하는 점수                            
                            choice_key, roeund_score = result_score(result_sec,rolling_dice_result) # 입력 받은 족보에 의하여 점수를 계산하여 반환 
                            
                            return choice_key, roeund_score, result_sec
                    else:
                        print()
                        print('족보에 있는 숫자만을 입력해주세요')               
                else:
                  print()
                  print('숫자만을 입력해주세요')

        elif choice =='n':
            break
        else:
            print()
            print('y와 n 둘 중 하나만을 입력해주세요')
            
    while True:
        
        # 2회차에 뽑은 눈만을 가지고 다시 뽑기기
        remove_dice_sec = input(f'{rolling_dice_sec}에서 지우고 싶은 숫자를 입력하시오 예)2,3,1>>').strip().split(',')
        
        # 3회차
        
        if all([remove_dice_sec[i].isdigit() for i in range(len(remove_dice_sec))]) == True:        # remove_dice_sec의 요소가 숫자인지 아닌지 판별
            if all([int(remove_dice_sec[i]) in rolling_dice_sec for i in range(len(remove_dice_sec))]) == True:   # remove_dice_sec의 요소가 rolling_dice_sec(1회차 받은 주사위 눈)에 있는지 판별
                if dice_chek(rolling_dice_sec, remove_dice_sec) != True:        # remove_dice_sec의 요소가 rolling_dice_sec의 요소의 갯수 만큼 들어 있나 확인
                    print(f'해당 {remove_dice_sec} 숫자를 다시 돌립니다.')
                    print()
                    for dice_thrd in range(len(remove_dice_sec)):       # 제거하고자 한 주사위의 수 만큼 새로운 주사위를 뽑는다
                        remove_dice_sec[dice_thrd] = int(remove_dice_sec[dice_thrd])        # => 숫자임이 확인 되었으므로 int로 바꾸어야함
                        rolling_dice_sec.remove(remove_dice_sec[dice_thrd])     # rolling_dice_sec에 있는 값 중  remove_dice_sec 있는 값들을 제거한다.
                        rolling_dice_thrd.append(r.randint(1,6))                # rolling_dice_thrd에 들어갈 새로운 값 생성성
                    print()
                    print(f'{len(remove_dice_sec)}개를 다시 돌린 후 나온 값\n\t{rolling_dice_thrd}\n\t1회차 주사위 값\n\t\t{rolling_dice}\n\2회차 주사위 값\n\t\t{rolling_dice_sec}')
                    break
                else:
                    print('2회차의 주사위 눈만 입력해주십시오')
                    continue
            else:
                print('2회차의 주사위 눈만 입력해주십시오')
                continue                            
        else:
            print('숫자만 입력홰주십시오')
        
    rolling_dice_result.extend(rolling_dice)            # 1회차 주사위의 눈을 최종 결과값에 입력
    rolling_dice_result.extend(rolling_dice_sec)        # 2회차 주사위의 눈을 최종 결과값에 입력
    rolling_dice_result.extend(rolling_dice_thrd)       # 3회차 주사위의 눈을 최종 결과값에 입력
    
    while True:
        print()
        result_thrd = input('점수를 입력하실 족보를 선택해주세요')
        if result_thrd.isdigit():         # 입력 받은 족보의 문자열이 숫자인지 확인
            if 1<= int(result_thrd) < 13:    # 족보에 해당되는 숫자인지 확인
                if result_thrd in choice_score:  # result_sec가 이미 입력된 족보인지 아닌지 확인 
                    print()
                    print('이미 입력된 족보입니다. 다시 선택해주세요')
                    continue
                else:
                    # 조건에 아무 이상이 없을 경우
                    # 입력된 족보에 따른 점수를 계산하여 결과를 반환함
                    # result_thrd : 선택한 족보 번호 
                    # choice_key : 선택한 족보 번호와 이름
                    # roeund_score : 해당 족보에 해당하는 점수     
                
                    choice_key, roeund_score = result_score(result_thrd,rolling_dice_result)
            
                    return choice_key, roeund_score, result_thrd     
            else:
                print()
                print('족보에 있는 숫자만을 입력해주세요')               
        else:
            print()
            print('숫자만을 입력해주세요')