import Queue

aut_win_counts = 0
dec_win_counts = 0
battle_count = 0

dec = {}
aut = {}

#Team Autobot
A_transformer = {1:'Bluestreak', 2 :'Brainstorm' , 3 :'Hubcap',4:'Metroplex', 5:'Optimus Prime', 6:'Repugnus', 7:'Wheeljack'}
        
#Team Decepticon
D_transformer = {8:'Galvatron' , 9: 'Megatron' , 10:'Predaking', 11:'Shrapnel', 12:'Soundwave',13:'Vortex'}

#Assumption 1 : Predefined Overall Rating for Decepticons
dec['Galvatron'] = {'Strength': 10, 'Intelligence': 6 ,'Speed': 7, 'Endurance': 4, 'Rank': 1, 'Courage': 6, 'Firepower': 7, 'Skill': 8}
dec['Megatron'] = {'Strength': 7, 'Intelligence': 7 ,'Speed': 8, 'Endurance': 6, 'Rank': 2, 'Courage': 8, 'Firepower': 6, 'Skill': 7}
dec['Predaking'] = {'Strength': 8, 'Intelligence': 9 ,'Speed': 9, 'Endurance': 9, 'Rank': 3, 'Courage': 9, 'Firepower': 4, 'Skill': 3}
dec['Shrapnel'] = {'Strength': 6, 'Intelligence': 7 ,'Speed': 6, 'Endurance': 9, 'Rank': 4, 'Courage': 6, 'Firepower': 7, 'Skill': 4}
dec['Soundwave'] = {'Strength': 4, 'Intelligence': 8 ,'Speed': 8, 'Endurance': 6, 'Rank': 5, 'Courage': 5, 'Firepower': 8, 'Skill': 6}
dec['Vortex'] = {'Strength': 9, 'Intelligence': 10 , 'Speed': 7, 'Endurance': 8, 'Rank': 6, 'Courage': 8, 'Firepower': 5, 'Skill': 5}


#Assumption 1 : Predefined Overall Rating for Autobots
aut['Bluestreak'] = {'Strength': 3, 'Intelligence': 5 ,'Speed': 8, 'Endurance': 10, 'Rank': 1, 'Courage': 8, 'Firepower': 7, 'Skill': 8}
aut['Brainstorm'] = {'Strength': 10, 'Intelligence': 3 ,'Speed': 3, 'Endurance': 4, 'Rank': 2, 'Courage': 6, 'Firepower': 9, 'Skill': 9}
aut['Hubcap'] = {'Strength': 8, 'Intelligence': 5 ,'Speed': 6, 'Endurance': 9, 'Rank': 3, 'Courage': 7, 'Firepower': 8, 'Skill': 7}
aut['Metroplex'] = {'Strength': 5, 'Intelligence': 8 ,'Speed': 7, 'Endurance': 9, 'Rank': 4, 'Courage': 6, 'Firepower': 4, 'Skill': 8}
aut['Optimus_Prime'] = {'Strength': 7, 'Intelligence': 8 ,'Speed': 8, 'Endurance': 9, 'Rank': 5, 'Courage': 9, 'Firepower': 8, 'Skill': 8}
aut['Repugnus'] = {'Strength': 7, 'Intelligence': 7 ,'Speed': 4, 'Endurance': 7, 'Rank': 6, 'Courage': 7, 'Firepower': 3, 'Skill': 7}
aut['Wheeljack'] = {'Strength': 9, 'Intelligence': 2 ,'Speed': 2, 'Endurance': 6, 'Rank': 7, 'Courage': 8, 'Firepower': 6, 'Skill': 6}

# sort them by rank
sorted_dec = sorted(dec.items(), key=lambda x: x[1]['Rank'])
sorted_aut = sorted(aut.items(), key=lambda x: x[1]['Rank'])

#print sorted_dec
#print sorted_aut

# put them in queue (FIFO)
aq = Queue.Queue()
dq = Queue.Queue()

for item in sorted_aut:
    aq.put(item)

