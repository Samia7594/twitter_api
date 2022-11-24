from flask import Flask, jsonify, Response, make_response, request, render_template
import tweepy

consumer_key = "CxCkNuSCmuelWNslaQhm9G7bq"
consumer_secret = "gJMNhCM6GoBAeK086LELVSunbdfSo1a02yeR0ehmAKtA8pkUZT"
access_token = "1365307419291746313-i2bEAmjz6NPErFs3cVhyE1LG0KF7SO"
access_secret = "KUCoEdshHZ7VUqKrY7S7FVUrFmjOPaD6uznOoHjzXQhMo"

app = Flask(__name__)

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_secret
)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')


@app.route('/search', methods=['GET'])
def search():
    q = request.args.get('q')
    media = request.args.get('media')

    if not q:
        return not_found('q must be defined in query params')

    res = api.search_tweets( q + " filter:media" if media else q)

    return jsonify([i._json for i in res])


@app.route('/users/<user>', methods=['GET'])
def get_users(user):
    res = api.search_users(user)

    return jsonify([i._json for i in res])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error or 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
