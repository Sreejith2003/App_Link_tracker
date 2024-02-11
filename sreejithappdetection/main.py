from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)

def get_google_links(query, num_links=1):
    try:
        links = list(search(query, num_results=num_links))
        return links
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_links_for_applications(app_names, num_links=1):
    all_links = {}
    for app_name in app_names:
        query = f"{app_name} application"
        links = get_google_links(query, num_links)
        all_links[app_name] = links
    return all_links

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    app_names = request.form.get('app_names')

    if app_names:
        app_names = app_names.split(',')
        app_names = [app.strip() for app in app_names]
    else:
        app_names = []

    all_links = get_links_for_applications(app_names)

    return render_template('results.html', all_links=all_links)

if __name__ == '__main__':
    app.run(debug=True)