for item in sorted_dec:
    dq.put(item)

#Enter number for Player 1 for Autobots : Select from 1-7 number for Autobots : 
#Bluestreak :1,   2 :'Brainstorm' , 3 :'Hubcap',4:'Metroplex', 5:'Optimus Prime', 6:'Repugnus', 7:'Wheeljack'
max_battles= 2^11+2

for i in range (0, max_battles):
    
    user_1= input("Enter the Name of the Transformer 1 : ")
    if user_1 is 5:
        print "Winner is Autobots : Optimus Prime"
    else:
        name_list=[]
        for key, value in A_transformer.items():
            name_list.append(key)
        if user_1 in name_list:
            print "The Autobot transformer is"
            print A_transformer[user_1]
                
        selected_transformer={}
        selected_transformer[A_transformer[user_1]] =user_1

    #Enter number for Player 2 for Decepticon : Select from 8-13 number for Decepticon
    #'Galvatron': 8 , 'Megatron':9 , 'Predaking':10, 'Shrapnel':11, 'Soundwave':12 ,'Vortex':13
        
    user_2= input("Enter the Name of the Transformer 2 : ")
    if user_2 is 10:                                          #if user enters 10 for Pedaking, winner automatically is Predaking
        print "Winner is Decepticons : Predaking"
    else:
        name_list1=[]                                                  #creates another list to store selected players
        for key, value in D_transformer.items():
            name_list1.append(key)
        if user_2 in name_list1:
            print "Decepticon transformer is"
            print D_transformer[user_2]
                
        selected_transformer2={}
        selected_transformer2[D_transformer[user_2]] = user_2



                
         #finding the sum of overall ratings for both Autobots and Decepticons
        dict_sum_dec = {"Galvatron":[10,6,7,4,1,6,7,8],"Megatron" : [7,7,8,6,2,8,6,7],
                "Predaking" : [8,9,9,9,3,9,4,3], "Shrapnel": [6,7,6,9,4,6,7,4],
                "Soundwave":[4,8,8,6,5,5,8,6],"Vortex":[9,10,7,8,6,8,5,5]}
        result_sum_dec ={}
        for k,v in dict_sum_dec.items():
            result_sum_dec[k]=sum(v)

        
        
        dict_sum_aut = {"Bluestreak":[3,5,8,10,1,8,7,8],"Brainstorm" : [10,3,3,4,2,6,9,9],
                "Hubcap" : [8,5,6,9,3,7,8,7], "Metroplex": [5,8,7,9,4,6,4,8],
                "Optimus_Prime":[7,8,8,9,5,9,8,8],"Repugnus":[7,7,4,7,6,7,3,7], "Wheeljack": [9,2,2,6,7,8,6,6]}
        result_sum_aut ={}
        for m,n in dict_sum_aut.items():
            result_sum_aut[m]=sum(n)

       
        print "Battle started"
        battle_count += 1
        
        #finding winner depending on what player is chosen
        print(selected_transformer)
        print("SUM AUT", result_sum_aut)
        print selected_transformer2
        print("SUM DEC", result_sum_dec)

        transformer1_value=[]
        for key1, value1 in selected_transformer.items():
            if key1 in result_sum_aut.keys():
                transformer1_value.append(result_sum_aut[key1])
        print(transformer1_value)


        transformer2_value=[]
        for key1, value1 in selected_transformer2.items():
            if key1 in result_sum_dec.keys():
                transformer2_value.append(result_sum_dec[key1])
        print(transformer2_value)


    if transformer1_value[0] > transformer2_value[0]:
        aut_win_counts += 1
        print (" Autobot is Winner")
    else:
        dec_win_counts += 1
        print (" Decepticon is Winner")

    # how many battles
    print "No. of battles: {}".format(battle_count)

    # how many survivors
    if aut_win_counts > dec_win_counts:
        while not dq.empty():
            print "Survivors: {}".format(dq.get())
    else:
        while not aq.empty():
            print "Survivors: {}".format(aq.get())
