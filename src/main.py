from ProphetPrediction import ProhetPrediction
from LSTMPrediction import LSTMPrediction
from gather_data import get_data
import git

google, microsoft, apple, jnj, amazon = get_data()

stocks = [['GOOGL', google], ['MSFT', microsoft], ['AAPL', apple],
          ['JNJ', jnj], ['AMZN', amazon]]

days = [7,14,30]

def make_graphs(stocks,days):
    for i in stocks:
        for n in days:
            #ProhetPrediction(i[1],i[0],n)
            #LSTMPrediction(i[1],i[0],n)
            return None
            
make_graphs(stocks,days)

repo = git.Repo(search_parent_directories=True)
repo.git.add('img/Predictions')
repo.git.commit('-m',"Updated images")
repo.git.push('origin', 'master')