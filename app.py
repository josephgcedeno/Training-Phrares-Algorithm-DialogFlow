@app.route('/',methods=["POST","GET"])
def train_data():
    
    if not session.get('logins') is None:
        if request.method == 'POST':
            list_of_phrases = request.form.getlist('phrases[]')
            intent_id = request.form['intent_id']
            entity = request.form['entity']
       
            diagresponse = append_training_phrases(project_id_df,intent_id,list_of_phrases,entity) if not entity=="" else append_training_phrases(project_id_df,intent_id,list_of_phrases)
            return jsonify({"success":diagresponse})
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        intent_list = json.load(
        open(os.path.join(SITE_ROOT, "static/data", "intents.json")))
        return render_template('traindata.html',intent_option=intent_list)
    session['lasturl'] = 'train_data'
    return render_template('login.html')
