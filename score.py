def result_score(score_choice,rolling_dice_result):
    '''
    Player가 입력한 족보 번호에 따른 점수 계산
    ''' 

    while True:
        if score_choice == '1':                                         # 1. one
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]
            
            key = "1.one"
            score = rolling_dice_result_str.count('1') * 1 
            
            return key, score

        elif score_choice == '2':                                         # 2. two
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]
            
            key = "2.two"
            score = rolling_dice_result_str.count('2') * 2
            
            return key, score        

        elif score_choice == '3':                                         # 3. three
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]
            
            key = "3.three"
            score = rolling_dice_result_str.count('3') * 3 
            
            return key, score

        elif score_choice == '4':                                         # 4. four
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]

            key = "4.four"
            score = rolling_dice_result_str.count('4') * 4 
            
            return key, score        

        elif score_choice == '5':                                         # 5.five
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]
            
            key = "5.five"
            score = rolling_dice_result_str.count('5') * 5 
            
            return key, score
            
        elif score_choice == '6':                                         # 6. six
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]
    
            key = "6.six"
            score = rolling_dice_result_str.count('6') * 6 
            
            return key, score

        elif score_choice == '7':                                         # 7. choice
            
            key = "7.choice"
            score = sum(rolling_dice_result)        

            return key, score  

        elif score_choice == '8':                                         # 8.Four of a Kind
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]
            
            for i in range(6):                                          
                if rolling_dice_result_str.count(f'{i+1}') == 4:
                    score = rolling_dice_result[i] * 4
                else:
                    score = 0
                    
            key = '8.Four of a Kind'    
            
            return key, score
        
        elif score_choice == '9':                                         # 9. Full Hous
            full_house = {}
            for i in rolling_dice_result:
                if i in full_house:
                    full_house[i] += 1
                else:
                    full_house[i] = 1
            
            if sorted(full_house.values()) == [2,3]:
                score = sum(rolling_dice_result)
            else:
                score = 0
            
            key = '9.Full Hous'
            
            return key, score
            
        elif score_choice == '10':                                         # 10. Little Straight
            sorted_rolling_dice_result = sorted(rolling_dice_result)
            
            if sorted_rolling_dice_result[0] == 1 and sorted_rolling_dice_result[1] == 2 and sorted_rolling_dice_result[2] == 3 and sorted_rolling_dice_result[3] == 4 and sorted_rolling_dice_result[4] == 5:
                score = 30
            else:
                score = 0

            key = '10.Little Straight'
            
            return key, score

        elif score_choice == '11':                                         # 11. Big Straight
            sorted_rolling_dice_result = sorted(rolling_dice_result)
            if sorted_rolling_dice_result[0] == 2 and sorted_rolling_dice_result[1] == 3 and sorted_rolling_dice_result[2] == 4 and sorted_rolling_dice_result[3] == 5 and sorted_rolling_dice_result[4] == 6:
                score = 30 
            else:
                score = 0
                
            key = '11.Big Straight'
            
            return key, score
            
        elif score_choice == '12':                                         # 12. Yacht
            rolling_dice_result_str = [str(i) for i in rolling_dice_result]
            
            for i in range(6):
                if rolling_dice_result_str.count(f'{i+1}') == 5:
                    score = 50
                else:
                    score = 0    
                    
            key = '12.Yacht'
            
            return key, score                
        else:
            print('다시입력')