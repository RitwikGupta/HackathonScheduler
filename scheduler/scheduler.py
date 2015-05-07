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

def get_min_distance(location, index):
    distances = []
    for hackathon in weekends[index]:
        distances.append( vincenty( hackathon['location'], location ).miles )
    return (len(distances)>0)? (len(weekends[index]), min(distances)) : (0, None)

def get_distances(location):
    distances=[]
    for index in possible_dates:
        if(hackathons[index]>0):
            distances.append(get_min_distance(location,index))
        else:
            distances.append(None)
    return distances
