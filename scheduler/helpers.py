from geopy.distance import vincenty

def get_best_weekend_index(location, possible_dates):
    #given a location and a date, it finds the best one based on score
    scores = get_scores(location, possible_dates)
    sorted_scores = sorted(scores)
    ranked weekends = []
    for score in sorted_scores:
        ranked_weekends.append(possible_dates[sorted_scores.index(score)])
    return ranked_weekends

def get_scores(location, possible_dates):
    #returns an array of scores for the given location at each date
    scores=[]
    for index in possible_dates:
        if(hackathons[index]>0):
            scores.append(get_weekend_score(location,index))
        else:
            scores.append(0)
    return scores

def get_weekend_score(location, index):
    #returns the score for a given date based on the hackathons in it
    scores = []
    for hackathon in weekends[index]:
        scores.append( 1000/(vincenty( hackathon['location'], location ).miles) )
    return sum(scores)
