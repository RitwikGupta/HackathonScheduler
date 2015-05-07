from Flask import flask, render_template
from geopy.distance import vincenty

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calc():
    possibilities = get_hackathons_at_dates(date_options)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def get_hackathons_at_dates(indexes):
    for index in indexes:
        new_array.append(hackathons[index])
    return new_array

def get_weekend_score(location, index):
    scores = []
    for hackathon in weekends[index]:
        scores.append( 1000/(vincenty( hackathon['location'], location ).miles) )
    return sum(distances)

def get_scores(location):
    scores=[]
    for index in possible_dates:
        if(hackathons[index]>0):
            scores.append(get_min_distance(location,index))
        else:
            scores.append(0)
    return scores
