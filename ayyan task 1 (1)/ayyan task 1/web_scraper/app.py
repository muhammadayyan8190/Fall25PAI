from flask import Flask, render_template, request, redirect, url_for
from scraper import scrape_emails_from_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        if not url:
            return render_template('index.html', error='Please provide a URL.')
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        return redirect(url_for('results', url=url))
    return render_template('index.html')

@app.route('/results')
def results():
    url = request.args.get('url', '')
    if not url:
        return redirect(url_for('index'))
    emails = scrape_emails_from_url(url)
    return render_template('results.html', url=url, emails=emails)

if __name__ == '__main__':
    app.run(debug=True)
