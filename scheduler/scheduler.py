from Flask import flask, render_template
from geopy.distance import vincenty

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calc():

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


def get_weekend_score(location, index):
    #returns the score for a given date based on the hackathons in it
    scores = []
    for hackathon in weekends[index]:
        scores.append( 1000/(vincenty( hackathon['location'], location ).miles) )
    return sum(distances)

def get_scores(location, possible_dates):
    #returns an array of scores for the given location at each date
    scores=[]
    for index in possible_dates:
        if(hackathons[index]>0):
            scores.append(get_min_distance(location,index))
        else:
            scores.append(0)
    return scores

def get_best_weekend(location, possible_dates):
    #given a location and a date, it finds the best one based on score
    scores = get_scores(location, possible_dates)
    return dates[scores.index(min(scores))]
