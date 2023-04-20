from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/')
def questions():
    """Creates HTML input elements per the Story class instance"""

    html = render_template("questions.html", prompts = silly_story.prompts)

    return html

@app.get('/results')
def story_result():
    """Calls get_result_text() method from Class and returns a fun little story"""

    prompts = request.args
    # breakpoint()
    result = silly_story.get_result_text( prompts)

    return render_template("results.html", story = result)

