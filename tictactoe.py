"""
Tic Tac Toe Player
"""


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the state.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(state):
    """
    Returns player who has the next turn on a state.
    """
    X_count=0
    O_count=0
    for i in range(3):
        for j in range(3):
            
            if state[i][j]==X:
                X_count+=1
            elif state[i][j]==O:
                O_count+=1
    if X_count>O_count:
        return O
    elif X_count<O_count:
        return X
    else:
        return X

def actions(state):
    """
    Returns set of all possible actions (i, j) available on the state.
    """
    list=[]
    for i in range(len(state[0])):
        for j in range(len(state[0])):
            if state[i][j]==EMPTY:
                list.append((i,j))
    return list

def result(state, action):
    """
    Returns the state that results from making move (i, j) on the state.
    """
    temp_state=[]
    for i in range(3):
        var=[]
        for j in range(3):
            var.append(state[i][j])
        temp_state.append(var)
   
   
    i=action[0]
    j=action[1]
    current_player=player(state)
    temp_state[i][j]=current_player
    return temp_state

def winner(state):
    """
    Returns the winner of the game, if there is one.
    """
    X_list=[X,X,X]
    O_list=[O,O,O]           
    for i in range(3):
        if state[i]==X_list:
            return X
        elif state[i]==O_list:
            return O
    X_count=0
    O_count=0
    for i in range(3):
        X_count=0
        O_count=0
        for j in range(3):
            if state[j][i]==X:
                X_count+=1
            elif state[j][i]==O:
                O_count+=1
        if X_count==3:
            return X
        elif O_count==3:
            return O
        

    X_count=0
    O_count=0
    for i in range(3):
        if(state[i][i]==X):
            X_count+=1
        if(state[i][i]==O):
            O_count+=1
    if X_count==3:
        return X
    if O_count==3:
        return O
    X_count=0
    O_count=0
    for i in range(3):
        if(state[i][2-i]==X):
            X_count+=1
        if(state[i][2-i]==O):
            O_count+=1
    if X_count==3:
        return X
    if O_count==3:
        return O
    
    return None



        
def terminal(state):
    """
    Returns True if game is over, False otherwise.
    """
    winning_player=winner(state)
    if winning_player==X or winning_player==O:
        return True
    for i in range(3):
        for j in range(3):
            if state[i][j]==EMPTY:
                return False
    return True


def utility(state):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if X==winner(state):
        return 1
    elif O==winner(state):
        return -1
    else:
        return 0
def max(a,b):
    if a>b:
        return a
    else:
        return b

def min(a,b):
    if a<b:
        return a
    else:
        return b


def Max_Value(state):
    if terminal(state):
        return utility(state)
    v=-10000
    for action in actions(state):
        temp=result(state,action)
        v=max(v,Min_Value(temp))
    return v



def Min_Value(state):
    if terminal(state):
        return utility(state)
    v=10000
    for action in actions(state):
        temp=result(state,action)
        v=min(v,Max_Value(temp))
        
    return v




def minimax(board):
    """
    Returns the optimal action for the current player on the state.
    """
    current_player=player(board)
    if current_player==X:
        max_val=-1000
        resut_action=None
        temp_state=[]
        for i in range(3):
            var=[]
            for j in range(3):
                var.append(board[i][j])
            temp_state.append(var)
        for action in actions(board):
            temp=Min_Value(result(board,action))
            if temp>max_val:
                max_val=temp
                resut_action=action
        return resut_action

    elif current_player==O:
        min_val=1000
        resut_action=None
        temp_state=[]
        for i in range(3):
            var=[]
            for j in range(3):
                var.append(board[i][j])
            temp_state.append(var)
        for action in actions(board):

            state=result(temp_state,action)
            temp=Max_Value(state)
            if temp<min_val:
                min_val=temp
                resut_action=action

        return resut_action    
    

