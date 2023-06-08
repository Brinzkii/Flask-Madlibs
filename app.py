from flask import Flask, request, render_template
from stories import story_1, story_2, story_3

app = Flask(__name__)


@app.route("/")
def show_home():
    return render_template("home.html")


@app.route("/form")
def show_form():
    if request.args["stories"] == "story_1":
        story = story_1
    elif request.args["stories"] == "story_2":
        story = story_2
    else:
        story = story_3

    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route("/story")
def show_story():
    prompts = list(request.args.keys())
    print(prompts)
    print(story_2.prompts)

    if prompts == story_1.prompts:
        story = story_1
    elif prompts[0] == "noun":
        story = story_2
    else:
        story = story_3

    text = story.generate(request.args)
    return render_template("story.html", text=text)
