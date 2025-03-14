from django.http import HttpResponse
from django.shortcuts import render

def predict_winner(team1, team2, spinners1, pacers1, all_rounders1, captain1,
                    spinners2, pacers2, all_rounders2, captain2, pitch):
    # Weights for each factor
    w_s = 1.2  # Weight for spinners
    w_p = 1.3  # Weight for pacers
    w_a = 1.5  # Weight for all-rounders
    w_t = 2.0  # Weight for pitch compatibility
    w_c = 1.8  # Weight for captain skill
    
    # Assign captain scores based on experience (this can be improved with real data)
    captain_scores = {
        "experienced": 1.5,
        "moderate": 1.0,
        "new": 0.5
    }
    
    captain_score1 = captain_scores.get(captain1, 1.0)
    captain_score2 = captain_scores.get(captain2, 1.0)
    
    # Assign pitch type score
    pitch_scores = {
        "spin-friendly": 1,
        "pace-friendly": -1,
        "balanced": 0
    }
    
    pitch_score = pitch_scores.get(pitch, 0)
    
    # Calculate team strength based on players
    team_strength1 = (spinners1 * 1.2) + (pacers1 * 1.3) + (all_rounders1 * 1.5)
    team_strength2 = (spinners2 * 1.2) + (pacers2 * 1.3) + (all_rounders2 * 1.5)
    
    # Calculate team scores
    team1_score = (spinners1 * w_s) + (pacers1 * w_p) + (all_rounders1 * w_a) + (pitch_score * w_t) + (captain_score1 * w_c) + team_strength1
    team2_score = (spinners2 * w_s) + (pacers2 * w_p) + (all_rounders2 * w_a) + (pitch_score * w_t) + (captain_score2 * w_c) + team_strength2
    
    print(f"{team1} Score: {team1_score}")
    print(f"{team2} Score: {team2_score}")
    
    if team1_score > team2_score:
        print(f"Predicted Winner: {team1}")
    elif team2_score > team1_score:
        print(f"Predicted Winner: {team2}")
    else:
        print("Match is expected to be very close!")


def index (request):
    return render(request, 'index.html')

def analyze (request):

    team1 = request.POST.get('team1', 'default')
    team2 = request.POST.get('team2', 'default')
    pitch = request.POST.get('pitch', 'default')
    t1spinners = int(request.POST.get('t1spinners', 'default'))
    t1pacers = int(request.POST.get('t1pacers', 'default'))
    t1allrounders = int(request.POST.get('t1allrounders', 'default'))
    t1captain = request.POST.get('t1captain', 'default')
    t2spinners = int(request.POST.get('t2spinners', 'default'))
    t2pacers = int(request.POST.get('t2pacers', 'default'))
    t2allrounders = int(request.POST.get('t2allrounders', 'default'))
    t2captain = request.POST.get('t2captain', 'default')

    print(team1)
    print(team2)

    predict_winner(team1=team1, team2=team2, spinners1=t1spinners, pacers1=t1pacers, all_rounders1=t1allrounders, captain1=t1captain, spinners2=t2spinners, pacers2=t2pacers, all_rounders2=t2allrounders, captain2=t2captain, pitch=pitch)

    return render(request, 'analyze.html')

