class Player(object):
    def __init__(self,bankroll = 0):
        bankroll = int(raw_input("The amount of money you want to deposit: "))
        self.bankroll = bankroll
        print "You have successfully deposit:  " , self.bankroll, "dollars"
    
    def add_bankroll(self,amount):
        self.bankroll += amount 
    
    def bankcrupt(self):
        if self.bankroll <= 0:
            return True
        else:
            return False 
        
    def bet(self,amount = 0):
        amount = int(raw_input("Enter how much you want to bet: "))
        self.amount = amount
        self.bankroll = self.bankroll - self.amount
        return self.amount
        
    def win(self,amount):
        self.bankroll += amount
    
    def show_bankroll(self):
        return self.bankroll
    
    def hit(self):
        return raw_input("Would you like to hit? Enter yes or no: \n").lower().startswith('y')

from random import shuffle 

class Cards(object): 
    def __init__(self,original_card=''):
        self.original_card = range(1,15) * 4
        del self.original_card[55]
        del self.original_card[41]
        
    def shuffle(self):
        shuffle(self.original_card)

    def pullcard(self):
        card_receive = self.original_card[0]
        value = 0
        del self.original_card[0]
        if card_receive > 10 and card_receive < 14:
            value = 10
        elif card_receive == 14:
            value = 11
        else:
            value = card_receive
        return card_receive, value
    
    def reset(self):
        self.original_card = range(1,15 )* 4
        del self.original_card[55]
        del self.original_card[41]

def display(card_display = []):
    
    if card_display == 1:
        card_display_str = 'A'
    elif card_display == 11:
        card_display_str = 'J'
    elif card_display == 12:
        card_display_str = 'Q'
    elif card_display == 13:
        card_display_str = 'K'
    elif card_display == 14:
        card_display_str = 'S'
    elif card_display == 10:
        card_display_str = 'X'
    else:
        card_display_str = str(card_display)
    
    return card_display_str

class Bank(object):
    def __init__(self,amount = 0):
        self.amount = amount
        
    def bank_add(self,add):
        self.amount +=add
    
    def bank_reset(self):
        self.amount = 0
        
    def bank_show(self):
        return self.amount

def win_check(card):
    if sum(card[1:22:2]) == 21:
        return True 

def bust_check(card):
    if sum(card[1:22:2]) > 21:
        return True
    else:
        return False

def total_points(card):
    return sum(card[1:22:2])

def print_player_card(card):
    print "Player 1 cards on hand are: ", card
    
def print_dealer_card(card):
    print "Dealer cards on hand are: ", card

