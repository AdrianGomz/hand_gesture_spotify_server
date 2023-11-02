from flask import Flask, request
import webbrowser

app = Flask(__name__)

code = ""
client_id = "d0f0f7d875c745dda41a5f8d4be43a4a"
client_secret = "0a9c2b122bd34e0ba1cb26225dec1877"
redirect_uri = 'http://localhost:3000'
url_accounts = 'https://accounts.spotify.com'
scope = "user-modify-playback-state"

@app.route('/')
def callback():
    global code
    code = request.args.get("code")
    return request.args


@app.route('/authenticate')
def authenticate():
    auth_endpoint = url_accounts[:]+"/authorize"
    auth_endpoint += '?response_type=code'
    auth_endpoint += '&client_id=' + client_id
    auth_endpoint += '&scope=' + scope
    auth_endpoint += '&redirect_uri=' + redirect_uri
    webbrowser.open(auth_endpoint)
    return "<h1>Spotify Auth Window Open</h1>"
    


@app.route('/code', methods=['GET'])
def getCode():
    global code
    return code


if __name__ == '__main__':
    app.run(debug=True, port=3000)
