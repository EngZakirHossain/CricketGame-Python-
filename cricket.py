import random
import time

good_possible_list = [0, 1, 2, 3, 4, 6, 'w', 1, 2, 4, 6, 4, 3]
possible_list = [0, 1, 2, 'w', 3, 4, 6, 'w', 1, 2, 4, 'w']
possible_list_bangladesh = [0, 1, 2, 3, 4, 6, 'w', 1, 2, 4]
possible_list_india = [0, 1, 2, 3, 4, 6, 'w', 2, 4, 4]
possible_list_pakistan = [0, 1, 2, 3, 4, 6, 'w', 1, 2, 4, 6]
possible_list_srilanka = [0, 1, 2, 3, 4, 6, 'w', 1, 2, 4, 6, 4]

good_weather='the peach is good for bat first.....'
bad_weather='the peach is good for field first.....'

def team_ferpormance_second(team1,possible_list):
    if team1=='bangladesh':
        if condition_peach==bad_weather:
            possible_list=good_possible_list
        elif condition_peach==good_weather:
            possible_list=possible_list_bangladesh

    elif team1=='india':
        if condition_peach==bad_weather:
            possible_list=good_possible_list
        elif condition_peach==good_weather:
            possible_list=possible_list_india
    elif team1=='pakistan':
        if condition_peach==bad_weather:
            possible_list=good_possible_list
        elif condition_peach==good_weather:
            possible_list=possible_list_pakistan
    elif team1=='srilanka':
        if condition_peach==bad_weather:
            possible_list=good_possible_list
        elif condition_peach==good_weather:
            possible_list=possible_list_srilanka
    return possible_list

def team_ferpormance_first(team1,possible_list):
    if team1=='bangladesh':
        if condition_peach==bad_weather:
            possible_list=possible_list_bangladesh
        elif condition_peach==good_weather:
            possible_list=good_possible_list

    elif team1=='india':
        if condition_peach==bad_weather:
            possible_list=possible_list_india
        elif condition_peach==good_weather:
            possible_list=good_possible_list
    elif team1=='pakistan':
        if condition_peach==bad_weather:
            possible_list=possible_list_pakistan
        elif condition_peach==good_weather:
            possible_list=good_possible_list
    elif team1=='srilanka':
        if condition_peach==bad_weather:
            possible_list=possible_list_srilanka
        elif condition_peach==good_weather:
            possible_list=good_possible_list
    return possible_list



def peach_condition(good_weather,bad_weather):
    return random.choice([good_weather,bad_weather])

def toss(team1, team2):
    return random.choice([team1, team2])

def my_choice(team1,team2):
    choose=input().lower()
    if choose == 'bat':
        return  team1
    if choose == 'ball':
        return  team2
    return

def com_choice(team1, team2):
    condition=condition_peach
    if condition==good_weather:
        return team2
    else:
        return team1


def team_sri():
    print('Your team players are....')
    print('1. Angelo Mathews.(Bat)')
    print('2. Upul Tharanga.(Bat)')
    print('3. Dinesh Chandimal.(Bat)')
    print('4. Niroshan Dickwella.(Bat)')
    print('5. Nuwan Pradeep.(ALL)')
    print('6. Asela Gunaratne.(WC)')
    print('7. Suranga Lakmal.(Ball)')
    print('8. Nuwan Kulasekara.(ball)')
    print('9. Lasith Malinga.(Ball)')
    print('10. Thisara Perera (C)')
    print('11. Kusal Perera.(Ball)')
    return
def team_ban():
    print('Your team players are....')
    print('1. Tamim Iqbal.(Bat)')
    print('2. Imrul Kayes.(Bat)')
    print('3. Mushfiqur Rahim.(WC)')
    print('4. Soumya Sarkar.(Bat)')
    print('5. Shakib Al Hasan.(ALL)')
    print('6. Mahmudullah.(ALL)')
    print('7. Mashrafe Mortaza.(C)')
    print('8. Mosaddek Hossain.(ALL)')
    print('9. Mehidy Hasan.(Ball)')
    print('10. Rubel Hossain.(Ball)')
    print('11. Mustafizur Rahman,(Ball)')
    return
def team_ind():
    print('Your team players are....')
    print('1. Virat Kohli.(Bat)')
    print('2. Shikhar Dhawan.(Bat)')
    print('3. Rohit Sharma.(Bat)')
    print('4. Ajinkya Rahane.(Bat)')
    print('5. Yuvraj Singh.(ALL)')
    print('6. Dinesh Karthik.(WC)')
    print('7. Umesh Yadav.(Ball)')
    print('8. Hardik Pandya.(ball)')
    print('9. Kedar Jadhav.(Ball)')
    print('10. Manish Pandey. (C)')
    print('11. Jasprit Bumrah.(Ball)')
    return
