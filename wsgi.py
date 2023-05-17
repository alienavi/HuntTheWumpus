from app.app import app, socketio
app = app
if __name__=='__main__':
    socketio.run(app, debug=True)