def playgame():
    
    player_1 = Player()
    log = 0

    while True:
        log += 1
        print "\n This is the ", log, "round of the game! \n"
        money = Bank()
        money.bank_add(player_1.bet())
        print 'Total Money from Player on the table: ', money.bank_show()
        game = Cards()
        game.reset()
        game.shuffle()
        print "The Game is ON!"
        print game.original_card
        player_1_card = []
        player_2_card = []
        player_1_display = [] 
        player_2_display = [] 

        for i in xrange(0,4,2):
            player_1_card[i:i+2] = game.pullcard()
            print player_1_card[i]
            player_1_display += display(player_1_card[i])
            player_2_card[i:i+2] = game.pullcard()
            print player_2_card[i]
            player_2_display += display(player_2_card[i])
        print "Player 1 cards on hand are: ", player_1_display
        print "Automated Dealer cards on hand are: ", player_2_display
        
        if win_check(player_1_card):  
            print "Black Jack, Player win!!"
            player_1.add_bankroll(money.bank_show() * 2)
            print "Your currentt bankroll is: ", player_1.show_bankroll()
            money.bank_reset()
            break
            
        elif win_check(player_2_card):
            print "Black Jack, Dealer win!!"
            print "Player bankroll is: ", player_1.show_bankroll()
            money.bank_reset()
            break
        
        elif bust_check(player_1_card):
            print "Player cards over 21 points, Game needs to restart! \n"
            money.bank_reset()
            break 
            
        elif bust_check(player_2_card):
            print "Dealer cards over 21 points, Game needs to restart! \n"
            money.bank_reset()
            break 
        
        else:
            j = 4
            ACE_1 = False
            ACE_2 = False 
            game_on = True 
            dealer_turn = False 
            
            while game_on: 
                
                control = 0
                
                if player_1.hit():
                    control += 1
                    player_1_card[j:j+2] = game.pullcard()
                    player_1_display += display(player_1_card[j])
                    print_player_card(player_1_display)
                    
                    print "Total point for player 1 is:  ", total_points(player_1_card)
                    
                    if win_check(player_1_card):  
                        print "Black Jack, Player win!!"
                        player_1.add_bankroll(money.bank_show() * 2)
                        print "Your currentt bankroll is: ", player_1.show_bankroll()
                        money.bank_reset()
                        break
                        
                    if player_1_card[j+1] == '11':
                        ACE_1 = True
                        
                    if bust_check(player_1_card):
                        if ACE_1 == False:
                            game_on = False
                            print_player_card(player_1_display)
                            print_dealer_card(player_2_display)
                            print "Player Card bust, you lose the game! /n"
                            print "Your currentt bankroll is: ", player_1.show_bankroll()
                            money.bank_reset()
                            break
                        
                        else:
                            
                            player_1_card[j+1] = 1
                            
                            if bust_check(player_1_card):
                                game_on = False 
                                print_player_card(player_1_display)
                                print_dealer_card(player_2_display)
                                print "Player Card bust, you lose the game! /n"
                                print "Your current bankroll is: ", player_1.show_bankroll()
                                money.bank_reset()
                                break
                                
                            if win_check(player_1_card):  
                                print "Black Jack, Player win!!"
                                player_1.add_bankroll(money.bank_show() * 2)
                                print "Your currentt bankroll is: ", player_1.show_bankroll()
                                money.bank_reset()
                                break
                
                
                
                if total_points(player_2_card) < 17:
                    control += 1
                    print "Dealer pull card"
                    player_2_card[j:j+2] = game.pullcard()
                    player_2_display += display(player_2_card[j])
                    print_dealer_card(player_2_display)

                    if player_2_card[j+1] == '11':
                        ACE_2 = True 
                        
                    if win_check(player_2_card):  
                        print "Black Jack, Dealer win!!"
                        print "Player bankroll is: ", player_1.show_bankroll()
                        money.bank_reset()
                        break
                    
                    if bust_check(player_2_card):
                        if ACE_2 == False:
                            game_on = False
                            player_1.add_bankroll(money.bank_show() * 2)
                            print_player_card(player_1_display)
                            print_dealer_card(player_2_display)
                            print "Dearler bust, Player win the game! /n"
                            money.bank_reset()
                            print "Player current bankroll is: ", player_1.show_bankroll()
                            break
                        else:
                            player_2_card[j+1] = 1
                            
                            if bust_check(player_2_card):
                                game_one = False
                                player_1.add_bankroll(money.bank_show() * 2)
                                print_player_card(player_1_display)
                                print_dealer_card(player_2_display)
                                print "Dearler bust, Player win the game! /n"
                                money.bank_reset()
                                print "Player current bankroll is: ", player_1.show_bankroll()
                            
                            if win_check(player_2_card):  
                                print "Black Jack, Dealer win!!"
                                player_1.add_bankroll(money.bank_show() * 2)
                                print "Player currentt bankroll is: ", player_1.show_bankroll()
                                money.bank_reset()
                                break
                
                if control > 0:
                    
                    print "\n ------Currnet Cards On Table-----  \n"
                    print_player_card(player_1_display)
                    print_dealer_card(player_2_display)
                    print "\n-------Next-------round------- \n"
                    j += 2
                    continue
                
                else:
                    if total_points(player_1_card) > total_points(player_2_card):
                        print "Player 1 win!"
                        player_1.add_bankroll(money.bank_show() * 2)
                        print "Player currentt bankroll is: ", player_1.show_bankroll()
                        money.bank_reset()
                        break
                    
                    elif total_points(player_1_card) < total_points(player_2_card):
                        print "Dealer win!"
                        print "Player currentt bankroll is: ", player_1.show_bankroll()
                        money.bank_reset()
                        break
                    
                    elif total_points(player_1_card) == total_points(player_2_card):
                        print "This is a tie!"
                        player_1.add_bankroll(money.bank_show())
                        print "Player currentt bankroll is: ", player_1.show_bankroll()
                        money.bank_reset()
                        break
                                    
        rematch = raw_input('Would like you to play again? y/n')
        
        if rematch == 'y':
            continue
        else: 
            print "\n------Thanks-----for-------playing!-------"
            print " \n Don't forget to cash your deposit: ", player_1.show_bankroll(), "USD \n"
            break

playgame()
