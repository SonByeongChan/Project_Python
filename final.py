from rolling_dice import Yoht_Dice

score_list = ['1.Ones','2.TWos','3.Threes', '4.Fours', '5.Fives', '6.sixes', '7.Choice', '8.Four of a kind', '9.Full House', '10.Little Straight', '11. Big Straight', '12.Yacht']
player_user = {}  # 플레이어 정보를 저장하는 dict
choice_score = {} # 플레이어가 입력한 족보를 저장하는 dict
Q = '*'*120


# 사용자로부터 플레이할 인원수를 입력받습니다.
print()
print('요트 다이스의 세계에 오신 여러분 환영합니다.!!'.center(100))
print()


# 플레이어의 인수와 닉네임을 설정하고
# 해당 플레이어의 인수 만큼 점수판 생성과 사용한 족보 리스트 생성

while True:
    
    player_num = input('플레이할 인원수를 입력해주세요(2~10): ').strip()
    
    if player_num.isdigit():        # 입력된 문자가 숫자인지 확인 합니다.
        player_num = int(player_num)    # 입력된 문자를 정수로 전환합니다.
        
        # 입력된 숫자가 2에서 10 사이인지 확인합니다.
        if 2 <= player_num <= 10:
            
            for i in range(player_num):
                print()
                name=input('이름을 적어주세요')
            
                player_user[f'{name}_player{i+1}'] = {'1.one':0, '2.two':0, '3.three':0, '4.four':0, 
                                                      '5.five':0, '6.six':0, '7.choice':0, '8.Four of a kind':0, 
                                                      '9.Full House':0, '10.Little Straight':0, '11.Big Straight':0, '12.Yacht':0}
                                                      # 각 플레이어에게 점수판 dict 생성
                choice_score[f'{name}_player{i+1}'] = [] # 족보 중복 입력 방지 확인을 위한 list
            # print(f'player 여러분 재미있게 즐겨주세요.'.center(100))
            break
        
        else:
            print('2 ~ 10 사이의 숫자를 입력해주세요')  # 숫자가 범위를 벗어났을 때의 에러 메시지
    else:
        print('숫자만을 입력해주세요')  # 입력값이 숫자가 아닐 때의 에러 메시지

    
# 게임 실행 코드 
# 게임의 라운드는 총 13회 동안 입력받은 PLayer들이 게임을 진행하게 함

Round = 1

while Round < 13:
    
    print(f'{Round}Round.'.center(100))     # 현재 라운드 출력력
    for i in range(len(player_user)):
        
        print()
        print(f'{list(player_user)[i]}'.center(100))
        print(f'{list(player_user)[i]}님의 현재 점수 : {sum(player_user[list(player_user)[i]].values())}점')
        print()
        print(Q,'\t\t\t\t\t!제공되는 족보!','1.one\t\t2.two\t\t\t3.three\t\t4.four\t\t\t5.five\t\t\t6.six\n7.choice\t8Four of a kind\t\t9.Full House\t10.Little Straight\t11. Big Straight\t12.Yacht',Q,sep='\n')
        print()
        print(f'{list(player_user)[i]}님이 현재까지 사용하신 족보 입니다. : {choice_score[list(player_user)[i]]}')  # 해당유저의 현재 족보를 보여 줍니다.
                
        a, b, c = Yoht_Dice(choice_score[list(player_user)[i]])
        player_user[list(player_user)[i]][a] = b   # 해당 플레이어의 점수판에서 족보의 키값을 찾아 점수를 등록함함
        choice_score[list(player_user)[i]].append(c) # 플레이가 선택한 족보의 번호가 추가됨 

    Round += 1

# 점수 및 등수 계산 

player_total_score = {} # 플레이어 들의 최종 스코어를 계산함 

for player_name in player_user.keys():
    total_score = sum(player_user[player_name].values())
    player_total_score[player_name] = total_score
    print(f"{player_name}: {total_score}")

# 점수 기준으로 정렬하여 등수 매기기
sorted_players = []
for player in player_total_score:
    sorted_players.append((player, player_total_score[player]))

# 점수 내림차순 정렬
for i in range(len(sorted_players)):
    for j in range(i + 1, len(sorted_players)):
        if sorted_players[i][1] < sorted_players[j][1]:  # 점수 비교
            sorted_players[i], sorted_players[j] = sorted_players[j], sorted_players[i]  # Swap

# 등수 출력 (동점 처리)
print("!플레이어 순위!")
rank = 1
previous_score = 0
previous_rank = 0

for i in range(len(sorted_players)):
    player_name = sorted_players[i][0]
    score = sorted_players[i][1]
    
    if score == previous_score:
        # 이전 점수와 같으면 이전 랭크를 사용
        print(f"{previous_rank}위: {player_name} - 점수: {score}점")
    else:
        # 새로운 점수면 랭크 갱신
        print(f"{rank}위: {player_name} - 점수: {score}")
        previous_rank = rank  # 현재 랭크 저장
    
    previous_score = score  # 현재 점수 저장
    rank += 1  # 다음 랭크로 이동