def team_pak():
    print('Your team players are....')
    print('1. Ahmed Shehzad.(Bat)')
    print('2. Mohammad Hafeez.(Bat)')
    print('3. Imad Wasim.(WC)')
    print('4. Umar Akmal.(Bat)')
    print('5. Shoaib Malik.(ALL)')
    print('6. Shadab Khan.(ALL)')
    print('7. Sarfraz Ahmed.(C)')
    print('8. Fakhar Zaman.(ALL)')
    print('9. Hasan Ali.(Ball)')
    print('10. Haris Sohail.(Ball)')
    print('11. Ahmed Shehzad.(Ball)')
    return

def select_my_team():

    select_your_team=input('Select your team: '.lower())
    # country1=select_your_team
    if select_your_team == 'srilanka':
        team_sri()
    elif select_your_team == 'bangladesh':
        team_ban()
    elif select_your_team == 'india':
        team_ind()
    elif select_your_team == 'pakistan':
        team_pak()
    else:
        print('Invalid Team name!!!')
        select_my_team()
    return select_your_team

def select_com_team():

    select_opponent_team=input('Select opponent team: ')
    if select_opponent_team == 'srilanka':
        team_sri()
    elif select_opponent_team == 'bangladesh':
        team_ban()
    elif select_opponent_team == 'india':
        team_ind()
    elif select_opponent_team == 'pakistan':
        team_pak()
    else:
        print('Invalid Team name!!!')
        select_com_team()
    return select_opponent_team

def cricket_game(country='Bangladesh', overs=1, wickets=10, possible_activity=possible_list,runs_team1=1000,runs_team2=1000):
    runs = 0
    wickets = 0
    for i in range(6*overs):
        time.sleep(1)
        run_per_ball = random.choice(possible_activity)
        print('Ball', str(i+1) + ':', run_per_ball)
        if run_per_ball not in [0, 'w']:
            runs += run_per_ball
        if run_per_ball == 'w':
            wickets += 1
        if runs > runs_team1:
            print(country + ':', runs ,'/' ,wickets)
            break
        if runs > runs_team2:
            print(country + ':', runs ,'/' ,wickets)
            break
        print(country + ':', runs ,'/' ,wickets)
    return country, runs, wickets


def play_cricket(team1, team2,play_over=1):
    toss_winner = toss(team1, team2)
    print(toss_winner, 'win the toss!!!')
    if toss_winner == team1:
        print('What you want to choose? (Bat/Ball): ')
        first_bat=my_choice(team1,team2)
    elif toss_winner == team2:
        first_bat=com_choice(team1, team2)
    over = play_over
    score=0
    wicket=10
    wicket_left=0
    win_wicket=0
    if first_bat == team1:
        print(team1, 'batting...')
        score_team1 = cricket_game(country=team1, overs=over)
        print(team2, 'batting...')
        new_possible_list=team_ferpormance_second(team1,possible_list)
        score_team2 = cricket_game(runs_team1=score_team1[1],country=team2, overs=over, possible_activity=new_possible_list)
        wicket_left=wicket - score_team2[2]
    else:
        print(team2, 'batting...')
        new_possible_list=team_ferpormance_first(team1,possible_list)
        score_team2 = cricket_game(country=team2, overs=over, possible_activity=new_possible_list)
        print()
        print(team1, 'batting...')
        score_team1 = cricket_game(runs_team2=score_team2[1],country=team1, overs=over)
        wicket_left=wicket - score_team1[2]
    print()
    if first_bat == team1:
        if score_team1[1] == score_team2[1]:
            print('Match Draw')
            print('Play super over!!!')
            super_over=1
            play_cricket(team1,team2,play_over=super_over)
        elif score_team1[1] > score_team2[1]:
            score= score_team1[1] - score_team2[1]
            print(team1, 'winner by ',score,'Runs')
        else:
            print(team2, 'winner by ',wicket_left,'wicket')
    else:
        if score_team1[1] == score_team2[1]:
            print('Match Draw')
            print('Play super over!!!')
            super_over=1
            play_cricket(team1,team2,play_over=super_over)
        elif score_team2[1] > score_team1[1]:
            score= score_team2[1] - score_team1[1]
            print(team2, 'winner by ',score,'Runs')
        else:
            print(team1, 'winner by ',wicket_left,'wicket')

print('Welcome to Asia cup 2018....')
print('Teams are....')
print('Srilanka, Bangladesh, India, Pakistan')
select_team1=select_my_team()
select_team2=select_com_team()
req_over=int(input('How many over you want to play: '))
condition_peach=peach_condition(good_weather,bad_weather)
print(condition_peach)
play_cricket(team1=select_team1,team2=select_team2,play_over=req_over)





